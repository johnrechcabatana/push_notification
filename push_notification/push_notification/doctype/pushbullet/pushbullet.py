# Copyright (c) 2023, cabatana.johnrech.g@gmail.com and contributors
# For license information, please see license.txt

import frappe
import re
from pushbullet import Pushbullet  
from frappe.model.document import Document

class PushBullet(Document):
	pass

def push_notify(self, method):
	token = frappe.db.get_single_value('PushBullet', 'accesstoken')
	hostname = frappe.db.get_single_value('PushBullet', 'hostname')
	enable_pushbullet = frappe.db.get_single_value('PushBullet', 'enable')
	document = frappe.db.get_single_value('PushBullet', 'document')
	access_token = token
	pb = Pushbullet(access_token)
	if enable_pushbullet == 1:
		doctype=self.doctype
		name = self.name
		docstatus = self.docstatus
		user = frappe.session.user
		message = ''
		if doctype in document:
			if docstatus == 0:
				message = "Saved"
			elif docstatus == 1:
				message = "Submitted"
			elif docstatus == 2:
				message = "Cancelled"
		
			notify_msg = "{0} has been {1} by {2}".format(name,message,user)
			push = pb.push_note(notify_msg, hostname+"/app/"+doctype.replace(" ", "-").lower()+"/"+name)