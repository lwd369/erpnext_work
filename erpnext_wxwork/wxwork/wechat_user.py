from wechatpy.enterprise.client import api


class WeChatUser(api.WeChatUser):

    def get_id_list(self):
        """
        获取用户列表ID

        https://developer.work.weixin.qq.com/document/path/96067
        """
        return self._get(
            'user/list_id',
            params={
            }
        )
