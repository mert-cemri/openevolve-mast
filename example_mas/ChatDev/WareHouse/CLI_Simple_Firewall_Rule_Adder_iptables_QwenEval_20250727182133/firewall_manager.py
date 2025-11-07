'''
Handles the interaction with iptables to add, remove, and list rules.
'''
import subprocess
class FirewallManager:
    def add_rule(self, action, protocol, port):
        command = ['sudo', 'iptables', '-A', 'INPUT', '-p', protocol, '--dport', str(port), '-j', action.upper()]
        subprocess.run(command, check=True)
    def remove_rule(self, protocol, port):
        # Save current rules
        save_command = ['sudo', 'iptables-save']
        result = subprocess.run(save_command, capture_output=True, text=True, check=True)
        rules = result.stdout.splitlines()
        # Filter out the rule to be removed
        filtered_rules = []
        for rule in rules:
            if f'-p {protocol} --dport {port}' in rule and ('-j ACCEPT' in rule or '-j DROP' in rule):
                continue
            filtered_rules.append(rule)
        # Restore filtered rules
        restore_command = ['sudo', 'iptables-restore']
        subprocess.run(restore_command, input='\n'.join(filtered_rules), text=True, check=True)
    def list_rules(self):
        command = ['sudo', 'iptables', '-L', 'INPUT', '-v', '-n']
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout