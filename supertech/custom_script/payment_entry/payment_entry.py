import frappe
from frappe.utils import now_datetime, time_diff_in_hours,pretty_date, now, add_to_date
from datetime import datetime
from email.utils import formataddr
from frappe import _


lp = [] 

def payment_sendmail(doc, method):
        supertech = frappe.db.get_value("Email Account", "Supertech Fabrics", "email_id")
        sender_name = "Supertech Fabrics"
        i_poc_email = frappe.db.get_value("Customer", doc.party, "account_manager")
        account_head_email = frappe.db.get_value("Customer", doc.party, "account_head")
        ms = f'''
        Dear Sir,<br><br>
        Thank you for your payment. 
        <br><br>
        With this e-mail, we acknowledge to you that we have received your payment of Rs {doc.get_formatted("paid_amount") }. Please find attached the payment receipt for your reference.
        <br><br>
        
        We appreciate your business and hope that our services were beneficial to you.
        
        <br><br>
        Sincerely, <br>
        Supertech Fabrics<br><br>
        '''
                
        all_cc = [i_poc_email, account_head_email]
        contact = frappe.db.get_list("Contact",{'status':'Passive'},'name' )
        for con in contact:
            doc1 = frappe.get_doc("Contact", con.get('name'))
            for j in doc1.links:
                if doc.party == j.link_name:
                    for e in doc1.email_ids:
                        b = e.email_id
                        lp.append(b)
                           
        sender = formataddr((sender_name, supertech))
        frappe.sendmail(
        recipients =lp,
        subject = "Thank you for the payment.",
        message = ms,
        cc = all_cc,
        sender = sender,
        reference_doctype = "Payment Entry",
        reference_name	= doc.name,
        now =  True,
        expose_recipients = "header",
        read_receipt = 0,
        is_notification = False,
        attachments = [frappe.attach_print("Payment Entry", doc.name, print_format="Payment Receipt", print_letterhead=True)]

                
                
                )
        lp.clear()        


                           
       