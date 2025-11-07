'''
Main application file for the CLI HTTP server.
'''
import argparse
from server import run_server
def main():
    parser = argparse.ArgumentParser(description='Simple CLI HTTP Server')
    parser.add_argument('directory', type=str, help='The directory to serve files from')
    parser.add_argument('port', type=int, help='The port to listen on')
    args = parser.parse_args()
    try:
        run_server(args.directory, args.port)
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()