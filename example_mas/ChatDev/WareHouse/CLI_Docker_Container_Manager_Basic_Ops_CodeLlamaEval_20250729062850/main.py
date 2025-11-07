import argparse
import sys
from container_manager import ContainerManager
def main():
    parser = argparse.ArgumentParser(description='CLI Docker container manager')
    parser.add_argument('--list', action='store_true', help='List running/all containers')
    parser.add_argument('--start', metavar='CONTAINER_ID', help='Start container by ID')
    parser.add_argument('--stop', metavar='CONTAINER_ID', help='Stop container by ID')
    parser.add_argument('--logs', metavar='CONTAINER_ID', help='View logs of container')
    args = parser.parse_args()
    try:
        if args.list:
            ContainerManager.list_containers()
        elif args.start:
            ContainerManager.start_container(args.start)
        elif args.stop:
            ContainerManager.stop_container(args.stop)
        elif args.logs:
            ContainerManager.view_logs(args.logs)
        else:
            parser.print_help()
    except docker.errors.NotFoundError as e:
        print(f"Container {args.start} not found")
if __name__ == '__main__':
    main()