import frappe


def get_context(context):
    
    context.user = frappe.get_user().load_user()
    
    context.gym_member = frappe.db.get_value("Gym Members", filters={'email_id':context.user.email}, fieldname=['name'])
    
    context.plans = frappe.get_list("Gym Membership Details",
                            filters={'status': 'Active', 'gym_member': context.gym_member},
                            fields=['gym_member', 'status', 'activation_date', 'trainer_name', 'validity_ends_indays', 'time_slot', 'last_date_of_plan', 'valid_no_of_days', 'select_plan', 'amount', 'trainer_contact'],)
    
    context.expired_plans = frappe.get_list("Gym Membership Details",
                            filters={'status': 'Expired', 'gym_member': context.gym_member},
                            fields=['gym_member', 'status', 'activation_date', 'trainer_name', 'time_slot', 'last_date_of_plan', 'valid_no_of_days', 'select_plan', 'amount', 'trainer_contact'],)



@frappe.whitelist()
def calculate_validity():
    gym_member = frappe.db.get_value("Gym Members", filters={'email_id':frappe.get_user().load_user().email}, fieldname=['name'])
    plan = frappe.get_value("Gym Membership Details", filters={'status': 'Active', 'gym_member': gym_member},
                            fieldname=['name'])
    doc = frappe.get_doc("Gym Membership Details", plan)
    
    print(f'this is doc{doc}')
    
    return doc