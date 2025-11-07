'''
Handles the listing and killing of processes.
'''
import os
import signal
import psutil
class ProcessManager:
    def list_processes(self, name):
        processes = []
        for proc in psutil.process_iter(['pid', 'name']):
            if name.lower() in proc.info['name'].lower():
                processes.append((proc.info['pid'], proc.info['name']))
        return processes
    def kill_process(self, pid):
        try:
            if self.confirm_kill(pid):
                os.kill(pid, signal.SIGTERM)
                print(f"Process {pid} killed.")
                return True
            else:
                print(f"Process {pid} not killed.")
                return False
        except psutil.NoSuchProcess:
            print(f"Process {pid} does not exist.")
            return False
        except OSError as e:
            print(f"Error killing process {pid}: {e}")
            return False
    def confirm_kill(self, pid):
        confirmation = input(f"Are you sure you want to kill process {pid}? (y/n): ")
        return confirmation.lower() == 'y'