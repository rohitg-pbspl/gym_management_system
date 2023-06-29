// Copyright (c) 2023, Scenarios and contributors
// For license information, please see license.txt

frappe.ui.form.on('Trainer Rating', {
	refresh: function (frm) {
		frappe.call({
				method: "gym_management_system.gym_management_system.doctype.trainer_rating.trainer_rating.user_name"
				
			})
			.then((r) => {

				if (frappe.session.user != 'Administrator') {
					cur_frm.set_df_property("gym_member", "hidden", 1);
					frm.set_value('gym_member', r.message);
				}
			})
	},
});



