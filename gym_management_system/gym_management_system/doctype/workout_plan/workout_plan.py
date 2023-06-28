# Copyright (c) 2023, Scenarios and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import datetime

class WorkoutPlan(Document):
    
  def before_save(self):
      
   start_date = datetime.datetime.strptime(self.start_date, '%Y-%m-%d').date()
   
   end_date = datetime.datetime.strptime(self.end_date, '%Y-%m-%d').date()
   
   
   self.duration = (end_date - start_date).days
   
   if datetime.date.today() > end_date:
       self.duration = 0
       self.status = "Expired"
       
       
@frappe.whitelist()
def get_workouts(state):
  get_doc = frappe.get_doc("Workout All Plans", state)
  
  child_table = get_doc.get("workout_plan_exercise")
  
  child_table_data_list = [ ]
  child_table_data = { }
  
  
  for child in child_table:
    child_table_data[child.weekly] = child.workout
     
  for weekly, workout in child_table_data.items():
    child_table_data_list.append(frappe._dict({"weekday":weekly, "workout":workout}))
  
  return child_table_data_list