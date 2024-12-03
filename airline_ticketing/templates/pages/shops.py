import frappe

def get_context(context):
    context.shops = frappe.get_all("Shop", filters={"status": "Available"}, fields=["airport", "number", "name", "area", "status"])
