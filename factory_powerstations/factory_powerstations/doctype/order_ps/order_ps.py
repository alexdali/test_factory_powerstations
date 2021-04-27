# -*- coding: utf-8 -*-
# Copyright (c) 2021, Alex Tas and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Order_PS(Document):
	# 
	def on_submit(self):
		### create doc power_station on submit
		doc_power_station = frappe.get_doc({
		    'doctype': 'Power station',
		    'model': 'M1',
		    'order': self.name_order,
		    'planned_ready_date': self.date_ready
		})
		doc_power_station.insert()

		# add comment
		self.add_comment('Comment', 'Создан документ Станция: {0}'.format(doc_power_station.name))

		# link doc to field
		self.product = doc_power_station.name


