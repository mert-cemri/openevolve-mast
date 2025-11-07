'''
Main entry point for the CLI HTTP server application.
Handles command-line arguments and starts the server.
'''
import sys
import argparse
from server import SimpleHTTPServer
from gui import ServerGUI
def main():
    '''
    Parses command-line arguments and starts the HTTP server.
    '''
    parser = argparse.ArgumentParser(description='Simple CLI HTTP Server')
    parser.add_argument('--port', type=int, default=8000, help='Port to listen on (default: 8000)')
    parser.add_argument('--directory', type=str, default='.', help='Directory to serve files from (default: current directory)')
    parser.add_argument('--gui', action='store_true', help='Start the graphical user interface')
    args = parser.parse_args()
    server = SimpleHTTPServer(args.directory, args.port)
    if args.gui:
        gui = ServerGUI(server)
        gui.run()
    else:
        server.start_server()
        print(f"Serving at port {args.port}")
if __name__ == '__main__':
    main()