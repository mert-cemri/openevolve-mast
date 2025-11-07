'''
Main file for CLI utility
'''
import argparse
import sys
from firewall import Firewall
def main():
    parser = argparse.ArgumentParser(description='CLI utility for adding basic firewall rules using iptables')
    parser.add_argument('-p', '--port', help='Port to allow or block')
    parser.add_argument('-a', '--action', help='Action to perform (allow or block)')
    parser.add_argument('-s', '--source', help='Source IP address')
    parser.add_argument('-d', '--destination', help='Destination IP address')
    parser.add_argument('-n', '--protocol', help='Protocol (TCP or UDP)')
    args = parser.parse_args()
    if not args.port or not args.action or not args.source or not args.destination or not args.protocol:
        print("Error: Please provide all the necessary arguments")
        sys.exit(1)
    firewall = Firewall()
    firewall.add_rule(args.port, args.action, args.source, args.destination, args.protocol)
    firewall.apply_rules()
if __name__ == '__main__':
    main()