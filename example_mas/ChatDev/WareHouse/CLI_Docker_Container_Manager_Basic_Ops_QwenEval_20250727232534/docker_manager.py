'''
Handles all Docker operations such as listing containers, starting/stopping containers, and viewing logs.
Uses subprocess to run Docker commands.
'''
import subprocess
class DockerManager:
    def list_containers(self, all_containers=False):
        '''
        Lists all Docker containers. If all_containers is True, lists all containers including stopped ones.
        Returns the output of the Docker command as a string.
        '''
        if all_containers:
            result = subprocess.run(['docker', 'ps', '-a'], capture_output=True, text=True)
        else:
            result = subprocess.run(['docker', 'ps'], capture_output=True, text=True)
        if result.returncode != 0:
            return f"Error: {result.stderr}"
        return result.stdout
    def start_container(self, container_id_or_name):
        '''
        Starts a Docker container by its ID or name.
        Returns the output of the Docker command as a string.
        '''
        result = subprocess.run(['docker', 'start', container_id_or_name], capture_output=True, text=True)
        if result.returncode != 0:
            return f"Error: {result.stderr}"
        return result.stdout
    def stop_container(self, container_id_or_name):
        '''
        Stops a Docker container by its ID or name.
        Returns the output of the Docker command as a string.
        '''
        result = subprocess.run(['docker', 'stop', container_id_or_name], capture_output=True, text=True)
        if result.returncode != 0:
            return f"Error: {result.stderr}"
        return result.stdout
    def view_logs(self, container_id_or_name):
        '''
        Views the logs of a Docker container by its ID or name.
        Returns the output of the Docker command as a string.
        '''
        result = subprocess.run(['docker', 'logs', container_id_or_name], capture_output=True, text=True)
        if result.returncode != 0:
            return f"Error: {result.stderr}"
        return result.stdout