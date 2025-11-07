'''
Main entry point for the CLI environment variable manager.
'''
import argparse
from environment_manager import EnvironmentManager
def main():
    parser = argparse.ArgumentParser(description="CLI Environment Variable Manager")
    subparsers = parser.add_subparsers(dest="command")
    # List command
    list_parser = subparsers.add_parser("list", help="List all environment variables")
    # Set command
    set_parser = subparsers.add_parser("set", help="Set an environment variable")
    set_parser.add_argument("name", help="Name of the environment variable")
    set_parser.add_argument("value", help="Value of the environment variable")
    set_parser.add_argument("-p", "--persistent", action="store_true", help="Persist the variable in the shell profile")
    # Unset command
    unset_parser = subparsers.add_parser("unset", help="Unset an environment variable")
    unset_parser.add_argument("name", help="Name of the environment variable")
    args = parser.parse_args()
    env_manager = EnvironmentManager()
    if args.command == "list":
        variables = env_manager.list_variables()
        for key, value in variables.items():
            print(f"{key}: {value}")
    elif args.command == "set":
        env_manager.set_variable(args.name, args.value, persistent=args.persistent)
        print(f"Variable {args.name} set to {args.value}.")
    elif args.command == "unset":
        env_manager.unset_variable(args.name)
        print(f"Variable {args.name} unset.")
if __name__ == "__main__":
    main()