// Copyright (c) 2021, Alex Tas and contributors
// For license information, please see license.txt

frappe.ui.form.on('Order_PS', {

	on_submit(frm) {

        // set a field as unhidden
		//frm.set_df_property('product', 'hidden', 0);
		// set a field as read only
		frm.set_df_property('product', 'read_only', !frm.is_new());


		frappe.msgprint({
		    title: __('Notification'),
		    indicator: 'green',
		    message: __(`Создан документ Станция:  ${frm.doc.product}`)
		});

    }
});
