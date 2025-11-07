'''
Module to handle ICMP echo requests and responses
'''
import os
import platform
import subprocess
import re
class PingTool:
    def __init__(self, host, count=4):
        self.host = host
        self.count = count
    def send_ping(self):
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        command = ['ping', param, str(self.count), self.host]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        if error:
            print(f"Error: {error.decode()}")
            return None
        return output.decode()
    def ping_host(self):
        output = self.send_ping()
        if not output:
            return None
        results = []
        # More flexible regex pattern to handle different formats
        for line in output.split('\n'):
            match = re.search(r'time=(\d+(\.\d+)?)\s*(ms|usec)', line)
            if match:
                time_value = float(match.group(1))
                time_unit = match.group(3)
                if time_unit == 'usec':
                    time_value /= 1000  # Convert usec to ms
                results.append(time_value)
        if not results:
            print("No valid ping responses received.")
            return None
        return results