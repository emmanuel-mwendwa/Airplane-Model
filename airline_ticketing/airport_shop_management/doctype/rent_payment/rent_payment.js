// Copyright (c) 2024, Mwendwa and contributors
// For license information, please see license.txt

frappe.ui.form.on("Rent Payment", {
	refresh(frm) {
        frm.set_value("payment_date", frappe.datetime.get_today());
        
        frm.set_query(
            "lease",
            function() {
                return {
                    filters: {
                        airport: frm.doc.airport,
                        status: "Active",
                        docstatus: 1
                    }
                };
            }
        )
	},
});
