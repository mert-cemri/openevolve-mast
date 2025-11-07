'''
Handles process-related operations such as listing and killing processes.
'''
import psutil
class ProcessManager:
    def list_processes_by_name(self, name):
        '''
        Lists all processes whose names contain the given name.
        '''
        processes = []
        for proc in psutil.process_iter(['pid', 'name']):
            if name.lower() in proc.info['name'].lower():
                processes.append(proc.info)
        return processes
    def kill_process(self, pid):
        '''
        Kills the process with the given process ID (PID).
        '''
        try:
            proc = psutil.Process(pid)
            proc.terminate()
            proc.wait(timeout=3)  # Wait for the process to terminate
            return True
        except psutil.NoSuchProcess:
            print(f"Process {pid} does not exist.")
        except psutil.AccessDenied:
            print(f"Access denied to kill process {pid}.")
        except psutil.ZombieProcess:
            print(f"Process {pid} is a zombie process.")
        except Exception as e:
            print(f"Error killing process {pid}: {e}")
        return False