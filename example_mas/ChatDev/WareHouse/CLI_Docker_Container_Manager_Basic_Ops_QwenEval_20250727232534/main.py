'''
Main entry point for the Docker Container Manager application.
Handles command-line arguments and invokes DockerManager methods.
'''
import sys
from docker_manager import DockerManager
def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <command> [args]")
        print("Commands: list, start, stop, logs")
        sys.exit(1)
    docker_manager = DockerManager()
    command = sys.argv[1]
    if command == "list":
        all_containers = False
        if len(sys.argv) > 2 and sys.argv[2] == "--all":
            all_containers = True
        print(docker_manager.list_containers(all_containers))
    elif command == "start":
        if len(sys.argv) < 3:
            print("Usage: python main.py start <container_id_or_name>")
            sys.exit(1)
        print(docker_manager.start_container(sys.argv[2]))
    elif command == "stop":
        if len(sys.argv) < 3:
            print("Usage: python main.py stop <container_id_or_name>")
            sys.exit(1)
        print(docker_manager.stop_container(sys.argv[2]))
    elif command == "logs":
        if len(sys.argv) < 3:
            print("Usage: python main.py logs <container_id_or_name>")
            sys.exit(1)
        print(docker_manager.view_logs(sys.argv[2]))
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
if __name__ == "__main__":
    main()