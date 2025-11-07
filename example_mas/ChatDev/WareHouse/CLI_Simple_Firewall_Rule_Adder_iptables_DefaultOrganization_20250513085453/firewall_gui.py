'''
Creates and manages the GUI for the Firewall Manager application.
'''
from tkinter import Label, Entry, Button, Tk
from firewall_manager import FirewallManager
class FirewallGUI:
    def __init__(self, root):
        self.manager = FirewallManager()
        self.port_label = Label(root, text="Port:")
        self.port_label.grid(row=0, column=0)
        self.port_entry = Entry(root)
        self.port_entry.grid(row=0, column=1)
        self.allow_button = Button(root, text="Allow", command=lambda: self.add_rule("allow"))
        self.allow_button.grid(row=1, column=0)
        self.block_button = Button(root, text="Block", command=lambda: self.add_rule("block"))
        self.block_button.grid(row=1, column=1)
        self.remove_button = Button(root, text="Remove", command=self.remove_rule)
        self.remove_button.grid(row=2, column=0, columnspan=2)
    def add_rule(self, action):
        port = self.port_entry.get()
        if action == "allow":
            success = self.manager.allow_port(port)
        else:
            success = self.manager.block_port(port)
        if success:
            print(f"Successfully added rule to {action} port {port}.")
        else:
            print(f"Failed to add rule to {action} port {port}.")
    def remove_rule(self):
        port = self.port_entry.get()
        action = "allow" if self.manager.allow_port(port) else "block"
        success = self.manager.remove_rule(port, action)
        if success:
            print(f"Successfully removed rule for port {port}.")
        else:
            print(f"Failed to remove rule for port {port}.")