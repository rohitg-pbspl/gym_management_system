# Copyright (c) 2023, Scenarios and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
    columns, data = [
        {
            "label": "Month",
            "fieldname": "month",
            "fieldtype": "data",
            "width": 230,
        },
        {
            "label": "Revenue",
            "fieldname": "revenue",
            "fieldtype": "float",
            "width": 230,
        },

    ], []

    records = frappe.get_all("Gym Membership Details", fields=[
                             'amount', 'current_month'])
    
    machine_records = frappe.get_all("Cardio Machine Subscription", fields=[
                             'subscription_amount', 'month'])

    revenue_by_month = {}

    for record in records:
        if record.current_month in revenue_by_month:
            revenue_by_month[record.current_month] = revenue_by_month[record.current_month] + record.amount
        else:
            revenue_by_month[record.current_month] = record.amount
            
    for records in machine_records:
        if records.month in revenue_by_month:
            revenue_by_month[records.month] = revenue_by_month[records.month] + records.subscription_amount
        else:
            revenue_by_month[records.month] = records.subscription_amount

    revenues = []
    
    for month, revenue in revenue_by_month.items():
        data.append(frappe._dict({"month": month, "revenue": revenue}))
        revenues.append(revenue)
    
    total_revenue = sum(revenues)

    chart = {
        "data": {
            "labels": [d.month for d in data],
            "datasets": [{
                "name": "Revenue by Month",
                        "values": [d.revenue for d in data],
            }]
        },
        "type": "pie",
    }
    
    report_summary = {
        "value": total_revenue,
        "label": _("Total Revenue"),
        "datatype": "Currency",
        "indicator": "Green" if total_revenue > 0 else "Red",
        "currency": "INR",
    },

    return columns, data, None, chart, report_summary
