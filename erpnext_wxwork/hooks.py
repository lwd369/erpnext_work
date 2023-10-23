from . import __version__ as app_version

app_name = "erpnext_wxwork"
app_title = "Erpnext Wxwork"
app_publisher = "zhuguoqing"
app_description = "mixin weixin work"
app_email = "317260164@qq.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpnext_wxwork/css/erpnext_wxwork.css"
# app_include_js = "/assets/erpnext_wxwork/js/erpnext_wxwork.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpnext_wxwork/css/erpnext_wxwork.css"
# web_include_js = "/assets/erpnext_wxwork/js/erpnext_wxwork.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "erpnext_wxwork/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "erpnext_wxwork.utils.jinja_methods",
#	"filters": "erpnext_wxwork.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "erpnext_wxwork.install.before_install"
# after_install = "erpnext_wxwork.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "erpnext_wxwork.uninstall.before_uninstall"
after_uninstall = "erpnext_wxwork.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "erpnext_wxwork.utils.before_app_install"
# after_app_install = "erpnext_wxwork.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "erpnext_wxwork.utils.before_app_uninstall"
# after_app_uninstall = "erpnext_wxwork.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnext_wxwork.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Notification Log": {
		"after_insert": "erpnext_wxwork.wxwork.notification_log.after_insert"
	},
	"wxwork_user": {
		"after_insert": "erpnext_wxwork.wxwork.wxwork_user.after_insert"
	},
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"erpnext_wxwork.tasks.all"
#	],
#	"daily": [
#		"erpnext_wxwork.tasks.daily"
#	],
#	"hourly": [
#		"erpnext_wxwork.tasks.hourly"
#	],
#	"weekly": [
#		"erpnext_wxwork.tasks.weekly"
#	],
#	"monthly": [
#		"erpnext_wxwork.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "erpnext_wxwork.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "erpnext_wxwork.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "erpnext_wxwork.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["erpnext_wxwork.utils.before_request"]
# after_request = ["erpnext_wxwork.utils.after_request"]

# Job Events
# ----------
# before_job = ["erpnext_wxwork.utils.before_job"]
# after_job = ["erpnext_wxwork.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"erpnext_wxwork.auth.validate"
# ]
