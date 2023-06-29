# Copyright (c) 2023, Scenarios and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class TrainerRating(Document):
    pass

@frappe.whitelist()
def user_name():
    get_user = frappe.db.get_value("Gym Members", filters={
                                   'name1': frappe.get_user().load_user().name}, fieldname=['name'])

    return get_user