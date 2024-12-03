# Copyright (c) 2024, Mwendwa and contributors
# For license information, please see license.txt

import frappe
import random
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(WebsiteGenerator):

    def validate(self):

        self.gate_number = self.random_gate_number() if not self.gate_number else self.gate_number

    def on_submit(self):

        self.status = "Completed"

    def random_gate_number(self):

        terminal_num = random.randint(1, 5)

        terminal_letter = random.choice(["A", "B", "C"])

        gate_num = random.randint(1, 5)

        return f"{terminal_num}{terminal_letter}{gate_num}"
    
    @frappe.whitelist()
    def update_ticket_gate_numbers(self):

        tickets = frappe.get_all("Airplane Ticket", filters={"flight": self.name}, fields=["name", "gate_number"])

        for ticket in tickets:
            frappe.db.set_value("Airplane Ticket", ticket["name"], "gate_number", self.gate_number)