# Copyright (c) 2024, Mwendwa and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

import random

class AirplaneTicket(Document):
    
    def validate(self):

        self.remove_duplicate_add_ons()
        self.calculate_total_amount()

        
    def calculate_total_amount(self):

        self.total_amount = self.flight_price

        if self.add_ons:
            for add_on in self.add_ons:
                self.total_amount += add_on.amount

        self.total_amount = round(self.total_amount, 2)

    def remove_duplicate_add_ons(self):

        seen_add_ons = set()
        unique_add_ons = []

        for add_on in self.add_ons:

            if add_on.item not in seen_add_ons:
                seen_add_ons.add(add_on.item)
                unique_add_ons.append(add_on)

            else:
                frappe.msgprint(
                    _("Duplicate add-on of type {0} removed.").format(add_on.item),
                    alert=True
                )
        self.add_ons = unique_add_ons

    def random_seat(self):

        seat_num = random.randint(1, 100)

        seat_letter = random.choice(["A", "B", "C", "D", "E"])

        return f"{seat_num}{seat_letter}"

    def before_submit(self):

        self.seat = self.random_seat()

        if self.status != "Boarded":

            frappe.throw(_("Ticket must be in Boarded status to be submitted."))