import frappe
from redis import Redis
from wechatpy.session.redisstorage import RedisStorage
from erpnext_wxwork.wxwork.wechat_client import WeChatClient


class WxWorkApp(object):
    """
    企业微信APP
    """

    @classmethod
    def push_queue_refresh_token(cls):
        """
        后台刷新Token
        :return:
        """
        frappe.enqueue(method=WxWorkApp.refresh_token, job_name='wxwork_init_refresh_token')

    @classmethod
    def refresh_token(cls):
        token = cls.get_entry_app().access_token
        token1 = cls.get_contact_app().access_token

    @classmethod
    def get_entry_app(cls):
        """获取入口应用"""
        wxwork_setting = frappe.get_single('wxwork_setting')
        if not wxwork_setting.cropid or not wxwork_setting.app_secret:
            return None
        app = cls.__get_app_client(wxwork_setting.cropid, wxwork_setting.get_password("app_secret"), "entry")
        app.agentid = wxwork_setting.agentid
        return app

    @classmethod
    def get_contact_app(cls):
        """获取通讯录应用"""
        wxwork_setting = frappe.get_single('wxwork_setting')
        if not wxwork_setting.cropid or not wxwork_setting.contact_secret:
            frappe.logger().error('企业微信通讯录应用未配置成功')
            return None
        return cls.__get_app_client(wxwork_setting.cropid, wxwork_setting.get_password("contact_secret"), "contact")

    @classmethod
    def __get_app_client(cls, cropid, app_secret, app='app'):
        """
        获取企业微信client
        :param secret: 秘钥
        :return:WeChatClient
        """
        redis_url = frappe.get_conf().get('redis_cache') + '/1'
        redis_client = Redis.from_url(redis_url)
        session_interface = RedisStorage(
            redis_client,
            prefix="wxwork:" + app + ":"
        )
        return WeChatClient(
            cropid,
            app_secret,
            session=session_interface,
        )
