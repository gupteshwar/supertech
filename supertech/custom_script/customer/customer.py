import frappe
from frappe.utils import today,add_to_date,money_in_words

@frappe.whitelist()
def calculate_volume(customer):
    dd = frappe.db.sql(f"""   select 
                                sum(grand_total) as count 
                            from 
                                `tabSales Order` 
                             where 
                                docstatus = 1 and
                                customer = '{customer}' 
                                and transaction_date between '{add_to_date(today(), days=-365, as_string=True)}' 
                                and '{today()}'
                                """,as_dict=1)
    count=0
    if dd[0]['count'] != None:
        count = int(dd[0]['count'])

# less than 20
    if count < 2000000:
        frappe.db.set_value('Customer', customer, 'volume',1)
        frappe.db.commit()
        return 2000000,'small',money_in_words(count, 'INR')
# 20-30
    elif 2000000 < count <= 3000000:
        frappe.db.set_value('Customer', customer, 'volume',2)
        frappe.db.commit()
        return 2000000,money_in_words(count, 'INR')
# 30-40
    elif 3000000 < count <= 4000000:
        frappe.db.set_value('Customer', customer, 'volume',3)
        frappe.db.commit()
        return 3000000,money_in_words(count, 'INR')
# 40-50
    elif 4000000 < count <= 5000000:
        frappe.db.set_value('Customer', customer, 'volume',4)
        frappe.db.commit()
        return 4000000,money_in_words(count, 'INR')
# 50-60
    elif 5000000 < count <= 6000000:
        frappe.db.set_value('Customer', customer, 'volume',5)
        frappe.db.commit()
        return 5000000,money_in_words(count, 'INR')
# 60-70
    elif 6000000 < count <= 7000000:
        frappe.db.set_value('Customer', customer, 'volume',6)
        frappe.db.commit()
        return 6000000,money_in_words(count, 'INR')
# 70-80
    elif 7000000 < count <= 8000000:
        frappe.db.set_value('Customer', customer, 'volume',7)
        frappe.db.commit()
        return 7000000,money_in_words(count, 'INR')
# 80-90
    elif 8000000 < count <= 9000000:
        frappe.db.set_value('Customer', customer, 'volume',8)
        frappe.db.commit()
        return 8000000,money_in_words(count, 'INR')
# 90-100 
    elif 9000000 < count <= 10000000:
        frappe.db.set_value('Customer', customer, 'volume',9)
        frappe.db.commit()
        return 9000000,money_in_words(count, 'INR')
# Above 1 cr
    elif 10000000 < count:
        frappe.db.set_value('Customer', customer, 'volume',10)
        frappe.db.commit()

        return 10000000,money_in_words(count, 'INR')

 
   
    return money_in_words(count, 'INR')