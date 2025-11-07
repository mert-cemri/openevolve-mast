'''
DockerManager class to interact with Docker using the Docker SDK.
'''
import docker
class DockerManager:
    def __init__(self):
        self.client = docker.from_env()
    def list_containers(self, all_containers=False):
        '''
        List all or running containers.
        '''
        return self.client.containers.list(all=all_containers)
    def start_container(self, container_id_or_name):
        '''
        Start a container by ID or name.
        '''
        container = self.client.containers.get(container_id_or_name)
        container.start()
    def stop_container(self, container_id_or_name):
        '''
        Stop a container by ID or name.
        '''
        container = self.client.containers.get(container_id_or_name)
        container.stop()
    def view_logs(self, container_id_or_name):
        '''
        View logs of a container by ID or name.
        '''
        container = self.client.containers.get(container_id_or_name)
        return container.logs().decode('utf-8')