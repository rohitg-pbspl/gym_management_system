# Copyright (c) 2023, Scenarios and contributors
# For license information, please see license.txt

import frappe


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

    revenue_by_month = {}

    for record in records:
        if record.current_month in revenue_by_month:
            revenue_by_month[record.current_month] = revenue_by_month[record.current_month] + record.amount
        else:
            revenue_by_month[record.current_month] = record.amount

    for month, revenue in revenue_by_month.items():
        data.append(frappe._dict({"month": month, "revenue": revenue}))

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

    return columns, data, None, chart, None
