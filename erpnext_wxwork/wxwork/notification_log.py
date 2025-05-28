import frappe
from erpnext_wxwork.wxwork.apps import WxWorkApp
from erpnext_wxwork.utils import url_util
from frappe.desk.utils import slug
from frappe.core.utils import html2text


def after_insert(doc, method=None):
    """
    发烧通知
    :param doc:
    :param method:
    :return:
    """
    wxwork_userid = frappe.get_value("wxwork_user", {"en_user": doc.for_user}, "wxwork_userid")
    if wxwork_userid is None: return
    entry_app = WxWorkApp.get_entry_app()
    if entry_app is None:
        return frappe.logger().error("企业微信没有配置成功")

    entry_app.message.send_text_card(
        agent_id=entry_app.agentid,
        user_ids=wxwork_userid,
        title="工作通知",
        description='写死的通知内容',
        url="/"
    )
