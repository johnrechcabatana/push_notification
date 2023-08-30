from . import __version__ as app_version

app_name = "push_notification"
app_title = "push_notification"
app_publisher = "cabatana.johnrech.g@gmail.com"
app_description = "push_notification"
app_email = "cabatana.johnrech.g@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/push_notification/css/push_notification.css"
# app_include_js = "/assets/push_notification/js/push_notification.js"

# include js, css files in header of web template
# web_include_css = "/assets/push_notification/css/push_notification.css"
# web_include_js = "/assets/push_notification/js/push_notification.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "push_notification/public/scss/website"

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
#	"methods": "push_notification.utils.jinja_methods",
#	"filters": "push_notification.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "push_notification.install.before_install"
# after_install = "push_notification.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "push_notification.uninstall.before_uninstall"
# after_uninstall = "push_notification.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "push_notification.notifications.get_notification_config"

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

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"push_notification.tasks.all"
#	],
#	"daily": [
#		"push_notification.tasks.daily"
#	],
#	"hourly": [
#		"push_notification.tasks.hourly"
#	],
#	"weekly": [
#		"push_notification.tasks.weekly"
#	],
#	"monthly": [
#		"push_notification.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "push_notification.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "push_notification.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "push_notification.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["push_notification.utils.before_request"]
# after_request = ["push_notification.utils.after_request"]

# Job Events
# ----------
# before_job = ["push_notification.utils.before_job"]
# after_job = ["push_notification.utils.after_job"]

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
#	"push_notification.auth.validate"
# ]
