# -*- coding: utf-8 -*-

import cgi
import cherrypy
import glob
import json
import os
import tempfile

# def json_handler(*args, **kwargs):
# 	value = cherrypy.serving.request._json_inner_handler(*args, **kwargs)
# 	return json.dumps(value, sort_keys=True, indent=4, separators=(',', ': '))


class CherryPyWebService:
	def __init__(self, manager_):
		self.manager = manager_
		self.workspace = os.curdir
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
	@cherrypy.tools.json_out() # handler=json_handler
	@cherrypy.tools.json_in()
	def new(self):
		input_json = cherrypy.request.json
		
		f = tempfile.NamedTemporaryFile(mode="w", suffix=".json", prefix="item-", dir=self.workspace, delete=False)
		
		filename = os.path.basename(f.name)
		input_json["id"] = filename[len("item-"):-len(".json")]
		
		f.write(json.dumps(input_json, sort_keys=True, indent=4, separators=(',', ': ')))
		f.close()
		
		return input_json
	
	
	@cherrypy.expose
	@cherrypy.tools.json_out() # handler=json_handler
	def list(self):
		return self.fake_data
		
		items = {}
		for filename in glob.glob(os.path.join(self.workspace, "item-*.json")):
			item_id = os.path.basename(filename)[len("item-"):-len(".json")]
			
			with open(filename, "r") as f:
				items[item_id] = json.load(f)
		
		return items
	
	
	@cherrypy.expose
	@cherrypy.tools.json_out() # handler=json_handler
	def info(self, item_id):
		if item_id not in self.fake_data:
			raise cherrypy.HTTPError(404, "Unknown item "+item_id)
		
		return self.fake_data[item_id]
		
		filename = os.path.join(self.workspace, "item-"+item_id+".json")
		with open(filename, "r") as f:
			info = json.load(f)
		
		return info
	
	
	@cherrypy.expose
	@cherrypy.tools.json_out() # handler=json_handler
	def delete(self, item_id):
		if item_id not in self.fake_data:
			raise cherrypy.HTTPError(404, "Unknown item "+item_id)
		
		info = self.fake_data[item_id]
		del(self.fake_data[item_id])
		
		info["status"] = "deleted"
		return info
		
		filename = os.path.join(self.workspace, "item-"+item_id+".json")
		with open(filename, "r") as f:
			info = json.load(f)
		
		os.remove(filename)
		
		return info


class myFieldStorage(cgi.FieldStorage):
	"""Our version uses a named temporary file instead of the default
	non-named file; keeping it visibile (named), allows us to create a
	2nd link after the upload is done, thus avoiding the overhead of
	making a copy to the destination filename."""

	def make_file(self, binary=None):
		return tempfile.NamedTemporaryFile()


def noBodyProcess():
	"""Sets cherrypy.request.process_request_body = False, giving
	us direct control of the file upload destination. By default
	cherrypy loads it to memory, we are directing it to disk."""
	cherrypy.request.process_request_body = False
	
	cherrypy.tools.noBodyProcess = cherrypy.Tool('before_request_body', noBodyProcess)
