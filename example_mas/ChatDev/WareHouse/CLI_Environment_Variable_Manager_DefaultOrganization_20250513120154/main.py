'''
Main entry point for the CLI environment variable manager application.
'''
import argparse
from env_manager import EnvVarManager
def main():
    parser = argparse.ArgumentParser(description="CLI Environment Variable Manager")
    parser.add_argument('-l', '--list', action='store_true', help='List all environment variables')
    parser.add_argument('-s', '--set', nargs=2, metavar=('NAME', 'VALUE'), help='Set an environment variable')
    parser.add_argument('-u', '--unset', metavar='NAME', help='Unset an environment variable')
    parser.add_argument('-p', '--persistent', action='store_true', help='Make the change persistent')
    args = parser.parse_args()
    env_manager = EnvVarManager()
    if args.list:
        for name, value in env_manager.list_vars():
            print(f"{name}={value}")
    elif args.set:
        name, value = args.set
        env_manager.set_var(name, value, args.persistent)
        print(f"Variable '{name}' set successfully.")
    elif args.unset:
        env_manager.unset_var(args.unset, args.persistent)
        print(f"Variable '{args.unset}' unset successfully.")
    else:
        parser.print_help()
if __name__ == "__main__":
    main()