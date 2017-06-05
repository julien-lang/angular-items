# -*- coding: utf-8 -*-

import cherrypy
import random

class APIService:
	def __init__(self, manager_):
		self.fake_data = {
			"f1e1": {
				"id": "f1e1",
				"name": "Item 1",
				"url": "http://my-test.com/1",
				"type": "Type-1",
				"status": "OK",
				"include": False,
			},
			"f1e2": {
				"id": "f1e2",
				"name": "Item 2",
				"url": "http://my-test.com/2",
				"type": "Type-1",
				"status": "Error",
				"include": False,
			},
			"f1e3": {
				"id": "f1e3",
				"name": "Item 445",
				"url": "http://my-test.com/2",
				"type": "Type-1",
				"status": "Processing",
				"include": False,
			},
			"f1e4": {
				"id": "f1e4",
				"name": "Super Item",
				"url": "http://my-test.com/2",
				"type": "Type-1",
				"status": "Offline",
				"include": False,
			},
			"f1e5": {
				"id": "f1e5",
				"name": "item-10045",
				"url": "http://my-test.com/2",
				"type": "Type-2",
				"status": "OK",
				"include": False,
			},
		}
	
	@cherrypy.expose
	@cherrypy.tools.json_out()
	@cherrypy.tools.json_in()
	def new(self):
		input_json = cherrypy.request.json
		
		if type(input_json) is not dict:
			raise cherrypy.HTTPError(400, "Invalid incoming format")
		
		if "name" not in input_json:
			raise cherrypy.HTTPError(400, "Missing name argument")
		
		if "type" not in input_json:
			raise cherrypy.HTTPError(400, "Missing type argument")
		
		if "url" not in input_json:
			input_json["url"] = "http://my-test/default"
		
		item_id = "item_%04d" % random.randint(1, 9999)
		while item_id in self.fake_data:
			item_id = "item_%04d" % random.randint(1, 9999)
		
		self.fake_data[item_id] = input_json
		self.fake_data[item_id]["id"] = item_id
		self.fake_data[item_id]["status"] = "Processing"
		return self.fake_data[item_id]
	
	
	@cherrypy.expose
	@cherrypy.tools.json_out()
	def list(self):
		return self.fake_data
	
	
	@cherrypy.expose
	@cherrypy.tools.json_out()
	def info(self, item_id):
		if item_id not in self.fake_data:
			raise cherrypy.HTTPError(404, "Unknown item "+item_id)
		
		return self.fake_data[item_id]
	
	
	@cherrypy.expose
	@cherrypy.tools.json_out()
	def delete(self, item_id):
		if item_id not in self.fake_data:
			raise cherrypy.HTTPError(404, "Unknown item "+item_id)
		
		info = self.fake_data[item_id]
		del(self.fake_data[item_id])
		
		info["status"] = "deleted"
		return info
