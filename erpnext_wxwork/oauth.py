import frappe
from erpnext_wxwork.wxwork.apps import WxWorkApp


@frappe.whitelist(allow_guest=True)
def redirect(url):
    is_logged_in = frappe.session.user != "Guest"
    if is_logged_in:
        # 已经登录了，直接重定向
        frappe.local.response["type"] = "redirect"
        frappe.local.response["location"] = url
    else:
        # 企业微信oauth2
        client = WxWorkApp.get_entry_app()
        wx_login_url = "http://erp.asymall.com/api/method/erpnext_wxwork.oauth.wxwork_login"
        redirect_url = client.oauth.authorize_url(wx_login_url, url)
        frappe.local.response["type"] = "redirect"
        frappe.local.response["location"] = redirect_url


@frappe.whitelist(allow_guest=True)
def wxwork_login(code, state):
    client = WxWorkApp.get_entry_app()
    info = client.oauth.get_oauth_user_info(code)
    if 0 != info['errcode']:
        # 企业微信登录失败，直接导航
        frappe.local.response["type"] = "redirect"
        frappe.local.response["location"] = state

    userid = info['userid']
    #ToDo 处理数据 跟进企业微信ID获取用户ID
    frappe.local.login_manager.user = "zhuguoqing@asymall.com"
    frappe.local.login_manager.post_login()

    frappe.local.response["type"] = "redirect"
    frappe.local.response["location"] = state
