#!/usr/bin/env python3
import argparse
import sys
from display_info import display_os_version, display_kernel_version, display_cpu_model, display_total_ram
def main():
    parser = argparse.ArgumentParser(description='Display basic system information on Linux.')
    parser.add_argument('-v', '--version', action='store_true', help='display OS version')
    parser.add_argument('-k', '--kernel', action='store_true', help='display kernel version')
    parser.add_argument('-c', '--cpu', action='store_true', help='display CPU model')
    parser.add_argument('-r', '--ram', action='store_true', help='display total RAM')
    args = parser.parse_args()
    if args.version:
        display_os_version()
    elif args.kernel:
        display_kernel_version()
    elif args.cpu:
        display_cpu_model()
    elif args.ram:
        display_total_ram()
    else:
        parser.print_help()
if __name__ == '__main__':
    main()