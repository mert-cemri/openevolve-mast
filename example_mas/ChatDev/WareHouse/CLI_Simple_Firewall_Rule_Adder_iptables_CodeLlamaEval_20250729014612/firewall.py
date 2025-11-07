'''
Firewall class for adding basic firewall rules using iptables
'''
import subprocess
class Firewall:
    def __init__(self):
        self.rules = []
    def add_rule(self, port, action, source, destination, protocol):
        if action == 'allow':
            self.rules.append(f'iptables -A INPUT -p {protocol} --dport {port} -s {source} -d {destination} -j ACCEPT')
        elif action == 'block':
            self.rules.append(f'iptables -A INPUT -p {protocol} --dport {port} -s {source} -d {destination} -j DROP')
        else:
            raise ValueError(f'Invalid action: {action}')
    def apply_rules(self):
        if not self.rules:
            print("No rules have been added")
            return
        for rule in self.rules:
            subprocess.run(rule, shell=True)