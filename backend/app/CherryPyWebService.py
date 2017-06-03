# -*- coding: utf-8 -*-

import cgi
import cherrypy
import glob
import json
import os
import tempfile

def json_handler(*args, **kwargs):
	value = cherrypy.serving.request._json_inner_handler(*args, **kwargs)
	return json.dumps(value, sort_keys=True, indent=4, separators=(',', ': '))


class CherryPyWebService:
	def __init__(self, manager_):
		self.manager = manager_
		self.workspace = os.curdir
	
	
	@cherrypy.expose
	@cherrypy.tools.json_out(handler=json_handler)
	@cherrypy.tools.json_in()
	def new(self):
		input_json = cherrypy.request.json
		print input_json
		
		f = tempfile.NamedTemporaryFile(mode="w", suffix=".json", prefix="item-", dir=self.workspace, delete=False)
		
		filename = os.path.basename(f.name)
		input_json["id"] = filename[len("item-"):-len(".json")]
		
		f.write(json.dumps(input_json, sort_keys=True, indent=4, separators=(',', ': ')))
		f.close()
		
		return input_json
	
	
	@cherrypy.expose
	@cherrypy.tools.json_out(handler=json_handler)
	def list(self):
		items = {}
		for filename in glob.glob(os.path.join(self.workspace, "item-*.json")):
			item_id = os.path.basename(filename)[len("item-"):-len(".json")]
			
			with open(filename, "r") as f:
				items[item_id] = json.load(f)
		
		return items
	
	
	@cherrypy.expose
	@cherrypy.tools.json_out(handler=json_handler)
	def info(self, item_id):
		filename = os.path.join(self.workspace, "item-"+item_id+".json")
		print item_id
		with open(filename, "r") as f:
			info = json.load(f)
		
		return info
	
	
	@cherrypy.expose
	@cherrypy.tools.json_out(handler=json_handler)
	def delete(self, item_id):
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
