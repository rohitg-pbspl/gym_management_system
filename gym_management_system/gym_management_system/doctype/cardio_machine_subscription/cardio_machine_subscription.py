# Copyright (c) 2023, Scenarios and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import datetime

class CardioMachineSubscription(Document):

  def before_save(self):
      
   start_date = datetime.datetime.strptime(self.start_date, '%Y-%m-%d').date()
   
   doc = frappe.get_doc("Plans", self.validity)
      
   self.end_date = start_date + datetime.timedelta(days=int(doc.validity))
   
   self.remaining_days = (self.end_date - datetime.date.today()).days
   
   if self.remaining_days <= 0:
       self.remaining_days = 0 
       self.status = 'Expired'
