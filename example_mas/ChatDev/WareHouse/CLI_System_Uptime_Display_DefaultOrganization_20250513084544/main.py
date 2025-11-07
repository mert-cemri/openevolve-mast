'''
This script provides a CLI tool that displays the system uptime.
'''
import subprocess
def get_uptime():
    '''
    Execute the system command to get the uptime.
    Returns:
    str: The system uptime as a string.
    '''
    try:
        # Execute the uptime command
        result = subprocess.run(['uptime', '-p'], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return f"Error fetching uptime: {e}"
def main():
    '''
    The main function to run the CLI tool.
    '''
    uptime = get_uptime()
    print(f"System Uptime: {uptime}")
if __name__ == "__main__":
    main()