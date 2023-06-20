import frappe

def delete_email_queues():
    # '''method deletes email queues whose status is in Sent and/or Error'''
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! weekday ---", frappe.utils.get_datetime().weekday() )

    #checking the day of the week, the script only works on monday, wednesday and friday
    # if not frappe.utils.get_datetime().weekday() in [1,3,5,6]:
    if frappe.utils.get_datetime().weekday() in [0,2,4]:

        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        #getting the tuple of names of Email Queues with status in Sent or Error
        deletable_email_queues_tuple = frappe.db.sql('''
        SELECT
            name
        FROM
            `tabEmail Queue`
        WHERE
            status
        IN
            ('Sent', 'Error')
        ''')
            
            #deleting the email queues in safe update mode
        frappe.db.sql('''
        DELETE FROM
            `tabEmail Queue`
        WHERE
            name
        IN
            %(deletable_email_queues)s;
        ''', values={'deletable_email_queues':deletable_email_queues_tuple})

        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
