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
    # print(money_in_words(count, 'INR'))

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
    else:
        frappe.db.set_value('Customer', customer, 'volume',0)
        frappe.db.commit()

        return 10000000,money_in_words(count, 'INR')
    return money_in_words(count, 'INR')



@frappe.whitelist()
def calculate_profitablitys(customer):
    dd = frappe.db.sql(f""" select
                                sum(qi.qty), 
                                sum(qi.rate), 
                                sum(qi.rmc_),
                                sum(qi.rmc_*qi.qty) as rm_value,
                                sum(qi.rate*qi.qty) as sales_value,
                                (sum(qi.rmc_*qi.qty) / sum(qi.rate*qi.qty))*100 as RMC_total

                            from 
                            `tabSales Invoice Item` qi
                            
                            left join `tabSales Invoice` q on qi.parent = q.name
                            
                            where q.customer = '{customer}' 
                             and  q.posting_date 
                                 between '{add_to_date(today(), days=-365, as_string=True)}' 
                                 and '{today()}' and q.status IN ('Draft', 'Submitted');
                            

                """,as_dict=1)
    count  = 0
    if dd[0]['RMC_total'] != None:
        count = dd[0]['RMC_total']

    if count < 50:
        frappe.db.set_value('Customer', customer, 'profitablity',1)
        frappe.db.commit()
        return 50,count

    elif 50 < count <= 55:
        frappe.db.set_value('Customer', customer, 'profitablity',2)
        frappe.db.commit()
        return 50,count

    elif 55 < count <= 60:
        frappe.db.set_value('Customer', customer, 'profitablity',3)
        frappe.db.commit()
        return 55,count

    elif 60 < count <= 65:
        frappe.db.set_value('Customer', customer, 'profitablity',5)
        frappe.db.commit()
        return 60,count

    elif 65 < count <= 70:
        frappe.db.set_value('Customer', customer, 'profitablity',7)
        frappe.db.commit()
        return 65,count

    elif 70 < count <= 75:
        frappe.db.set_value('Customer', customer, 'profitablity',8)
        frappe.db.commit()
        return 70,count

    elif 75 < count <= 80:
        frappe.db.set_value('Customer', customer, 'profitablity',9)
        frappe.db.commit()
        return 75,count

    elif 80 < count:
        frappe.db.set_value('Customer', customer, 'profitablity',10)
        frappe.db.commit()
        return 80,count
    else:
        frappe.db.set_value('Customer', customer, 'profitablity',0)
        frappe.db.commit()
        return 80,count
    return dd[0]['RMC_total']



@frappe.whitelist()
def calaculate_payments(customer):
    dd =frappe.db.sql(f""" 
            select payment_terms from `tabCustomer` where name = '{customer}'
         """,as_dict=1)
    payment = dd[0]['payment_terms']

    if payment ==None or payment == '':
        frappe.db.set_value('Customer', customer, 'payments',0)
        frappe.db.commit()
        return payment

    elif payment =="100% Advance" :
        frappe.db.set_value('Customer', customer, 'payments',10)
        frappe.db.commit()
        return payment
        
    elif payment =="50% Advance & Balance against Delivery" :
        frappe.db.set_value('Customer', customer, 'payments',9)
        frappe.db.commit()
        return payment
        
    elif payment =="30% with PO and balance against Dispatch" :
        frappe.db.set_value('Customer', customer, 'payments',9)
        frappe.db.commit()
        return payment
        
    elif payment =="30% Against Material & 70% within 45 days" :
        frappe.db.set_value('Customer', customer, 'payments',7)
        frappe.db.commit()
        return payment
        
    elif payment =="7 Days after Invoice" :
        frappe.db.set_value('Customer', customer, 'payments',8)
        frappe.db.commit()
        return payment
        
    elif payment =="15 Days after Invoice" :
        frappe.db.set_value('Customer', customer, 'payments',7)
        frappe.db.commit()
        return payment
        
    elif payment =="30 Days after Invoice" :
        frappe.db.set_value('Customer', customer, 'payments',5)
        frappe.db.commit()
        return payment
        
    elif payment =="40 Days after Invoice" :
        frappe.db.set_value('Customer', customer, 'payments',4)
        frappe.db.commit()
        return payment

    elif payment =="45 Days after Invoice" :
        frappe.db.set_value('Customer', customer, 'payments',4)
        frappe.db.commit()
        return payment

    elif payment =="60 Days after Invoice" :
        frappe.db.set_value('Customer', customer, 'payments',4)
        frappe.db.commit()
        return payment

    else:
        frappe.db.set_value('Customer', customer, 'payments',0)
        frappe.db.commit()
        return payment
    return 0


@frappe.whitelist()
def calaculate_payments_delay(customer):
    si_list = frappe.db.sql(f"""  
                            select
                                name,
                                posting_date
                            from
                                `tabSales Invoice`
                            where 
                                customer = '{customer}' 
                            and 
                                status = 'paid'
                            and 
                                 posting_date 
                                 between '{add_to_date(today(), days=-365, as_string=True)}' 
                                 and '{today()}'
                                 and status IN ('Draft', 'Submitted');

                        """,as_dict=1)
                        
    avg = []
    for i in si_list:

        dd = frappe.db.sql(f"""  
                            select 
                            pe.posting_date,
                            per.due_date
                            from 
                            `tabPayment Entry` pe
                            
                            left join `tabPayment Entry Reference` per on pe.name = per.parent
                            
                            where pe.party = '{customer}' and per.reference_doctype = 'Sales Invoice' 
                            and per.reference_name = "{i['name']}"
                            
                            order by pe.posting_date asc
                            
                        """,as_dict=1)
        diff = dd[-1]['posting_date'] - i['posting_date']
        avg.append(int(diff.days))
        
    delay = 0
    if sum(avg) != 0:
        delay= round(sum(avg) / len(avg))
    else:
        delay =  0

    if 0 < delay <= 15:
        frappe.db.set_value('Customer', customer, 'payment_delay',9)
        frappe.db.commit()
        return 50,delay

    elif 15 < delay <= 30:
        frappe.db.set_value('Customer', customer, 'payment_delay',8)
        frappe.db.commit()
        return 55,delay

    elif 30 < delay <= 45:
        frappe.db.set_value('Customer', customer, 'payment_delay',6)
        frappe.db.commit()
        return 60,delay

    elif 45 < delay <= 60:
        frappe.db.set_value('Customer', customer, 'payment_delay',4)
        frappe.db.commit()
        return 65,delay

    elif 60 < delay:
        frappe.db.set_value('Customer', customer, 'payment_delay',1)
        frappe.db.commit()
        return 80,delay

    else:
        frappe.db.set_value('Customer', customer, 'payment_delay',0)
        frappe.db.commit()
        return 80,delay

    return delay


@frappe.whitelist()
def calaculate_overall_score(customer): 
    i = frappe.get_doc('Customer',customer)

    relationship= 0 if i.relationship == None else i.relationship
    loyalty = 0 if i.loyalty == None else i.loyalty


    score = i.profitablity + i.volume + i.payments + i.payment_delay + relationship + loyalty
    frappe.db.set_value('Customer', customer, 'customer_score',score*2)
    frappe.db.commit()     

import time

@frappe.whitelist()
def customer_scoring():
    customers = frappe.db.get_list('Customer')

    start = time.time()

    for i in customers:
        calculate_volume(i.name)
        calculate_profitablitys(i.name)
        calaculate_payments(i.name)
        calaculate_payments_delay(i.name)
        calaculate_overall_score(i.name)
  

    end = time.time()
    

    # print(f"The time of execution of above program is :{(end-start) * 10**3 }ms")
    return f"The time of execution of above program is :{(end-start) * 10**3 }ms"