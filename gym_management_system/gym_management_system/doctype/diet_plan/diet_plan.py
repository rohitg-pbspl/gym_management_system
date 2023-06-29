# Copyright (c) 2023, Scenarios and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import datetime


class DietPlan(Document):

    def before_save(self):

        start_date = datetime.datetime.strptime(
            self.start_date, '%Y-%m-%d').date()

        end_date = datetime.datetime.strptime(self.end_date, '%Y-%m-%d').date()

        self.duration = (end_date - start_date).days

        if datetime.date.today() > end_date:
            self.duration = 0
            self.status = "Expired"
