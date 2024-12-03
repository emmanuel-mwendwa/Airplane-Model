// Copyright (c) 2024, Mwendwa and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Flight", {
	refresh(frm) {
        
	},

    gate_number(frm) {
        if (frm.doc.gate_number) {
            frappe.call({
                method: "update_ticket_gate_numbers",
                doc: frm.doc,
                args: {},
                callback: function(r) {
                    refresh_field("gate_number");
                }
            })
        }
    }
});
