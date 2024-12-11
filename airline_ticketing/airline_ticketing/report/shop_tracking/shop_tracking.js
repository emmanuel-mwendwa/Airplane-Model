// Copyright (c) 2024, Mwendwa and contributors
// For license information, please see license.txt

frappe.query_reports["Shop Tracking"] = {
    filters: [
        {
            "fieldname": "airport",
            "label": __("Airport"),
            "fieldtype": "Link",
            "options": "Airport",
            "reqd": 1,
        }
    ],
};

