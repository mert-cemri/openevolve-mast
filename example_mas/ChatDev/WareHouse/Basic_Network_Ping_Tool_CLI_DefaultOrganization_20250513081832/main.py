'''
Main file for the CLI network ping tool.
'''
import argparse
from utils import run_ping_command
def main():
    parser = argparse.ArgumentParser(description='CLI Network Ping Tool')
    parser.add_argument('address', type=str, help='IP Address or Hostname to ping')
    parser.add_argument('count', type=int, help='Number of pings to send')
    args = parser.parse_args()
    results = run_ping_command(args.address, args.count)
    print(results)
if __name__ == "__main__":
    main()