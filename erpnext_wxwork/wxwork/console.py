import frappe
from erpnext_wxwork.wxwork import wxwork_user
from erpnext_wxwork.wxwork import notification_log


def test_user():
    user = frappe.get_doc('wxwork_user', "ZhuGuoQing")
    wxwork_user.after_insert(user)


def test_log():
    user = frappe.get_doc('Notification Log', 23)
    notification_log.after_insert(user)
