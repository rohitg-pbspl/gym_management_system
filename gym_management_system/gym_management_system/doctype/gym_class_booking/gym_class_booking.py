# Copyright (c) 2023, Scenarios and contributors
# For license information, please see license.txt

import pandas as pd
import frappe
from frappe.model.document import Document
import datetime

class GymClassBooking(Document):

  def before_save(self):
  
   start_date = datetime.datetime.strptime(self.start_date, '%Y-%m-%d').date()
   
   doc = frappe.get_doc("Plans", self.validity)

   self.end_date = start_date + datetime.timedelta(days=int(doc.validity))
   
   self.remaining_days = (self.end_date - datetime.date.today()).days
   
   if self.remaining_days <= 0:
       self.remaining_days = 0
       self.status = 'Expired'
       
       
    
def notification_mail():

 docs = frappe.get_list("Gym Class Booking", filters={'status':'Active'}, fields = ["class", "gym_member", "trainer", "start_date", "end_date"])
 
 
 for index, item in enumerate(docs):
   
   email = frappe.get_value("Gym Members", item['gym_member'], 'email_id')
   
   item['email'] = email
     

    # specify the start date is 2021 jan 1 st
    # specify the end date is 2021 feb 1 st
   a = pd.date_range(start=item["start_date"], end=item["end_date"])
   
    # display only date using date() function
   for i in a:
    
    if i.date().strftime("%A") == "Wednesday" == datetime.date.today().strftime("%A") and i.date() == datetime.date.today():
      
      
      frappe.sendmail(
        recipients = [item["email"]],
        sender = "rohit.g@promantia.com",
        subject = "Your Classes Attended Data this Week",
        message = f"""In this week you have attended {item['class']} class and it is valid upto {item['end_date']}
      Trainer of this class is {item['trainer']}"""
      )
      
      
    
          
          
            
     
     
     
     
       
       
    
  