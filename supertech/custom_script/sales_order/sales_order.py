import frappe
from frappe import _


def before_save(doc, method):
    if doc.customer_category == "Export" and doc.taxes_and_charges != '':
        frappe.throw(frappe._("You can not select sales taxes and template,if customer category is 'Export'."))
     