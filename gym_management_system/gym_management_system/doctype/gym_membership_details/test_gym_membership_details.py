# Copyright (c) 2023, Scenarios and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase
import datetime


class TestGymMembershipDetails(FrappeTestCase):

 def test_check_status(self):
     
   doc = frappe.get_doc(doctype = "Gym Membership Details", gym_member = "GM06230031", trainer="GT036", activation_date="2023-04-01", time_slot="05:00 AM to 07:00 AM")
   
   doc.select_plan = "1 Month"
   
   doc.save()
   
   self.assertEqual(doc.last_date_of_plan, datetime.date(2023, 5, 1))
   
   
   
 def test_check_validity(self):
    
   doc = frappe.get_doc(doctype = "Gym Membership Details", gym_member = "GM06230031", trainer="GT036", activation_date="2023-04-01", time_slot="05:00 AM to 07:00 AM")
   
   doc.select_plan = "1 Month"
   
   doc.save()
   
   self.assertEqual(doc.valid_no_of_days, 30)
   
   self.assertEqual(doc.validity_ends_indays, 0)
