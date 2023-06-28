frappe.call({

    method: "calculate_validity",
    type: "GET"

}).then((response) => {
    console.log(response)
})

