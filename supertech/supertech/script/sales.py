import frappe
from frappe.utils import now_datetime, time_diff_in_hours,pretty_date, now, add_to_date
from datetime import datetime, date
from email.utils import formataddr



@frappe.whitelist()
def sendmail():
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    supertech = frappe.db.get_value("Email Account", "Notifications", "email_id")
    sender_name = "Supertech"
    director = frappe.db.get_value("Email Account", "kiran choudhary gmail", "email_id")
        
    alldoc = frappe.db.get_list("Sales Order",{'docstatus':1},['name', 'modified'] )
    for i in alldoc:
        doc = frappe.get_doc("Sales Order", i.get('name'))
        a1 = str(doc.modified)[:11]
        b1 = str(now_datetime())[:11]
        a = str(doc.modified)[11:13]
        print(type(a))
        b = str(now_datetime())[11:13]
        print(type(a))
        c = (int(b) - int(a))
        if b1 == a1 and c == 2:
            ms = f'''Dear Sir,<br><br>
            Thank you for your order. <br>
            This is to acknowledge you that we are processing your order. In case of a query, our team shall reach out soon. The dispatch date and details shall be notified soon.
            <br><br><br>
            Sincerely,<br>   
            Supertech Fabrics
            '''
            all_cc = [ director, doc.i_poc_email, doc.account_head_email]
            sender = formataddr((sender_name, supertech))

            frappe.sendmail(
            recipients =doc.contact_email,
            subject = "Your order is confirmed!!",
            message = ms,
            cc = all_cc,
            sender = sender,
            reference_doctype = "Sales Order",
            reference_name	= doc.name,
            reply_to = doc.i_poc_email,
            now =  True,
            expose_recipients = "header",
            read_receipt = 0,
            is_notification = False,
            )


@frappe.whitelist()
def sendmail_after_eighteen_hrs():
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    director = frappe.db.get_value("Email Account", "kiran choudhary gmail", "email_id")
    sender_name = "Utssav Gupta | Director"

    alldoc = frappe.db.get_list("Sales Order",{'docstatus':1},['name', 'modified'] )
    for i in alldoc:
        doc = frappe.get_doc("Sales Order", i.get('name'))
        a1 =  add_to_date(str(doc.modified), days=1)[:11]
        b2 = str(now_datetime())[:11]
        b = str(now_datetime())[11:13]
        d = int(b)
        if b2 == a1 and d == 17:
            ms = f'''Dear Sir,<br><br>
             want to reach out personally and thank you for the order. We appreciate your business.<br><br>
             Our team is very customer centric and will make your experience flawless. If at any moment you feel we can do something better or have any concerns, feel free to directly reach out to me on my number +91 9818699837 or email utssav@supertechfabrics.com . I shall be happy to help in any way possible. <br><br>
             Thank you once again!!
             <br><br>
             Sincerely,<br>
             Utssav Gupta,<br>
             Director, <br>
             Supertech Fabrics

            '''
            sender = formataddr((sender_name, director))
            frappe.sendmail(
            recipients =doc.contact_email,
            subject = " Many Thanks for your order !!",
            message = ms,
            sender = sender,
            reference_doctype = "Sales Invoice",
            reference_name	= doc.name,
            now =  True,
            expose_recipients = "header",
            read_receipt = 0,
            is_notification = False,
            
            

            )

#---------------------------------------------one day before due day-----------------
            

@frappe.whitelist()
def sendmail_one_day_before_due_date():
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    supertech = frappe.db.get_value("Email Account", "Notifications", "email_id")
    sender_name = "Supertech"
    email_id = "stf@utssavgupta.com"
    bank = frappe.db.get_value("Terms and Conditions", "Supertech Bank Details", "terms")
    alldoc = frappe.db.get_list("Sales Invoice",{'docstatus':1},['name', 'modified'] )
    for i in alldoc:
        doc = frappe.get_doc("Sales Invoice", i.get('name'))
        a = add_to_date(doc.due_date, days=-1)
        b = now_datetime().date()
        c = str(now_datetime())[11:13]
        d = int(c)
        if b == a and d == 16 and doc.outstanding_amount > 0:
            if doc.po_no:
                ms1 = f'''Invoice No {doc.name} is OVERDUE'''
                ms = f'''To<br>
    {doc.customer_name}<br><br>

    Dear Sir,<br>
    Greetings from Supertech Fabrics, I hope this finds you well.<br>
    We are writing for a gentle reminder that the invoice below is due for Tomorrow.<br><br>
    
    Invoice Date: { frappe.utils.formatdate(doc.posting_date, "dd-mm-yyyy") }<br>
    Invoice Number: {doc.name}
    <br>
    PO No. : {doc.po_no}<br>
    Invoice Amount: {doc.get_formatted("rounded_total") }<br>
    Due Amount: {doc.get_formatted("outstanding_amount") }<br>
    Due Date: { frappe.utils.formatdate(doc.due_date, "dd-mm-yyyy") }
    <br>
    <br>
    We deeply value timely business to enable us to continue serving at our best. 
    It is a sincere request to kindly arrange the payment to process the said invoice and advise us of it.<br><br>
    Please find our Bank Details:<br>
    {bank}
    <br><br>
    If you have processed this recently, then we request you to ignore the mail. <br><br><br>
    Sincerely,<br>
    Supertech Fabrics<br><br><br>
    
                '''
                
                all_cc = [ email_id, doc.i_poc_email, doc.account_head_email]
                sender = formataddr((sender_name, supertech))

                frappe.sendmail(
                recipients =doc.contact_email,
                subject = ms1,
                message = ms,
                cc = all_cc,
                sender = sender,
                reference_doctype = "Sales Invoice",
                reference_name	= doc.name,
                now =  True,
                expose_recipients = "header",
                read_receipt = 0,
                is_notification = False,
                attachments = [frappe.attach_print("Sales Invoice", doc.name, print_format="Supertech Sales Invoice", print_letterhead=True)]
                    
                    )
            else:
                ms1 = f'''Invoice No {doc.name} is OVERDUE'''
                ms = f'''To<br>
    {doc.customer_name}<br><br>

    Dear Sir,<br>
    Greetings from Supertech Fabrics, I hope this finds you well.<br>
    We are writing for a gentle reminder that the invoice below is due for Tomorrow.<br><br>
    
    Invoice Date: { frappe.utils.formatdate(doc.posting_date, "dd-mm-yyyy") }<br>
    Invoice Number: {doc.name}
    <br>
    Invoice Amount: {doc.get_formatted("rounded_total") }<br>
    Due Amount: {doc.get_formatted("outstanding_amount") }<br>
    Due Date: { frappe.utils.formatdate(doc.due_date, "dd-mm-yyyy") }
    <br>
    <br>
    We deeply value timely business to enable us to continue serving at our best. 
    It is a sincere request to kindly arrange the payment to process the said invoice and advise us of it.<br><br>
    Please find our Bank Details:<br>
    {bank}
    <br><br>
    If you have processed this recently, then we request you to ignore the mail. <br><br><br>
    Sincerely,<br>
    Supertech Fabrics<br><br><br>
    
                '''
                
                all_cc = [ email_id, doc.i_poc_email, doc.account_head_email]
                sender = formataddr((sender_name, supertech))

                frappe.sendmail(
                recipients =doc.contact_email,
                subject = ms1,
                message = ms,
                cc = all_cc,
                sender = sender,
                reference_doctype = "Sales Invoice",
                reference_name	= doc.name,
                now =  True,
                expose_recipients = "header",
                read_receipt = 0,
                is_notification = False,
                attachments = [frappe.attach_print("Sales Invoice", doc.name, print_format="Supertech Sales Invoice", print_letterhead=True)]
                    
                    )                    
    
#---------------------------------------------10 days after due date -----------------
            

@frappe.whitelist()
def sendmail_after_ten():
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    supertech = frappe.db.get_value("Email Account", "Notifications", "email_id")
    sender_name = "Supertech"
    email_id = "stf@utssavgupta.com"
    bank = frappe.db.get_value("Terms and Conditions", "Supertech Bank Details", "terms")
    alldoc = frappe.db.get_list("Sales Invoice",{'docstatus':1},['name', 'modified'] )
    for i in alldoc:
        doc = frappe.get_doc("Sales Invoice", i.get('name'))
        a = add_to_date(doc.due_date, days=10)
        b = now_datetime().date()
        c = str(now_datetime())[11:13]
        d = int(c)
        if b == a and d == 16 and doc.outstanding_amount > 0:
            if doc.po_no:
                ms1 = f'''Invoice No {doc.name} is OVERDUE'''
                ms = f'''To<br>
    {doc.customer_name}<br><br>

    Dear Sir,<br>
    Hope you are doing well!<br><br>
    Gentle reminder, payment against invoice no {doc.name} is pending and is due by 10 days.<br><br>
    
    Invoice Date: { frappe.utils.formatdate(doc.posting_date, "dd-mm-yyyy") }<br>
    Invoice Number: {doc.name}
    <br>
    PO No. : {doc.po_no}<br>
    Invoice Amount: {doc.get_formatted("rounded_total") }<br>
    Due Amount: {doc.get_formatted("outstanding_amount") }<br>
    Due Date: { frappe.utils.formatdate(doc.due_date, "dd-mm-yyyy") }
    <br>
    <br>
    It is requested to kindly advise us on the said payment.<br><br>
    For Payment , please find our Bank Details:<br>
    {bank}
    <br><br>
    If you have processed this recently, then we request you to ignore the mail. <br><br><br>
    Sincerely,<br>
    Supertech Fabrics<br><br><br>
    
                '''
                
                
                all_cc = [ email_id, doc.i_poc_email, doc.account_head_email]
                sender = formataddr((sender_name, supertech))

                frappe.sendmail(
                recipients =doc.contact_email,
                subject = ms1,
                message = ms,
                cc = all_cc,
                sender = sender,
                reference_doctype = "Sales Invoice",
                reference_name	= doc.name,
                now =  True,
                expose_recipients = "header",
                read_receipt = 0,
                is_notification = False,
                attachments = [frappe.attach_print("Sales Invoice", doc.name, print_format="Supertech Sales Invoice", print_letterhead=True)]
                    
                    )  
            else:
                ms1 = f'''Invoice No {doc.name} is OVERDUE'''
                ms = f'''To<br>
    {doc.customer_name}<br><br>

    Dear Sir,<br>
    Hope you are doing well!<br><br>
    Gentle reminder, payment against invoice no {doc.name} is pending and is due by 10 days.<br><br>
    
    Invoice Date: { frappe.utils.formatdate(doc.posting_date, "dd-mm-yyyy") }<br>
    Invoice Number: {doc.name}
    <br>
    Invoice Amount: {doc.get_formatted("rounded_total") }<br>
    Due Amount: {doc.get_formatted("outstanding_amount") }<br>
    Due Date: { frappe.utils.formatdate(doc.due_date, "dd-mm-yyyy") }
    <br>
    <br>
    It is requested to kindly advise us on the said payment.<br><br>
    For Payment , please find our Bank Details:<br>
    {bank}
    <br><br>
    If you have processed this recently, then we request you to ignore the mail. <br><br><br>
    Sincerely,<br>
    Supertech Fabrics<br><br><br>
    
                '''
                
                
                all_cc = [ email_id, doc.i_poc_email, doc.account_head_email]
                sender = formataddr((sender_name, supertech))

                frappe.sendmail(
                recipients =doc.contact_email,
                subject = ms1,
                message = ms,
                cc = all_cc,
                sender = sender,
                reference_doctype = "Sales Invoice",
                reference_name	= doc.name,
                now =  True,
                expose_recipients = "header",
                read_receipt = 0,
                is_notification = False,
                attachments = [frappe.attach_print("Sales Invoice", doc.name, print_format="Supertech Sales Invoice", print_letterhead=True)]
                    
                    )                      

   

#---------------------------------------------25 days after due date -----------------
            

@frappe.whitelist()
def sendmail_after_twenty_five():
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    supertech = frappe.db.get_value("Email Account", "Notifications", "email_id")
    sender_name = "Supertech"
    email_id = "stf@utssavgupta.com"
    bank = frappe.db.get_value("Terms and Conditions", "Supertech Bank Details", "terms")
    alldoc = frappe.db.get_list("Sales Invoice",{'docstatus':1},['name', 'modified'] )
    for i in alldoc:
        doc = frappe.get_doc("Sales Invoice", i.get('name'))
        a = add_to_date(doc.due_date, days=25)
        b = now_datetime().date()
        c = str(now_datetime())[11:13]
        d = int(c)
        if b == a and d == 16 and doc.outstanding_amount > 0:
            if doc.po_no:
                ms1 = f'''Invoice No {doc.name} is OVERDUE'''
                ms = f'''To<br>
    {doc.customer_name}<br><br>

    Dear Sir,<br>
    Hope you are doing well!<br><br>
    Gentle reminder, payment against invoice no {doc.name} is pending and is due by 25 days.<br><br>
    
    Invoice Date: { frappe.utils.formatdate(doc.posting_date, "dd-mm-yyyy") }<br>
    Invoice Number: {doc.name}
    <br>
    PO No. : {doc.po_no}<br>
    Invoice Amount: {doc.get_formatted("rounded_total") }<br>
    Due Amount: {doc.get_formatted("outstanding_amount") }<br>
    Due Date: { frappe.utils.formatdate(doc.due_date, "dd-mm-yyyy") }
    <br>
    <br>
    It is requested to kindly advise us on the said payment.<br><br>
    Please find our Bank Details:<br>
    {bank}
    <br><br>
    If you have processed this recently, then we request you to ignore the mail. <br><br><br>
    Sincerely,<br>
    Supertech Fabrics<br><br><br>
    
                '''
                
                
                all_cc = [ email_id, doc.i_poc_email, doc.account_head_email]
                sender = formataddr((sender_name, supertech))

                frappe.sendmail(
                recipients =doc.contact_email,
                subject = ms1,
                message = ms,
                cc = all_cc,
                sender = sender,
                reference_doctype = "Sales Invoice",
                reference_name	= doc.name,
                now =  True,
                expose_recipients = "header",
                read_receipt = 0,
                is_notification = False,
                attachments = [frappe.attach_print("Sales Invoice", doc.name, print_format="Supertech Sales Invoice", print_letterhead=True)]
                    
                    )
            else:
                ms1 = f'''Invoice No {doc.name} is OVERDUE'''
                ms = f'''To<br>
    {doc.customer_name}<br><br>

    Dear Sir,<br>
    Hope you are doing well!<br><br>
    Gentle reminder, payment against invoice no {doc.name} is pending and is due by 25 days.<br><br>
    
    Invoice Date: { frappe.utils.formatdate(doc.posting_date, "dd-mm-yyyy") }<br>
    Invoice Number: {doc.name}
    <br>
    Invoice Amount: {doc.get_formatted("rounded_total") }<br>
    Due Amount: {doc.get_formatted("outstanding_amount") }<br>
    Due Date: { frappe.utils.formatdate(doc.due_date, "dd-mm-yyyy") }
    <br>
    <br>
    It is requested to kindly advise us on the said payment.<br><br>
    Please find our Bank Details:<br>
    {bank}
    <br><br>
    If you have processed this recently, then we request you to ignore the mail. <br><br><br>
    Sincerely,<br>
    Supertech Fabrics<br><br><br>
    
                '''
                
                
                all_cc = [ email_id, doc.i_poc_email, doc.account_head_email]
                sender = formataddr((sender_name, supertech))

                frappe.sendmail(
                recipients =doc.contact_email,
                subject = ms1,
                message = ms,
                cc = all_cc,
                sender = sender,
                reference_doctype = "Sales Invoice",
                reference_name	= doc.name,
                now =  True,
                expose_recipients = "header",
                read_receipt = 0,
                is_notification = False,
                attachments = [frappe.attach_print("Sales Invoice", doc.name, print_format="Supertech Sales Invoice", print_letterhead=True)]
                    
                    )                     
   
#---------------------------------------------45 days after due date -----------------
            

@frappe.whitelist()
def sendmail_after_forty_five():
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    supertech = frappe.db.get_value("Email Account", "Notifications", "email_id")
    sender_name = "Supertech"
    email_id = "stf@utssavgupta.com"
    bank = frappe.db.get_value("Terms and Conditions", "Supertech Bank Details", "terms")
    alldoc = frappe.db.get_list("Sales Invoice",{'docstatus':1},['name', 'modified'] )
    for i in alldoc:
        doc = frappe.get_doc("Sales Invoice", i.get('name'))
        a = add_to_date(doc.due_date, days=45)
        b = now_datetime().date()
        c = str(now_datetime())[11:13]
        d = int(c)
        if b == a and d == 16 and doc.outstanding_amount > 0:
            if doc.po_no:
                ms1 = f'''Invoice No {doc.name} is OVERDUE'''
                ms = f'''To<br>
    {doc.customer_name}<br><br>

    Dear Sir,<br>
    Hope you are doing well!<br><br>
    Gentle reminder, payment against invoice no {doc.name} is pending and is due by 45 days.<br><br>
    
    Invoice Date: { frappe.utils.formatdate(doc.posting_date, "dd-mm-yyyy") }<br>
    Invoice Number: {doc.name}
    <br>
    PO No. : {doc.po_no}<br>
    Invoice Amount: {doc.get_formatted("rounded_total") }<br>
    Due Amount: {doc.get_formatted("outstanding_amount") }<br>
    Due Date: { frappe.utils.formatdate(doc.due_date, "dd-mm-yyyy") }
    <br>
    <br>
    We sincerely request you to kindly arrange for the transfer against the said invoice. Please find our Bank Details:<br>
    {bank}
    <br><br>
    If you have processed this recently, then we request you to ignore the mail. <br><br><br>
    Sincerely,<br>
    Supertech Fabrics<br><br><br>
    
                '''
                
                
                all_cc = [ email_id, doc.i_poc_email, doc.account_head_email]
                sender = formataddr((sender_name, supertech))

                frappe.sendmail(
                recipients =doc.contact_email,
                subject = ms1,
                message = ms,
                cc = all_cc,
                sender = sender,
                reference_doctype = "Sales Invoice",
                reference_name	= doc.name,
                now =  True,
                expose_recipients = "header",
                read_receipt = 0,
                is_notification = False,
                attachments = [frappe.attach_print("Sales Invoice", doc.name, print_format="Supertech Sales Invoice", print_letterhead=True)]
                    
                    )
            else:
                ms1 = f'''Invoice No {doc.name} is OVERDUE'''
                ms = f'''To<br>
    {doc.customer_name}<br><br>

    Dear Sir,<br>
    Hope you are doing well!<br><br>
    Gentle reminder, payment against invoice no {doc.name} is pending and is due by 45 days.<br><br>
    
    Invoice Date: { frappe.utils.formatdate(doc.posting_date, "dd-mm-yyyy") }<br>
    Invoice Number: {doc.name}
    <br>
    Invoice Amount: {doc.get_formatted("rounded_total") }<br>
    Due Amount: {doc.get_formatted("outstanding_amount") }<br>
    Due Date: { frappe.utils.formatdate(doc.due_date, "dd-mm-yyyy") }
    <br>
    <br>
    We sincerely request you to kindly arrange for the transfer against the said invoice. Please find our Bank Details:<br>
    {bank}
    <br><br>
    If you have processed this recently, then we request you to ignore the mail. <br><br><br>
    Sincerely,<br>
    Supertech Fabrics<br><br><br>
    
                '''
                
                
                all_cc = [ email_id, doc.i_poc_email, doc.account_head_email]
                sender = formataddr((sender_name, supertech))

                frappe.sendmail(
                recipients =doc.contact_email,
                subject = ms1,
                message = ms,
                cc = all_cc,
                sender = sender,
                reference_doctype = "Sales Invoice",
                reference_name	= doc.name,
                now =  True,
                expose_recipients = "header",
                read_receipt = 0,
                is_notification = False,
                attachments = [frappe.attach_print("Sales Invoice", doc.name, print_format="Supertech Sales Invoice", print_letterhead=True)]
                    
                    )                    
   


#---------------------------------------------17 days after due date -----------------
            

@frappe.whitelist()
def sendmail_seventeen():
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    supertech = frappe.db.get_value("Email Account", "Notifications", "email_id")
    sender_name = "Sruthi Chopra"
    alldoc = frappe.db.get_list("Sales Invoice",{'docstatus':1},['name', 'modified'] )
    for i in alldoc:
        doc = frappe.get_doc("Sales Invoice", i.get('name'))
        a = add_to_date(doc.due_date, days=17)
        b = now_datetime().date()
        c = str(now_datetime())[11:13]
        d = int(c)
        if b == a and d == 16 and doc.outstanding_amount > 0:
            if doc.po_no:
                ms1 = f'''Invoice No {doc.name} is OVERDUE'''
                ms = f'''Re: {doc.customer_name}<br>
    Hi {doc.account_head_name}

    <br><br>

    The invoice shown below is due from {doc.customer_name} from last 17 days.<br>
    Please contact the client and seek immediate payment.<br>
    Invoice Date: { frappe.utils.formatdate(doc.posting_date, "dd-mm-yyyy") }<br>
    Invoice Number: {doc.name}
    <br>
    PO No. : {doc.po_no}<br>
    Invoice Amount: {doc.get_formatted("rounded_total") }<br>
    Due Amount: {doc.get_formatted("outstanding_amount") }<br>
    Due Date: { frappe.utils.formatdate(doc.due_date, "dd-mm-yyyy") }
    <br>
    <br>
    If this has been processed recently, then we request you to share the payment advice with us.
    <br><br><br>
    Sincerely,<br>
    Supertech Fabrics
    
                '''
                
                recipients = [doc.i_poc_email,doc.account_head_email]
                sender = formataddr((sender_name, supertech))
                frappe.sendmail(
                recipients =recipients,
                subject = ms1,
                message = ms,
                sender = sender,
                reference_doctype = "Sales Invoice",
                reference_name	= doc.name,
                now =  True,
                expose_recipients = "header",
                read_receipt = 0,
                is_notification = False,
                attachments = [frappe.attach_print("Sales Invoice", doc.name, print_format="Supertech Sales Invoice", print_letterhead=True)]
                    
                    )
            else:
                ms1 = f'''Invoice No {doc.name} is OVERDUE'''
                ms = f'''Re: {doc.customer_name}<br>
    Hi {doc.account_head_name}

    <br><br>

    The invoice shown below is due from {doc.customer_name} from last 17 days.<br>
    Please contact the client and seek immediate payment.<br>
    Invoice Date: { frappe.utils.formatdate(doc.posting_date, "dd-mm-yyyy") }<br>
    Invoice Number: {doc.name}
    <br>
    Invoice Amount: {doc.get_formatted("rounded_total") }<br>
    Due Amount: {doc.get_formatted("outstanding_amount") }<br>
    Due Date: { frappe.utils.formatdate(doc.due_date, "dd-mm-yyyy") }
    <br>
    <br>
    If this has been processed recently, then we request you to share the payment advice with us.
    <br><br><br>
    Sincerely,<br>
    Supertech Fabrics
    
                '''
                
                recipients = [doc.i_poc_email,doc.account_head_email]
                sender = formataddr((sender_name, supertech))
                frappe.sendmail(
                recipients =recipients,
                subject = ms1,
                message = ms,
                sender = sender,
                reference_doctype = "Sales Invoice",
                reference_name	= doc.name,
                now =  True,
                expose_recipients = "header",
                read_receipt = 0,
                is_notification = False,
                attachments = [frappe.attach_print("Sales Invoice", doc.name, print_format="Supertech Sales Invoice", print_letterhead=True)]
                    
                    )                    
    
#---------------------------------------------35 days after due date -----------------
            

@frappe.whitelist()
def sendmail_thirty_five():
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    supertech = frappe.db.get_value("Email Account", "Notifications", "email_id")
    sender_name = "Sruthi Chopra"
    alldoc = frappe.db.get_list("Sales Invoice",{'docstatus':1},['name', 'modified'] )
    for i in alldoc:
        doc = frappe.get_doc("Sales Invoice", i.get('name'))
        a = add_to_date(doc.due_date, days=35)
        b = now_datetime().date()
        c = str(now_datetime())[11:13]
        d = int(c)
        if b == a and d == 16 and doc.outstanding_amount > 0:
            if doc.po_no:
                ms1 = f'''Invoice No {doc.name} is OVERDUE'''
                ms = f'''Re: {doc.customer_name}<br>
    Hi {doc.account_head_name}

    <br><br>

    The invoice shown below is due from {doc.customer_name} from last 35 days.<br>
    Please contact the client and seek immediate payment.<br>
    Invoice Date: { frappe.utils.formatdate(doc.posting_date, "dd-mm-yyyy") }<br>
    Invoice Number: {doc.name}
    <br>
    PO No. : {doc.po_no}<br>
    Invoice Amount: {doc.get_formatted("rounded_total") }<br>
    Due Amount: {doc.get_formatted("outstanding_amount") }<br>
    Due Date: { frappe.utils.formatdate(doc.due_date, "dd-mm-yyyy") }
    <br>
    <br>
    If this has been processed recently, then we request you to share the payment advice with us.
    <br><br><br>
    Sincerely,<br>
    Supertech Fabrics
    
                '''
                
                recipients = [doc.i_poc_email,doc.account_head_email]
                sender = formataddr((sender_name, supertech))
                frappe.sendmail(
                recipients =recipients,
                subject = ms1,
                message = ms,
                sender = sender,
                reference_doctype = "Sales Invoice",
                reference_name	= doc.name,
                now =  True,
                expose_recipients = "header",
                read_receipt = 0,
                is_notification = False,
                attachments = [frappe.attach_print("Sales Invoice", doc.name, print_format="Supertech Sales Invoice", print_letterhead=True)]
                    
                    )
            else:
                ms1 = f'''Invoice No {doc.name} is OVERDUE'''
                ms = f'''Re: {doc.customer_name}<br>
    Hi {doc.account_head_name}

    <br><br>

    The invoice shown below is due from {doc.customer_name} from last 35 days.<br>
    Please contact the client and seek immediate payment.<br>
    Invoice Date: { frappe.utils.formatdate(doc.posting_date, "dd-mm-yyyy") }<br>
    Invoice Number: {doc.name}
    <br>
    Invoice Amount: {doc.get_formatted("rounded_total") }<br>
    Due Amount: {doc.get_formatted("outstanding_amount") }<br>
    Due Date: { frappe.utils.formatdate(doc.due_date, "dd-mm-yyyy") }
    <br>
    <br>
    If this has been processed recently, then we request you to share the payment advice with us.
    <br><br><br>
    Sincerely,<br>
    Supertech Fabrics
    
                '''
                
                recipients = [doc.i_poc_email,doc.account_head_email]
                sender = formataddr((sender_name, supertech))
                frappe.sendmail(
                recipients =recipients,
                subject = ms1,
                message = ms,
                sender = sender,
                reference_doctype = "Sales Invoice",
                reference_name	= doc.name,
                now =  True,
                expose_recipients = "header",
                read_receipt = 0,
                is_notification = False,
                attachments = [frappe.attach_print("Sales Invoice", doc.name, print_format="Supertech Sales Invoice", print_letterhead=True)]
                    
                    )                    
                  

#---------------------------------------------50 days after due date -----------------
            

@frappe.whitelist()
def sendmail_fifty():
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    supertech = frappe.db.get_value("Email Account", "Notifications", "email_id")
    sender_name = "Sruthi Chopra"
    alldoc = frappe.db.get_list("Sales Invoice",{'docstatus':1},['name', 'modified'] )
    for i in alldoc:
        doc = frappe.get_doc("Sales Invoice", i.get('name'))
        a = add_to_date(doc.due_date, days=50)
        b = now_datetime().date()
        c = str(now_datetime())[11:13]
        d = int(c)
        if b == a and d == 16 and doc.outstanding_amount > 0:
            if doc.po_no:
                ms1 = f'''Invoice No {doc.name} is OVERDUE'''
                ms = f'''Re: {doc.customer_name}<br>
    Hi {doc.account_head_name}

    <br><br>

    The invoice shown below is due from {doc.customer_name} from last 50 days.<br>
    Please contact the client and seek immediate payment.<br>
    Invoice Date: { frappe.utils.formatdate(doc.posting_date, "dd-mm-yyyy") }<br>
    Invoice Number: {doc.name}
    <br>
    PO No. : {doc.po_no}<br>
    Invoice Amount: {doc.get_formatted("rounded_total") }<br>
    Due Amount: {doc.get_formatted("outstanding_amount") }<br>
    Due Date: { frappe.utils.formatdate(doc.due_date, "dd-mm-yyyy") }
    <br>
    <br>
    If this has been processed recently, then we request you to share the payment advice with us.
    <br><br><br>
    Sincerely,<br>
    Supertech Fabrics
    
                '''
                
                recipients = [doc.i_poc_email,doc.account_head_email]
                sender = formataddr((sender_name, supertech))
                frappe.sendmail(
                recipients =recipients,
                subject = ms1,
                message = ms,
                sender = sender,
                reference_doctype = "Sales Invoice",
                reference_name	= doc.name,
                now =  True,
                expose_recipients = "header",
                read_receipt = 0,
                is_notification = False,
                attachments = [frappe.attach_print("Sales Invoice", doc.name, print_format="Supertech Sales Invoice", print_letterhead=True)]
                    
                    )
            else:
                ms1 = f'''Invoice No {doc.name} is OVERDUE'''
                ms = f'''Re: {doc.customer_name}<br>
    Hi {doc.account_head_name}

    <br><br>

    The invoice shown below is due from {doc.customer_name} from last 50 days.<br>
    Please contact the client and seek immediate payment.<br>
    Invoice Date: { frappe.utils.formatdate(doc.posting_date, "dd-mm-yyyy") }<br>
    Invoice Number: {doc.name}
    <br>
    Invoice Amount: {doc.get_formatted("rounded_total") }<br>
    Due Amount: {doc.get_formatted("outstanding_amount") }<br>
    Due Date: { frappe.utils.formatdate(doc.due_date, "dd-mm-yyyy") }
    <br>
    <br>
    If this has been processed recently, then we request you to share the payment advice with us.
    <br><br><br>
    Sincerely,<br>
    Supertech Fabrics
    
                '''
                
                recipients = [doc.i_poc_email,doc.account_head_email]
                sender = formataddr((sender_name, supertech))
                frappe.sendmail(
                recipients =recipients,
                subject = ms1,
                message = ms,
                sender = sender,
                reference_doctype = "Sales Invoice",
                reference_name	= doc.name,
                now =  True,
                expose_recipients = "header",
                read_receipt = 0,
                is_notification = False,
                attachments = [frappe.attach_print("Sales Invoice", doc.name, print_format="Supertech Sales Invoice", print_letterhead=True)]
                    
                    )                    
                     
#---------------------------------------------70 days after due date -----------------
            

@frappe.whitelist()
def sendmail_seventy():
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    supertech = frappe.db.get_value("Email Account", "Notifications", "email_id")
    sender_name = "Sruthi Chopra"
        

    alldoc = frappe.db.get_list("Sales Invoice",{'docstatus':1},['name', 'modified'] )
    for i in alldoc:
        doc = frappe.get_doc("Sales Invoice", i.get('name'))
        a = add_to_date(doc.due_date, days=70)
        b = now_datetime().date()
        c = str(now_datetime())[11:13]
        d = int(c)
        if b == a and d == 16 and doc.outstanding_amount > 0:
            if doc.po_no:
                ms1 = f'''Invoice No {doc.name} is OVERDUE'''
                ms = f'''Re: {doc.customer_name}<br>
    Hi {doc.account_head_name}

    <br><br>

    The invoice shown below is due from {doc.customer_name} from last 70 days.<br>
    Please contact the client and seek immediate payment.<br>
    Invoice Date: { frappe.utils.formatdate(doc.posting_date, "dd-mm-yyyy") }<br>
    Invoice Number: {doc.name}
    <br>
    PO No. : {doc.po_no}<br>
    Invoice Amount: {doc.get_formatted("rounded_total") }<br>
    Due Amount: {doc.get_formatted("outstanding_amount") }<br>
    Due Date: { frappe.utils.formatdate(doc.due_date, "dd-mm-yyyy") }
    <br>
    <br>
    If this has been processed recently, then we request you to share the payment advice with us.
    <br><br><br>
    Sincerely,<br>
    Supertech Fabrics
    
                '''
                
                recipients = [doc.i_poc_email,doc.account_head_email]
                sender = formataddr((sender_name, supertech))
                frappe.sendmail(
                recipients =recipients,
                subject = ms1,
                message = ms,
                sender = sender,
                reference_doctype = "Sales Invoice",
                reference_name	= doc.name,
                now =  True,
                expose_recipients = "header",
                read_receipt = 0,
                is_notification = False,
                attachments = [frappe.attach_print("Sales Invoice", doc.name, print_format="Supertech Sales Invoice", print_letterhead=True)]
                    
                    ) 
            else:
                ms1 = f'''Invoice No {doc.name} is OVERDUE'''
                ms = f'''Re: {doc.customer_name}<br>
    Hi {doc.account_head_name}

    <br><br>

    The invoice shown below is due from {doc.customer_name} from last 70 days.<br>
    Please contact the client and seek immediate payment.<br>
    Invoice Date: { frappe.utils.formatdate(doc.posting_date, "dd-mm-yyyy") }<br>
    Invoice Number: {doc.name}
    <br>
    Invoice Amount: {doc.get_formatted("rounded_total") }<br>
    Due Amount: {doc.get_formatted("outstanding_amount") }<br>
    Due Date: { frappe.utils.formatdate(doc.due_date, "dd-mm-yyyy") }
    <br>
    <br>
    If this has been processed recently, then we request you to share the payment advice with us.
    <br><br><br>
    Sincerely,<br>
    Supertech Fabrics
    
                '''
                
                recipients = [doc.i_poc_email,doc.account_head_email]
                sender = formataddr((sender_name, supertech))
                frappe.sendmail(
                recipients =recipients,
                subject = ms1,
                message = ms,
                sender = sender,
                reference_doctype = "Sales Invoice",
                reference_name	= doc.name,
                now =  True,
                expose_recipients = "header",
                read_receipt = 0,
                is_notification = False,
                attachments = [frappe.attach_print("Sales Invoice", doc.name, print_format="Supertech Sales Invoice", print_letterhead=True)]
                    
                    )                         

#---------------------------------------------90 days after due date -----------------
            

@frappe.whitelist()
def sendmail_ninety():
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    supertech = frappe.db.get_value("Email Account", "Notifications", "email_id")
    sender_name = "Sruthi Chopra"

    alldoc = frappe.db.get_list("Sales Invoice",{'docstatus':1},['name', 'modified'] )
    for i in alldoc:
        doc = frappe.get_doc("Sales Invoice", i.get('name'))
        a = add_to_date(doc.due_date, days=90)
        b = now_datetime().date()
        c = str(now_datetime())[11:13]
        d = int(c)
        if b == a and d == 16 and doc.outstanding_amount > 0:
            if doc.po_no:
                ms1 = f'''Invoice No {doc.name} is OVERDUE'''
                ms = f'''Re: {doc.customer_name}<br>
    Hi {doc.account_head_name}

    <br><br>

    The invoice shown below is due from {doc.customer_name} from last 90 days.<br>
    Please contact the client and seek immediate payment.<br>
    Invoice Date: { frappe.utils.formatdate(doc.posting_date, "dd-mm-yyyy") }<br>
    Invoice Number: {doc.name}
    <br>
    PO No. : {doc.po_no}<br>
    Invoice Amount: {doc.get_formatted("rounded_total") }<br>
    Due Amount: {doc.get_formatted("outstanding_amount") }<br>
    Due Date: { frappe.utils.formatdate(doc.due_date, "dd-mm-yyyy") }
    <br>
    <br>
    If this has been processed recently, then we request you to share the payment advice with us.
    <br><br><br>
    Sincerely,<br>
    Supertech Fabrics
    
                '''
                
                recipients = [doc.i_poc_email,doc.account_head_email]
                sender = formataddr((sender_name, supertech))
                frappe.sendmail(
                recipients =recipients,
                subject = ms1,
                message = ms,
                sender = sender,
                reference_doctype = "Sales Invoice",
                reference_name	= doc.name,
                now =  True,
                expose_recipients = "header",
                read_receipt = 0,
                is_notification = False,
                attachments = [frappe.attach_print("Sales Invoice", doc.name, print_format="Supertech Sales Invoice", print_letterhead=True)]
                    
                    )
            else:
                ms1 = f'''Invoice No {doc.name} is OVERDUE'''
                ms = f'''Re: {doc.customer_name}<br>
    Hi {doc.account_head_name}

    <br><br>

    The invoice shown below is due from {doc.customer_name} from last 90 days.<br>
    Please contact the client and seek immediate payment.<br>
    Invoice Date: { frappe.utils.formatdate(doc.posting_date, "dd-mm-yyyy") }<br>
    Invoice Number: {doc.name}
    <br>
    Invoice Amount: {doc.get_formatted("rounded_total") }<br>
    Due Amount: {doc.get_formatted("outstanding_amount") }<br>
    Due Date: { frappe.utils.formatdate(doc.due_date, "dd-mm-yyyy") }
    <br>
    <br>
    If this has been processed recently, then we request you to share the payment advice with us.
    <br><br><br>
    Sincerely,<br>
    Supertech Fabrics
    
                '''
                
                recipients = [doc.i_poc_email,doc.account_head_email]
                sender = formataddr((sender_name, supertech))
                frappe.sendmail(
                recipients =recipients,
                subject = ms1,
                message = ms,
                sender = sender,
                reference_doctype = "Sales Invoice",
                reference_name	= doc.name,
                now =  True,
                expose_recipients = "header",
                read_receipt = 0,
                is_notification = False,
                attachments = [frappe.attach_print("Sales Invoice", doc.name, print_format="Supertech Sales Invoice", print_letterhead=True)]
                    
                    )