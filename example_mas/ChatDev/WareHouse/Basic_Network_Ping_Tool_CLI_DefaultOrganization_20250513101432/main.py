'''
Main application file for the CLI network ping tool.
'''
import subprocess
import platform
import argparse
import re
def ping(address, count):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, str(count), address]
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        results = parse_ping_output(output)
        display_results(results)
    except subprocess.CalledProcessError as e:
        print(f"Failed to ping {address}. Error: {e.output}")
def parse_ping_output(output):
    '''
    Parses the output of the ping command to extract round-trip times and summary statistics.
    '''
    lines = output.splitlines()
    times = []
    summary = ""
    for line in lines:
        if "time=" in line:
            time_part = line.split("time=")[-1]
            time_value = time_part.split()[0]
            times.append(time_value)
        # Adjust regex based on OS
        if platform.system().lower() == 'windows':
            match = re.search(r'Average = (\d+ms)', line)
        else:
            match = re.search(r'(\d+\.\d+/)', line)
        if match:
            summary = match.group(1)
    return times, summary
def display_results(results):
    '''
    Displays the round-trip times and summary statistics.
    '''
    times, summary = results
    for time in times:
        print(f"Round-trip time: {time}")
    print(f"\nSummary:\n{summary}")
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='CLI network ping tool')
    parser.add_argument('address', type=str, help='IP address or hostname to ping')
    parser.add_argument('count', type=int, help='Number of echo requests to send')
    args = parser.parse_args()
    ping(args.address, args.count)