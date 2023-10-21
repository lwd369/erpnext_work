from wechatpy.enterprise.client import api


class WeChatOAuth(api.WeChatOAuth):
    def get_oauth_user_info(self, code):
        """
        获取访问用户身份
        详情请参考
        https://developer.work.weixin.qq.com/document/path/91023

        :param code: 通过成员授权获取到的code
        :return: 返回的 JSON 数据包
        """

        return self._get(
            'auth/getuserinfo',
            params={
                'code': code,
            }
        )