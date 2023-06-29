// Copyright (c) 2023, Scenarios and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Membership Details', {
	gym_member: function (frm) {
		var today = new Date();
		var dd = String(today.getDate()).padStart(2, '0');
		var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
		var yyyy = today.getFullYear();
		today = yyyy + '-' + mm + '-' + dd;
		frm.set_value('activation_date', today)
	},

});