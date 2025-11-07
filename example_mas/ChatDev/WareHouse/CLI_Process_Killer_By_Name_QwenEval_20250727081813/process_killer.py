'''
Module to kill processes by their PID.
'''
import psutil
import logging
import signal
class ProcessKiller:
    def kill_process(self, pid):
        """Kills the process with the given PID. If the process does not terminate within 3 seconds, it is forcefully killed."""
        logging.info(f"Attempting to kill process with PID: {pid}")
        try:
            proc = psutil.Process(pid)
            proc.terminate()
            try:
                proc.wait(timeout=3)
            except psutil.TimeoutExpired:
                logging.warning(f"Process {pid} did not terminate within 3 seconds. Forcibly killing it.")
                proc.kill()
                proc.wait(timeout=3)
            logging.info(f"Process {pid} killed successfully.")
            return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            logging.warning(f"Failed to kill process {pid}.")
            return False