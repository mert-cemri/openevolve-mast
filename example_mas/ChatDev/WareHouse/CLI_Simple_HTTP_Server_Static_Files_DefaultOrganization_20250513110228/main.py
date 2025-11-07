'''
Main entry point for the CLI HTTP server application.
'''
import argparse
from server import StaticFileServer
def main():
    parser = argparse.ArgumentParser(description='Simple CLI HTTP Server')
    parser.add_argument('directory', type=str, help='Directory to serve files from')
    parser.add_argument('port', type=int, help='Port number to listen on')
    args = parser.parse_args()
    server = StaticFileServer(args.directory, args.port)
    server.start()
if __name__ == "__main__":
    main()