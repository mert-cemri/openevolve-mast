'''
Utility functions for the CLI network ping tool.
'''
import subprocess
import platform
import logging
# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
def run_ping_command(address, count):
    try:
        # Determine the platform-specific ping command
        if platform.system().lower() == "windows":
            command = ["ping", "-n", str(count), address]
        else:
            command = ["ping", "-c", str(count), address]
        # Execute the ping command
        output = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True  # This will raise CalledProcessError if the command fails
        )
        return output.stdout
    except subprocess.CalledProcessError as e:
        logging.error(f"Ping command failed with error: {e}")
        return f"Ping command failed. Please check the address and try again."
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return f"An unexpected error occurred: {e}"