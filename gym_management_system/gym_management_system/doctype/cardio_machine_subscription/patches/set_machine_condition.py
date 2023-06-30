import frappe


def execute():
    machine_subscriptions = frappe.get_all("Cardio Machine Subscription", fields=[
                                           "name", "is_machine_condition_ok"])

    for machines in machine_subscriptions:
        if machines.is_machine_condition_ok:
            frappe.db.set_value("Cardio Machine Subscription", machines.name,
                                "machine_condition", "Working Properly", update_modified=False)
        else:
            frappe.db.set_value("Cardio Machine Subscription", machines.name,
                                "machine_condition", "Not Working Properly", update_modified=False)
