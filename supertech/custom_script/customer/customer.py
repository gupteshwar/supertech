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
                                and transaction_date 
                                 between '{add_to_date(today(), days=-365, as_string=True)}' 
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



@frappe.whitelist()
def calculate_profitablitys(customer):
    dd = frappe.db.sql(f""" select
                                qi.qty, 
                                qi.rate, 
                                qi.rmc_,
                                qi.rmc_*qi.qty as rm_value,
                                qi.rmc_*qi.qty as sales_value,
                                (qi.rmc_*qi.qty) / (qi.rate*qi.qty) as RMC,
                                (sum(qi.rmc_*qi.qty) / sum(qi.rate*qi.qty))/100 as RMC_total
                            from 
                              `tabQuotation Item` qi
                            
                            left join `tabQuotation` q on qi.parent = q.name
                            where q.party_name = '{customer}' and qi.rmc_ != 0 
                                and  q.transaction_date 
                                 between '{add_to_date(today(), days=-365, as_string=True)}' 
                                 and '{today()}'
                """,as_dict=1)
    count  = 0
    if dd[0]['RMC_total'] != None:
        count = dd[0]['RMC_total']

    if count < 50:
        frappe.db.set_value('Customer', customer, 'profitablity',10)
        frappe.db.commit()
        return 50,count

    elif 50 < count <= 55:
        frappe.db.set_value('Customer', customer, 'profitablity',9)
        frappe.db.commit()
        return 50,count

    elif 55 < count <= 60:
        frappe.db.set_value('Customer', customer, 'profitablity',8)
        frappe.db.commit()
        return 55,count

    elif 60 < count <= 65:
        frappe.db.set_value('Customer', customer, 'profitablity',7)
        frappe.db.commit()
        return 60,count

    elif 65 < count <= 70:
        frappe.db.set_value('Customer', customer, 'profitablity',5)
        frappe.db.commit()
        return 65,count

    elif 70 < count <= 75:
        frappe.db.set_value('Customer', customer, 'profitablity',3)
        frappe.db.commit()
        return 70,count

    elif 75 < count <= 80:
        frappe.db.set_value('Customer', customer, 'profitablity',2)
        frappe.db.commit()
        return 75,count

    elif 80 < count:
        frappe.db.set_value('Customer', customer, 'profitablity',1)
        frappe.db.commit()
        return 80,count

    return dd[0]['RMC_total']




import time

@frappe.whitelist()
def customer_scoring():
    customers = frappe.db.get_list('Customer')
    start = time.time()

    for i in customers:
        calculate_volume(i.name)
        calculate_profitablitys(i.name)        
    # record end time
    end = time.time()
    
    # print the difference between start
    # and end time in milli. secs
    print("The time of execution of above program is :",
        (end-start) * 10**3, "ms")
    return 'done'