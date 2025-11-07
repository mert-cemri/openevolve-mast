'''
Main entry point for the Docker CLI Manager application.
'''
import argparse
from docker_manager import DockerManager
def list_containers(manager, all_containers):
    containers = manager.list_containers(all_containers)
    for container in containers:
        print(f"{container.id[:12]}: {container.name} (Status: {container.status})")
def start_container(manager, container_id_or_name):
    try:
        manager.start_container(container_id_or_name)
        print("Container started")
    except Exception as e:
        print(f"Error: {str(e)}")
def stop_container(manager, container_id_or_name):
    try:
        manager.stop_container(container_id_or_name)
        print("Container stopped")
    except Exception as e:
        print(f"Error: {str(e)}")
def view_logs(manager, container_id_or_name):
    try:
        logs = manager.view_logs(container_id_or_name)
        print(logs)
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Docker CLI Manager")
    parser.add_argument("command", choices=["list", "start", "stop", "logs"], help="Command to execute")
    parser.add_argument("--all", action="store_true", help="List all containers")
    parser.add_argument("container", nargs="?", help="Container ID or name")
    args = parser.parse_args()
    manager = DockerManager()
    if args.command == "list":
        list_containers(manager, args.all)
    elif args.command == "start":
        if args.container:
            start_container(manager, args.container)
        else:
            print("Error: Container ID or name required for start command")
    elif args.command == "stop":
        if args.container:
            stop_container(manager, args.container)
        else:
            print("Error: Container ID or name required for stop command")
    elif args.command == "logs":
        if args.container:
            view_logs(manager, args.container)
        else:
            print("Error: Container ID or name required for logs command")