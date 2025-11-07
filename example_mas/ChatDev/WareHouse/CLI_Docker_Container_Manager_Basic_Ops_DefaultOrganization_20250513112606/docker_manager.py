'''
Handles Docker operations such as listing, starting, stopping containers, and viewing logs.
'''
import subprocess
class DockerManager:
    def list_containers(self, all_containers=False):
        command = ["docker", "ps"]
        if all_containers:
            command.append("-a")
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Error listing containers: {e}"
    def start_container(self, container_id):
        command = ["docker", "start", container_id]
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error starting container {container_id}: {e}")
    def stop_container(self, container_id):
        command = ["docker", "stop", container_id]
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error stopping container {container_id}: {e}")
    def view_logs(self, container_id):
        command = ["docker", "logs", container_id]
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Error viewing logs for container {container_id}: {e}"