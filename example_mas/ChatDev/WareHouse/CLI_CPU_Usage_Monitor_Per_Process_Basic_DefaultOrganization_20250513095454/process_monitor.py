'''
Process monitoring logic for retrieving CPU usage information.
'''
import psutil
class ProcessMonitor:
    def get_process_info(self):
        '''
        Retrieves a list of tuples containing process ID, name, and CPU usage percentage for all processes.
        '''
        process_info = []
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                proc.cpu_percent(interval=None)  # Initialize reference point
                process_info.append((proc.info['pid'], proc.info['name'], proc.cpu_percent(interval=0.1)))
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return process_info
    def get_process_info_by_pid(self, pid):
        '''
        Retrieves a tuple containing process ID, name, and CPU usage percentage for a specific process identified by PID.
        '''
        try:
            proc = psutil.Process(pid)
            proc.cpu_percent(interval=None)  # Initialize reference point
            return (proc.pid, proc.name(), proc.cpu_percent(interval=0.1))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            return None