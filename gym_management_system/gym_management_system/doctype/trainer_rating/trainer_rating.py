# Copyright (c) 2023, Scenarios and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class TrainerRating(Document):
	
 def before_save(self):
   
   
   
   get_user = frappe.get_user().load_user()
   
   gym_member = frappe.db.get_value("Gym Members", filters={'email_id':get_user.email}, fieldname=['name'])
      
   self.gym_member = gym_member