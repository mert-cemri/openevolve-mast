'''
Server logic for serving static files using Python's http.server module.
'''
import os
import http.server
import socketserver
class StaticFileHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, directory=None, **kwargs):
        self.directory = directory
        super().__init__(*args, directory=directory, **kwargs)
    def translate_path(self, path):
        # Override to use the specified directory
        path = super().translate_path(path)
        relpath = os.path.relpath(path, os.getcwd())
        return os.path.join(self.directory, relpath)
def run_server(directory, port):
    os.chdir(directory)
    handler = StaticFileHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Serving HTTP on port {port} from directory {directory}")
        httpd.serve_forever()