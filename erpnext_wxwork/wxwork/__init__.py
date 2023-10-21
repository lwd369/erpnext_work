import frappe
from erpnext_wxwork.wxwork.apps import WxWorkApp

"""
启动后刷新一次
"""
WxWorkApp.push_queue_refresh_token()
