import frappe
from erpnext_wxwork.wxwork.apps import WxWorkApp
from erpnext_wxwork.utils import url_util


def after_insert(doc, method=None):
    """
    插入成功发送一个链接
    :param doc:
    :param method:
    :return:
    """
    wxwork_userid = doc.wxwork_userid
    entry_app = WxWorkApp.get_entry_app()
    if entry_app is None:
        return frappe.logger().error("企业微信没有配置成功")
    entry_app.message.send_text_card(
        agent_id=entry_app.agentid,
        user_ids=wxwork_userid,
        title="系统通知",
        description="欢迎加入集团系统<br>希望集团系统能帮助你提高工作效率",
        url=url_util.wxwork_oauth_url('/app/home')
    )
