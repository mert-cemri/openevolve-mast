'''
This module contains the implementation of a CLI tool that displays the system uptime.
The system uptime is fetched using the `uptime` command.
'''
import subprocess
def get_uptime():
    '''
    Execute the system command to get the uptime.
    Returns:
    - A string representing the system uptime.
    '''
    try:
        # Execute the uptime command and capture the output
        result = subprocess.run(['uptime', '-p'], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: Command failed with exit code {e.returncode}"
    except FileNotFoundError:
        return "Error: `uptime` command not found. Please ensure it is installed on your system."
    except Exception as e:
        return f"Error: {e}"
def main():
    '''
    The entry point of the application to display the system uptime.
    '''
    uptime = get_uptime()
    print(f"System Uptime: {uptime}")
if __name__ == "__main__":
    main()