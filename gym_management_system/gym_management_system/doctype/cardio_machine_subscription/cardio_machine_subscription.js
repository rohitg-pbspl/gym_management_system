// Copyright (c) 2023, Scenarios and contributors
// For license information, please see license.txt

frappe.ui.form.on('Cardio Machine Subscription', {
	refresh: function (frm) {
		frappe.call({
				method: "gym_management_system.gym_management_system.doctype.cardio_machine_subscription.cardio_machine_subscription.user_name"
				
			})
			.then((r) => {

				if (frappe.session.user != 'Administrator') {
					cur_frm.set_df_property("gym_member", "read_only", 1);
					frm.set_value('gym_member', r.message);
				}
			})
	},
	after_save: function (frm) {
		if (frappe.session.user != 'Administrator'){
		cur_frm.set_df_property("validity", "read_only", 1)
		cur_frm.set_df_property("start_date", "read_only", 1)
	}
	}
});
