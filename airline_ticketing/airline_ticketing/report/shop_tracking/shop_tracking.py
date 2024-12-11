# Copyright (c) 2024, Mwendwa and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters):

    columns = get_columns()
    data = get_data(filters)

    return columns, data


def get_columns():
    columns = [
        {
            "label": "Airport", 
            "fieldname": "airport", 
            "fieldtype": "Link", 
            "options": "Airport", 
            "width": 200
        },
        {
            "label": "Shop Name",
            "fieldname": "shop_name",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": "Status",
            "fieldname": "status",
            "fieldtype": "Select",
            "width": 120,
        },
        {
            "label": "Total Shops",
            "fieldname": "total_shops",
            "fieldtype": "Int",
            "width": 120
        },
        {
            "label": "Available Shops",
            "fieldname": "available_shops",
            "fieldtype": "Int",
            "width": 120
        },
        {
            "label": "Occupied Shops",
            "fieldname": "occupied_shops",
            "fieldtype": "Int",
            "width": 120
        },
        {
            "label": "Out of Order",
            "fieldname": "out_of_order",
            "fieldtype": "Int",
            "width": 120
        }
    ]

    return columns


def get_data(filters):
    data = []

    airport_filter = filters.get("airport") if filters else None

    airports = frappe.get_all(
        "Airport", 
        fields=["name"], 
        filters={"name": airport_filter} if airport_filter else None
    )
    
    for airport in airports:

        total_shops = frappe.db.count("Shop", filters={"airport": airport.name})
        
        available_shops = frappe.db.count("Shop", filters={"airport": airport.name, "status": "Available"})
        
        occupied_shops = frappe.db.count("Shop", filters={"airport": airport.name, "status": "Occupied"})

        out_of_order = frappe.db.count("Shop", filters={"airport": airport.name, "status": "Out of Order"})
        
        data.append({
            "airport": airport.name,
            "shop_name": None,
            "status": None,
            "total_shops": total_shops,
            "available_shops": available_shops,
            "occupied_shops": occupied_shops,
            "out_of_order": out_of_order
        })

        # Fetch individual shops
        shops = frappe.get_all(
            "Shop", 
            fields=["name", "status"], 
            filters={"airport": airport.name}
        )

        for shop in shops:
            data.append({
                "airport": None,
                "shop_name": shop.name,
                "status": shop.status,
                "total_shops": None,
                "available_shops": None,
                "occupied_shops": None,
                "out_of_order": None
            })

    return data
