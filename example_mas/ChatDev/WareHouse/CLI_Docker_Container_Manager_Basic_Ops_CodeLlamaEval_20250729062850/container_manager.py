import docker
class ContainerManager:
    def __init__(self):
        self.client = docker.from_env()
    def list_containers(self):
        containers = self.client.containers.list()
        for container in containers:
            print(container.id, container.name)
    def start_container(self, container_id):
        container = self.client.containers.get(container_id)
        container.start()
    def stop_container(self, container_id):
        container = self.client.containers.get(container_id)
        container.stop()
    def view_logs(self, container_id):
        container = self.client.containers.get(container_id)
        print(container.logs())