'''
Module to find processes by their name.
'''
import psutil
import logging
class ProcessFinder:
    def find_processes(self, name):
        """Finds processes matching the given name."""
        logging.info(f"Finding processes with name: {name}")
        matching_processes = []
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                if name.lower() in proc.info['name'].lower():
                    matching_processes.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                logging.warning(f"Process {proc.info['pid']} could not be accessed or is no longer running.")
        return matching_processes