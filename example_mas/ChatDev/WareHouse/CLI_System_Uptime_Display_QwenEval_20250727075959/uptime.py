'''
Module for retrieving system uptime by executing the `uptime` command.
'''
import subprocess
def get_system_uptime():
    try:
        # Execute the `uptime` command and capture its output
        result = subprocess.run(['uptime', '-p'], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error retrieving uptime: {e}"