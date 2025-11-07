'''
Defines the StaticFileServer class to serve static files over HTTP.
'''
import http.server
import socketserver
import os
class StaticFileServer:
    def __init__(self, directory, port):
        '''
        Initializes the server with the specified directory and port.
        '''
        self.directory = directory
        self.port = port
    def start(self):
        '''
        Starts the HTTP server.
        '''
        os.chdir(self.directory)  # Change the current working directory to the specified directory
        handler = http.server.SimpleHTTPRequestHandler
        with socketserver.TCPServer(("", self.port), handler) as httpd:
            print(f"Serving HTTP on port {self.port} (http://localhost:{self.port}/) from {self.directory}")
            httpd.serve_forever()