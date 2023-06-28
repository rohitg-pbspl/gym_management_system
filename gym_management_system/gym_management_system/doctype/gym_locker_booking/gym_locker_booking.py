# Copyright (c) 2023, Scenarios and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GymLockerBooking(Document):
  
 def before_save(self):
   
   data = frappe.db.sql("""
                        SELECT
                          remaining_lockers
                        FROM
                          `tabGym Locker Booking`
                        """)
   data1 = frappe.get_list(doctype='Gym Locker Booking',
                           fields = ['assigned_to']
                           )
   
   names = [d["assigned_to"] for d in data1]
 
   if self.assigned_to in names:
     pass
   else:
    if len(data) == 0 or None:
      self.remaining_lockers = self.total_lockers - 1
 
    elif data[-1][-1] != 0 :
      self.remaining_lockers = data[-1][-1] - 1
    else:
      frappe.throw("Number of Remaining Lockers are zero please contact 'Gym Admin'")
     
     