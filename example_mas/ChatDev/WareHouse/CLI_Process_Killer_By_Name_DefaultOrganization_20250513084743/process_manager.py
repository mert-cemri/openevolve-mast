'''
This module provides functionalities to find and kill processes by their name using the psutil library.
'''
import psutil
class ProcessManager:
    def find_processes_by_name(self, name):
        '''
        Finds and returns a list of processes matching the given name.
        :param name: The name of the process to search for.
        :return: A list of matching processes.
        '''
        matching_processes = []
        for proc in psutil.process_iter(['pid', 'name']):
            if name.lower() in proc.info['name'].lower():
                matching_processes.append(proc)
        return matching_processes
    def kill_process(self, pid):
        '''
        Kills the process with the specified PID.
        :param pid: The PID of the process to kill.
        :return: None
        '''
        try:
            proc = psutil.Process(pid)
            proc.terminate()
            proc.wait(timeout=3)
            return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.TimeoutExpired):
            return False