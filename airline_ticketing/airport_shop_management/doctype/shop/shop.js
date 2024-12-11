// Copyright (c) 2024, Mwendwa and contributors
// For license information, please see license.txt

frappe.ui.form.on("Shop", {
    refresh: function(frm) {
        frm.set_query("type", function() {
            return {
                filters: {
                    enabled: 1
                }
            };
        });
    }
});
