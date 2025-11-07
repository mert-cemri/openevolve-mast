'''
Module containing the logic for the HTTP server.
'''
import http.server
import socketserver
import threading
class SimpleHTTPServer:
    '''
    Class to handle the HTTP server operations.
    '''
    def __init__(self, directory, port):
        '''
        Initializes the server with the specified directory and port.
        '''
        self.directory = directory
        self.port = port
        self.httpd = None
    def start_server(self):
        '''
        Starts the HTTP server in a separate thread.
        '''
        handler = http.server.SimpleHTTPRequestHandler
        handler.directory = self.directory
        self.httpd = socketserver.TCPServer(("", self.port), handler)
        print(f"Serving at port {self.port}")
        # Run the server in a separate thread
        server_thread = threading.Thread(target=self.httpd.serve_forever)
        server_thread.daemon = True  # Ensure the thread exits when the main program exits
        server_thread.start()
    def stop_server(self):
        '''
        Stops the HTTP server.
        '''
        if self.httpd:
            self.httpd.shutdown()
            self.httpd.server_close()
            print("Server stopped")