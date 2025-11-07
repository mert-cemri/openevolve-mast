'''
Main entry point for the CLI tool that displays system uptime.
'''
import uptime
def display_uptime():
    system_uptime = uptime.get_system_uptime()
    print(system_uptime)
def main():
    display_uptime()
if __name__ == '__main__':
    main()