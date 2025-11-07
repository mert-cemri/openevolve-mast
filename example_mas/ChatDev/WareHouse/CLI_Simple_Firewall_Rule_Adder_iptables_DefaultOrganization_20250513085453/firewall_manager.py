'''
Handles interaction with iptables for managing firewall rules.
'''
import subprocess
class FirewallManager:
    def allow_port(self, port):
        command = f"sudo iptables -A INPUT -p tcp --dport {port} -j ACCEPT"
        return self.run_command(command)
    def block_port(self, port):
        command = f"sudo iptables -A INPUT -p tcp --dport {port} -j DROP"
        return self.run_command(command)
    def remove_rule(self, port, action):
        if action == "allow":
            command = f"sudo iptables -D INPUT -p tcp --dport {port} -j ACCEPT"
        elif action == "block":
            command = f"sudo iptables -D INPUT -p tcp --dport {port} -j DROP"
        else:
            raise ValueError("Invalid action specified.")
        return self.run_command(command)
    def run_command(self, command):
        try:
            subprocess.run(command, shell=True, check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")
            return False