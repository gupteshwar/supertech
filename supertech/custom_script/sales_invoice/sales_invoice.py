import frappe
from frappe.utils import now_datetime, time_diff_in_hours,pretty_date, now, add_to_date
from datetime import datetime
from email.utils import formataddr
from frappe import _

ls = []
def sendmail1(doc, method):
        supertech = frappe.db.get_value("Email Account", "Supertech Fabrics", "email_id")
        sender_name = "Supertech Fabrics"
        director = frappe.db.get_value("Email Account", "Utssav Gupta | Director", "email_id")
        plant_manager = "gaurang@utssavgupta.com"
        rajeev = "rajeev@utssavgupta.com"
        i_poc_email = frappe.db.get_value("Customer", doc.customer, "account_manager")
        account_head_email = frappe.db.get_value("Customer", doc.customer, "account_head")
        ms = f'''To<br>
        {doc.customer_name}<br><br>
        Dear Sir,<br><br>
        Your order has been dispatched. Please find below the Invoice particulars against your order no:  {doc.po_no}
        <br><br>
        PO Number : {doc.po_no}<br
        Invoice No : {doc.name}<br>
        Invoice Date : { frappe.utils.formatdate(doc.posting_date, "dd-mm-yyyy") }<br>
        Invoice Amount : {doc.get_formatted("grand_total") }<br>
        <br><br>
        We shall share with you the LR & transportor details in our next email shortly. 
        <br><br>
        Thank you for your business.
        <br><br>
        Sincerely, <br>
        Supertech Fabrics<br><br>
        '''
                
        all_cc = [ director, plant_manager, i_poc_email, account_head_email, rajeev]
        contact = frappe.db.get_list("Contact",{'status':'Passive'},'name' )
        for con in contact:
                doc1 = frappe.get_doc("Contact", con.get('name'))
                for j in doc1.links:
                        if doc.customer == j.link_name:
                                for e in doc1.email_ids:
                                        b = e.email_id
                                        ls.append(b)
                           
        sender = formataddr((sender_name, supertech))
        frappe.sendmail(
        recipients =ls,
        subject = "Your order has been dispatched!!",
        message = ms,
        cc = all_cc,
        sender = sender,
        reference_doctype = "Sales Invoice",
        reference_name	= doc.name,
        now =  True,
        expose_recipients = "header",
        read_receipt = 0,
        is_notification = False,
        attachments = [frappe.attach_print("Sales Invoice", doc.name, print_format="Supertech E - Invoice", print_letterhead=True)]
                
                
                )
        ls.clear()        
       
      
#---------------------------------------------------------------------------------

def before_save(doc, method):
    if doc.customer_category == "Export" and doc.taxes_and_charges != None:
        frappe.throw(frappe._("You can not select sales taxes and template,if customer category is 'Export'."))



#-------------------------------------------------------------------------------
lu = []
def sendmail_on_update(doc, method):
        if doc.send_email == 1 and doc.file:
                supertech = frappe.db.get_value("Email Account", "Supertech Fabrics", "email_id")
                sender_name = "Supertech Fabrics"
                director = frappe.db.get_value("Email Account", "Utssav Gupta | Director", "email_id")
                plant_manager = "gaurang@utssavgupta.com"
                rajeev = "rajeev@utssavgupta.com"
                i_poc_email = frappe.db.get_value("Customer", doc.customer, "account_manager")
                account_head_email = frappe.db.get_value("Customer", doc.customer, "account_head")
                ms = f'''To<br>
                {doc.customer_name}<br><br>
                Dear Sir,<br>
                Please find below the dispatch particulars against your order no:  {doc.po_no}
                <br><br>
                Invoice No : {doc.name}<br>
                Invoice Date : { frappe.utils.formatdate(doc.posting_date, "dd-mm-yyyy") }<br>
                Invoice Amount : {doc.get_formatted("grand_total") }<br>
                Transporter Name : {doc.transporter_name}<br>
                L R No : {doc.lr_number} <br>
                Freight Basis : {doc.local_freight} 
                <br><br>
                PFA enclosed LR Copy.
                <br><br>
                I request you to acknowledge this email as a confirmation when you receive your consignment. 
                <br><br>
                Once again, thank you for your business. We look forward for your next order. 
                <br><br>
                Sincerely, <br>
                Supertech Fabrics<br><br>
                '''
                
                all_cc = [ director, plant_manager, i_poc_email, account_head_email, rajeev]
                
                contact = frappe.db.get_list("Contact",{'status':'Passive'},'name' )
                for con in contact:
                        doc1 = frappe.get_doc("Contact", con.get('name'))
                        for j in doc1.links:
                                if doc.customer == j.link_name:
                                        for e in doc1.email_ids:
                                                b = e.email_id
                                                lu.append(b)
                                     

                sender = formataddr((sender_name, supertech))
                frappe.sendmail(
                recipients =lu,
                subject = "Dispatch details are here",
                message = ms,
                cc = all_cc,
                sender = sender,
                reference_doctype = "Sales Invoice",
                reference_name	= doc.name,
                now =  True,
                expose_recipients = "header",
                read_receipt = 0,
                is_notification = False,
                attachments = [frappe.attach_print("Sales Invoice", doc.name, print_format="Supertech E - Invoice", print_letterhead=True), {"fid": doc.file}]
                        
                        
                )
                lu.clear()





#------------------------------------------------------------------------------
      
  
           
    
                                     

       
                
                
        



                                        



