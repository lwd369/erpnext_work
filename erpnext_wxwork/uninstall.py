import frappe


def after_uninstall():
    # TODO 还不清楚为什么无法删除 wxwork_setting
    # frappe.get_single("wxwork_setting").delete()
    pass
