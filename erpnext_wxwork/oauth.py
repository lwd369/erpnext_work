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

    def to_redirect():
        frappe.local.response["type"] = "redirect"
        frappe.local.response["location"] = state

    if 0 != info['errcode']:
        return to_redirect()

    userid = info['userid']
    # ToDo 处理数据 跟进企业微信ID获取用户ID
    wxwork_user = frappe.get_doc("wxwork_user", userid)
    if wxwork_user is None:
        return to_redirect()

    # 登录后再重定向
    frappe.local.login_manager.user = wxwork_user.en_user
    frappe.local.login_manager.post_login()

    to_redirect()
