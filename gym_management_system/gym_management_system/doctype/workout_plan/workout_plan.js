// Copyright (c) 2023, Scenarios and contributors
// For license information, please see license.txt

frappe.ui.form.on('Workout Plan', {
	workout_goal: function (frm) {


		frappe.call({
				method: "gym_management_system.gym_management_system.doctype.workout_plan.workout_plan.get_workouts",
				args: {
					state: frm.doc.workout_goal
				},
			})
			.then((r) => {

				frm.doc.workout_plan_exercise = []

				$.each(r.message, function (_i, e) {

					var childTable = frm.add_child("workout_plan_exercise");
					childTable.weekly = e.weekday;
					childTable.workout = e.workout;

				})
				refresh_field("workout_plan_exercise")

			})


	}
});