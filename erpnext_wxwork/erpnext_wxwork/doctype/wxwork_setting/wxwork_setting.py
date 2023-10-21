# Copyright (c) 2023, zhuguoqing and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class wxwork_setting(Document):
    def before_save(self):
        # 设置默认过期时间
        if 0 == self.app_token_expire:
            self.app_token_expire = 7200

        if 0 == self.contact_token_expire:
            self.contact_token_expire = 7200
