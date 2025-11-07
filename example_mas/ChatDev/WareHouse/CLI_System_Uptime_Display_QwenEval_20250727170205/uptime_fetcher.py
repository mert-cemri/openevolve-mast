'''
Handles fetching the system uptime using the `uptime` command.
'''
import subprocess
class UptimeFetcher:
    def get_uptime(self):
        '''
        Fetches the system uptime using the `uptime` command.
        Returns the uptime as a string.
        Raises an exception if the command fails.
        '''
        try:
            result = subprocess.run(['uptime', '-p'], capture_output=True, text=True, check=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            return f"Error fetching uptime: {e}"
        except Exception as e:
            return f"An unexpected error occurred: {e}"