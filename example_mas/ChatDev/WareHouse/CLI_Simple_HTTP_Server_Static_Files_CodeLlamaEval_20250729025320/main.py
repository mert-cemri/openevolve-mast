#!/usr/bin/env python3
'''
A simple HTTP request handler that serves static files (HTML, CSS, JS, images) from a specified local directory.
'''
import os
import sys
import argparse
from http.server import HTTPServer, SimpleHTTPRequestHandler
class SimpleHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()
def main():
    parser = argparse.ArgumentParser(description='A simple HTTP server')
    parser.add_argument('-p', '--port', type=int, default=8000, help='port to listen on')
    parser.add_argument('-d', '--directory', default='.', help='directory to serve files from')
    args = parser.parse_args()
    os.chdir(args.directory)
    server = HTTPServer(('', args.port), SimpleHTTPRequestHandler)
    print(f'Serving files from {args.directory} on port {args.port}...')
    server.serve_forever()
if __name__ == '__main__':
    main()