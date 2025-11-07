import argparse
import uptime
parser = argparse.ArgumentParser(description='Display system uptime')
parser.add_argument('-u', '--uptime', action='store_true', help='Display system uptime')
args = parser.parse_args()
if args.uptime:
    uptime_str = uptime.get_system_uptime()
    print(uptime_str)