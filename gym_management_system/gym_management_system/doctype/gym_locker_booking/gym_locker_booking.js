// Copyright (c) 2023, Scenarios and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Locker Booking', {
	refresh: function (frm) {
		frappe.call({
				method: "gym_management_system.gym_management_system.doctype.gym_locker_booking.gym_locker_booking.user_name"
			})
			.then((r) => {

				if (frappe.session.user != 'Administrator' && r.message != "Error") {
					cur_frm.set_df_property("assigned_to", "read_only", 1);
					frm.set_value('assigned_to', r.message);
				} else {
					cur_frm.set_df_property("assigned_to", "read_only", 1);
					frappe.throw("You have already booked locker")
				}

			})

	}
});