// Copyright (c) 2023, Scenarios and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Locker Booking', {
	refresh: function (frm) {
		if (frappe.session.user != 'Administrator'){
			frm.set_df_property("assigned_to", "read_only", 1);
		}
	},
	locker_number: function (frm) {
		frappe.call({
				method: "gym_management_system.gym_management_system.doctype.gym_locker_booking.gym_locker_booking.check_locker_assigned"
			})
			.then((r) => {
				if (frappe.session.user != 'Administrator' && r.message != "Error") {
					frm.set_value('assigned_to', r.message);
				} else if (frappe.session.user != 'Administrator' && r.message == "Error"){
				    frappe.throw("You have already booked locker")
				} else {
					
				}

			})

	},


});