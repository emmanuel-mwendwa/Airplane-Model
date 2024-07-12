# Copyright (c) 2024, Mwendwa and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class AirplaneTicket(Document):
	
    def validate(self):

        self.total_amount = self.flight_price

        if self.add_ons:
            for add_on in self.add_ons:
                self.total_amount += add_on.amount

        self.total_amount = round(self.total_amount, 2)

        
