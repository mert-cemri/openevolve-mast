'''
This is the main entry point for the CLI environment variable manager application.
'''
import argparse
from env_manager import EnvironmentManager
def main():
    parser = argparse.ArgumentParser(description="CLI Environment Variable Manager")
    parser.add_argument('action', choices=['list', 'set', 'unset'], help="Action to perform")
    parser.add_argument('--name', help="Name of the environment variable")
    parser.add_argument('--value', help="Value of the environment variable (required for 'set')")
    parser.add_argument('--persistent', action='store_true', help="Make the change persistent")
    args = parser.parse_args()
    env_manager = EnvironmentManager()
    if args.action == 'list':
        env_vars = env_manager.list_env_vars()
        for key, value in env_vars.items():
            print(f"{key}={value}")
    elif args.action == 'set':
        if not args.name or not args.value:
            print("Error: 'set' action requires both --name and --value arguments.")
            return
        env_manager.set_env_var(args.name, args.value, args.persistent)
        print(f"Environment variable '{args.name}' set successfully.")
    elif args.action == 'unset':
        if not args.name:
            print("Error: 'unset' action requires --name argument.")
            return
        env_manager.unset_env_var(args.name, args.persistent)
        print(f"Environment variable '{args.name}' unset successfully.")
if __name__ == "__main__":
    main()