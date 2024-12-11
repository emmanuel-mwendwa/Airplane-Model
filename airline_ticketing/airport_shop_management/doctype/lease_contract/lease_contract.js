// Copyright (c) 2024, Mwendwa and contributors
// For license information, please see license.txt

frappe.ui.form.on("Lease Contract", {
	refresh(frm) {
        frm.set_query(
            "shop",
            function() {
                return {
                    filters: {
                        airport: frm.doc.airport,
                        status: "Available"
                    }
                };
            }
        )
	},

    start_date(frm) {
        validate_lease_duration(frm);
    },

    end_date(frm) {
        validate_lease_duration(frm);
    }
});

function validate_lease_duration(frm) {
    if (frm.doc.start_date && frm.doc.end_date) {
        const start_date = frappe.datetime.str_to_obj(frm.doc.start_date);
        const end_date = frappe.datetime.str_to_obj(frm.doc.end_date);

        if (start_date >= end_date) {
            frappe.msgprint(__("Lease Start Date must be before Lease End Date"));
            frm.set_value("end_date", null);
            return;
        }

        const difference_in_days = frappe.datetime.get_day_diff(end_date, start_date);
        if (difference_in_days < 30) {
            frappe.msgprint(__("The lease duration must be at least one month"));
            frm.set_value("end_date", null);
        }
    }
}