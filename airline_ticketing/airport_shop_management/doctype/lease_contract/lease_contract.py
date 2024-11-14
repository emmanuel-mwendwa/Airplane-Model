# Copyright (c) 2024, Mwendwa and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class LeaseContract(Document):
	def validate(self):

		self.rent_amount = self.set_rent_amount()

	def set_rent_amount(self):

		default_rent_amount = frappe.db.get_single_value("Shop Management Settings", "rent_amount")

		if default_rent_amount == 0:

			frappe.throw("Set the default rent amount in Shop Management Settings")

		return default_rent_amount


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
			message = f"Dear {lease_doc.tenant_email}, your rent is due for Shop {lease_doc.shop_name}"
			frappe.sendmail(recipients=[tenant_email], subject=subject, message=message)