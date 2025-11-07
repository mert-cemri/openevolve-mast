'''
Main entry point for the Docker CLI Manager application.
'''
import sys
from docker_manager import DockerManager
def main():
    docker_manager = DockerManager()
    if len(sys.argv) < 2:
        print("Usage: main.py <command> [<args>]")
        print("Commands:")
        print("  list [--all]       List running/all containers")
        print("  start <id>         Start a container by ID")
        print("  stop <id>          Stop a container by ID")
        print("  logs <id>          View logs of a container by ID")
        return
    command = sys.argv[1]
    if command == "list":
        all_containers = "--all" in sys.argv
        print(docker_manager.list_containers(all_containers))
    elif command == "start" and len(sys.argv) == 3:
        docker_manager.start_container(sys.argv[2])
    elif command == "stop" and len(sys.argv) == 3:
        docker_manager.stop_container(sys.argv[2])
    elif command == "logs" and len(sys.argv) == 3:
        print(docker_manager.view_logs(sys.argv[2]))
    else:
        print("Invalid command or arguments")
if __name__ == "__main__":
    main()