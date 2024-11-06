// Copyright (c) 2024, Mwendwa and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
	refresh(frm) {
        frm.add_custom_button(__("Assign Seat"), function(){
            const dialog = new frappe.ui.Dialog({
                title: __("Select Seat"),
                fields:[
                    {
                        label: 'Seat Number',
                        fieldname: 'seat_number',
                        fieldtype: 'Data'
                    }
                ],
                size: 'small',
                primary_action_label: 'Assign',
                primary_action(values) {
                    frm.set_value('seat', values.seat_number);
                    dialog.hide();
                }
            });

            dialog.show();
        }, __("Actions"));
	},

    validate(frm) {
        if (frm.is_new() && frm.doc.flight) {
            frappe.call({
                method: "airline_ticketing.airline_ticketing.doctype.airplane_ticket.airplane_ticket.check_capacity",
                args: {
                    flight: frm.doc.flight
                },
                async: false,
                callback: function(r) {
                    if (r.message) {
                        frappe.msgprint(__(r.message));
                        frappe.validated = false;
                    }
                }
            });
        }
    }
});
