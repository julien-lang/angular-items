#! /usr/bin/python

import cherrypy

from app.CherryPyWebService import CherryPyWebService

def main():
	cherrypy.server.max_request_body_size = 0
	cherrypy.server.socket_timeout = 60
	cherrypy.server.socket_host = "0.0.0.0"
	
	cherrypy.quickstart(CherryPyWebService(cherrypy.engine))


if __name__ == "__main__":
	main()
