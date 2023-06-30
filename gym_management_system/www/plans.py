import frappe
from gym_management_system.gym_management_system.doctype.cardio_machine_subscription.cardio_machine_subscription import user_name


def get_context(context):

    
    context.plans = frappe.get_list("Gym Membership Details",
                            filters={'status': 'Active', 'gym_member': user_name()},
                            fields=['gym_member', 'status', 'activation_date', 'trainer_name', 'validity_ends_indays', 'time_slot', 'last_date_of_plan', 'valid_no_of_days', 'select_plan', 'amount', 'trainer_contact'],)
    
    context.expired_plans = frappe.get_list("Gym Membership Details",
                            filters={'status': 'Expired', 'gym_member': user_name()},
                            fields=['gym_member', 'status', 'activation_date', 'trainer_name', 'time_slot', 'last_date_of_plan', 'valid_no_of_days', 'select_plan', 'amount', 'trainer_contact'],)
