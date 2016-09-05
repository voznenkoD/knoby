#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep

PORT_NUMBER = 8080

class HttpProcessor(BaseHTTPRequestHandler):
	def do_GET(self):
		try:
			sendReply = False
			if self.path.endswith(".html"):
				mimetype='text/html'
				sendReply = True
			if self.path.endswith(".js"):
				mimetype='application/js'
				sendReply = True
			if sendReply == True:
				#Open the static file requested and send it
				f = open(curdir + sep + self.path) 
				self.send_response(200)
				self.send_header('Content-type',mimetype)
				self.end_headers()
				self.wfile.write(f.read())
				f.close()
			else:
				self.send_response(200)
				self.send_header('Content-type','text/plain')
				self.end_headers()
				# Send the html message
				self.wfile.write("29")
			return
		except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)

	#Handler for the POST requests
	def do_POST(self):
		if self.path=="/post":
			content_len = int(self.headers.getheader('content-length', 0))
			post_body = self.rfile.read(content_len)

			print post_body
			self.send_response(200)
			self.end_headers()
			self.wfile.write("Thanks")
			return			
try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), HttpProcessor)
	print 'Started httpserver on port ' , PORT_NUMBER
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()