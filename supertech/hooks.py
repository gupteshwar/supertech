from . import __version__ as app_version

app_name = "supertech"
app_title = "Supertech"
app_publisher = "saad"
app_description = "supertech"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "saad.c@indictranstech.com"
app_license = "MIT"

# Includes in <head>
# ------------------
fixtures = ['Custom Field','Notification','Client Script','Server Script','Webhook','Property Setter', 'Print Format', 'Role', 'Letter Head', 'Print Style', 'Print Settings',"Workflow","Workflow State","Workflow Action","Terms and Conditions", "Letter Head", ]

# include js, css files in header of desk.html
# app_include_css = "/assets/supertech/css/supertech.css"
# app_include_js = "/assets/supertech/js/supertech.js"

# include js, css files in header of web template
# web_include_css = "/assets/supertech/css/supertech.css"
# web_include_js = "/assets/supertech/js/supertech.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "supertech/public/scss/website"

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

# Installation
# ------------

# before_install = "supertech.install.before_install"
# after_install = "supertech.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "supertech.uninstall.before_uninstall"
# after_uninstall = "supertech.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "supertech.notifications.get_notification_config"

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
# doctype_js = {
# 	"Sales Invoice" : "supertech/custom_script/sales_invoice/sales_invoice.js",
# 	}

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	
	"Sales Invoice": {
		"on_submit": "supertech.custom_script.sales_invoice.sales_invoice.sendmail1",
		"before_save": "supertech.custom_script.sales_invoice.sales_invoice.before_save"
		
	



},
"Sales Order": {
		"before_save": "supertech.custom_script.sales_order.sales_order.before_save",
},
"Delivery Note": {
		"before_save": "supertech.custom_script.delivery_note.delivery_note.before_save",
}


}

# Scheduled Tasks
# ---------------

scheduler_events = {
	"cron": {
        "0 9 * * *": [
            "supertech.custom_script.customer.customer.customer_scoring"
        ],
        "30 12 * * *": [
            "supertech.custom_script.customer.customer.customer_scoring"
        ],
        "0 17 * * *": [
            "supertech.custom_script.customer.customer.customer_scoring"
        ]
		
		
    },
	# "all": [
	# 	"supertech.tasks.all"
	# ],
	# "daily": [
	# 	"supertech.supertech.script.sales.sendmail_afteroneda",
	# 	"supertech.supertech.script.sales.sendmail_after",
	# 	"supertech.supertech.script.sales.sendmail_function",
	# 	# "supertech.supertech.script.sales.sendmail_function_before_one_day",
	# 	"supertech.supertech.script.sales.sendmail_beforeoneday"
	# ],
	"hourly": [
           "supertech.supertech.script.sales.sendmail",
		   "supertech.supertech.script.sales.sendmail_after_eighteen_hrs",
		   "supertech.supertech.script.sales.sendmail_one_day_before_due_date",
		   "supertech.supertech.script.sales.sendmail_after_ten",
		   "supertech.supertech.script.sales.sendmail_after_twenty_five",
		   "supertech.supertech.script.sales.sendmail_after_forty_five",
		   "supertech.supertech.script.sales.sendmail_seventeen",
		   "supertech.supertech.script.sales.sendmail_thirty_five",
		   "supertech.supertech.script.sales.sendmail_fifty",
		   "supertech.supertech.script.sales.sendmail_seventy",
		   "supertech.supertech.script.sales.sendmail_ninety"
	],
	# "weekly": [
	# 	"supertech.tasks.weekly"
	# ],
	# "monthly": [
	# 	"supertech.tasks.monthly"
	# ]
}

# Testing
# -------

# before_tests = "supertech.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "supertech.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "supertech.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"supertech.auth.validate"
# ]