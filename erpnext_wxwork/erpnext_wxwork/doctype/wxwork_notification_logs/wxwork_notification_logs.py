# Copyright (c) 2023, zhuguoqing and contributors
# For license information, please see license.txt

from frappe.model.document import Document
import frappe
from erpnext_wxwork.wxwork.apps import WxWorkApp
from erpnext_wxwork.utils import url_util
from frappe.desk.utils import slug
from frappe.core.utils import html2text

# 设置日志级别和创建专用logger
frappe.utils.logger.set_log_level("DEBUG")
logger = frappe.logger("wxwork", allow_site=True, file_count=50)

class WxworkNotificationLogs(Document):

    def after_insert(doc, method=None):
        """
        发送企业微信通知
        :param doc:
        :param method:
        :return:
        """
        logger.info(f"开始处理企业微信通知: {doc.name}")
        
        # 检查用户ID
        logger.info(f"检查用户ID: {doc.user_ids}")
        if doc.user_ids is None:
            logger.info("用户ID为空，跳过发送")
            return
            
        # 获取企业微信应用
        logger.info("获取企业微信应用配置")
        entry_app = WxWorkApp.get_entry_app()
        if entry_app is None:
            logger.error("企业微信未配置成功，无法发送企业微信通知")
            frappe.msgprint("企业微信未配置成功，无法发送企业微信通知")
            return
            
        logger.info(f"企业微信应用获取成功，AgentID: {entry_app.agentid}")
        
        # 准备发送参数
        logger.info(f"准备发送参数 - 标题: {doc.title}, 用户: {doc.user_ids}")
        logger.debug(f"描述内容: {doc.description[:100] if doc.description else 'None'}...")
        logger.debug(f"跳转URL: {doc.url}")
        
        try:
            # 发送企业微信消息
            logger.info("开始发送企业微信文本卡片消息")
            result = entry_app.message.send_text_card(
                agent_id=entry_app.agentid,
                user_ids=doc.user_ids,
                title=doc.title,
                description=doc.description,
                url=url_util.wxwork_oauth_url(doc.url)
            )
            logger.info(f"企业微信消息发送成功，返回结果: {result}")
            
        except Exception as e:
            logger.error(f"企业微信消息发送失败: {str(e)}")
            import traceback
            logger.error(f"详细错误信息: {traceback.format_exc()}")
            # 记录到系统错误日志
            frappe.log_error(f"企业微信通知发送失败: {str(e)}", "WxWork Notification Error")
            raise e
