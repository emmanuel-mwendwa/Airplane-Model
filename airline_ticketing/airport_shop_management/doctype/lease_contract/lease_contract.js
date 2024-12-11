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
});
