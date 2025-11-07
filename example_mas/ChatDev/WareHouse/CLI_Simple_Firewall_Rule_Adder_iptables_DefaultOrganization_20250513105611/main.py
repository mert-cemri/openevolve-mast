'''
Main application file for the Firewall Manager CLI utility.
'''
import argparse
import subprocess
def add_rule(port):
    '''
    Add a firewall rule to allow traffic on the specified port.
    '''
    if port.isdigit():
        command = ["sudo", "iptables", "-A", "INPUT", "-p", "tcp", "--dport", port, "-j", "ACCEPT"]
        try:
            execute_iptables_command(command)
            print(f"Success: Rule added for port {port}.")
        except Exception as e:
            print(f"Error: Failed to add rule for port {port}:\n{str(e)}")
    else:
        print("Error: Please enter a valid port number.")
def remove_rule(port):
    '''
    Remove a firewall rule to block traffic on the specified port.
    '''
    if port.isdigit():
        command = ["sudo", "iptables", "-D", "INPUT", "-p", "tcp", "--dport", port, "-j", "ACCEPT"]
        try:
            execute_iptables_command(command)
            print(f"Success: Rule removed for port {port}.")
        except Exception as e:
            print(f"Error: Failed to remove rule for port {port}:\n{str(e)}")
    else:
        print("Error: Please enter a valid port number.")
def execute_iptables_command(command):
    '''
    Execute the iptables command with sudo privileges.
    '''
    try:
        output = run_command(command)
        print(f"Success: Command executed:\n{output}")
    except subprocess.CalledProcessError as e:
        print(f"Error: Command failed with error:\n{e.stderr}")
    except Exception as e:
        print(f"Error: Failed to execute command:\n{str(e)}")
def run_command(command):
    '''
    Run a shell command and return the output.
    '''
    result = subprocess.run(command, text=True, capture_output=True, check=True)
    return result.stdout
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Firewall Manager CLI Utility')
    parser.add_argument('action', choices=['allow', 'block'], help='Action to perform: allow or block a port')
    parser.add_argument('port', help='Port number to allow or block')
    args = parser.parse_args()
    if args.action == 'allow':
        add_rule(args.port)
    elif args.action == 'block':
        remove_rule(args.port)