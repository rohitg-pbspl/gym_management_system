# Copyright (c) 2023, Scenarios and contributors
# For license information, please see license.txt

from frappe.model.document import Document
import frappe
import datetime

class GymMembershipDetails(Document):
    
 def before_save(self):
  
  activation_date = datetime.datetime.strptime(self.activation_date, '%Y-%m-%d').date()
  
  
  self.current_month = datetime.date(2021, (int(str(activation_date)[5:7])), 1).strftime('%B')

  months_to_add = int(self.select_plan[0])
  
  self.last_date_of_plan = activation_date + datetime.timedelta(days=months_to_add*365/12)
  
  self.valid_no_of_days = (self.last_date_of_plan - activation_date).days
  
  self.validity_ends_indays = (self.last_date_of_plan - datetime.date.today()).days
  
  if self.validity_ends_indays <= 0:
      
      self.status = 'Expired'



  
  



