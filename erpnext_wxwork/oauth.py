import frappe
from erpnext_wxwork.wxwork.apps import WxWorkApp
from urllib.parse import quote


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
        wx_login_url = (frappe.get_conf().domain or frappe.local.site) + "/api/method/erpnext_wxwork.oauth.wxwork_login"

        redirect_url = client.oauth.authorize_url(wx_login_url, quote(url))
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

    wxid = info['userid']
    try:
        wxwork_user = frappe.get_doc("wxwork_user", wxid)
    except frappe.DoesNotExistError:
        return to_redirect()

    frappe.local.login_manager.user = wxwork_user.en_user
    frappe.local.login_manager.post_login()
    to_redirect()
