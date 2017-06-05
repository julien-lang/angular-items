#! /usr/bin/python

import cherrypy

from app.APIService import APIService

def main():
	print("testettete")
	cherrypy.server.max_request_body_size = 0
	cherrypy.server.socket_timeout = 60
	cherrypy.server.socket_host = "0.0.0.0"
	
	cherrypy.config.update({
		'tools.encode.on': True,
		'tools.encode.encoding': 'utf-8'
	})
	
	cherrypy.quickstart(APIService(cherrypy.engine))


if __name__ == "__main__":
	main()
