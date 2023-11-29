# Copyright (c) 2023, zhuguoqing and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe
from erpnext_wxwork.wxwork.apps import WxWorkApp
from erpnext_wxwork.utils import url_util
from frappe.desk.utils import slug
from frappe.core.utils import html2text


class WxworkNotificationLogs(Document):

    def after_insert(doc, method=None):
        """
        发烧通知
        :param doc:
        :param method:
        :return:
        """

        if doc.user_ids is None:
            return
        entry_app = WxWorkApp.get_entry_app()
        if entry_app is None:
            frappe.msgprint("企业微信未配置成功，无法发送企业微信通知")
            return
        entry_app.message.send_text_card(
            agent_id=entry_app.agentid,
            user_ids=doc.user_ids,
            title=doc.title,
            description=doc.description,
            url=url_util.wxwork_oauth_url(doc.url)
        )
