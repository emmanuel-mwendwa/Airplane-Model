# Copyright (c) 2024, Mwendwa and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class LeaseContract(Document):
    def validate(self):

        self.rent_amount = self.set_rent_amount()

    def before_save(self):
        
        self.check_if_another_lease_exists()
        
    def before_submit(self):

        frappe.db.set_value("Shop", self.shop, "status", "Occupied")

    def on_cancel(self):

        frappe.db.set_value("Shop", self.shop, "status", "Available")
        self.status = "Cancelled"

    def set_rent_amount(self):

        default_rent_amount = frappe.db.get_single_value("Shop Management Settings", "rent_amount")

        if default_rent_amount == 0:

            frappe.throw("Set the default rent amount in Shop Management Settings")

        return default_rent_amount
    
    def check_if_another_lease_exists(self):

        active_leases = frappe.get_all(
            "Lease Contract", 
            filters={"status": "Active", "shop": self.shop}, 
            fields=["name", "shop"]
        )

        if active_leases:
            frappe.throw(f"Shop {self.shop} is already leased by {active_leases[0].name}")


@frappe.whitelist()
def send_rent_reminders():

    enable_reminders = frappe.db.get_single_value("Shop Management Settings", "enable_rent_reminders")

    if not enable_reminders:
        return

    active_leases = frappe.get_all("Lease Contract", filters={"status": "Active"})

    for active_lease in active_leases:
        lease_doc = frappe.get_doc("Lease Contract", active_lease.name)
        tenant_email = lease_doc.tenant_email

        if tenant_email:
            subject = "Rent Due Reminder"
            message = f"""
                Dear {lease_doc.tenant_email},<br><br>
                Your rent is due for Shop {lease_doc.shop_name}.  <br>
                Please pay {lease_doc.rent_amount} promptly. <br><br>
                Regards,<br>
                Airport Management.
            """
            frappe.sendmail(recipients=[tenant_email], subject=subject, message=message)