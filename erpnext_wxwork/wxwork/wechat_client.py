from wechatpy.enterprise import WeChatClient as _WeChatClient
from erpnext_wxwork.wxwork.wechat_user import WeChatUser
from erpnext_wxwork.wxwork.auth import WeChatOAuth


class WeChatClient(_WeChatClient):
    """
    客户端
    """

    """
    定义类型为BaseWeChatAPI的属性，会自动填充请求参数
    """
    user = WeChatUser()
    oauth = WeChatOAuth()

    # 应用ID
    agentid = None
