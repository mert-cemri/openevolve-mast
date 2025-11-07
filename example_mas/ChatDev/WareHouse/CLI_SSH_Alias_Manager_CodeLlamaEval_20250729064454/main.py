import tkinter as tk
from ssh_alias_manager import SSHAliasManager
class SSHAliasManagerGUI:
    def __init__(self, master):
        self.master = master
        self.manager = SSHAliasManager('ssh_aliases.json')
        self.create_widgets()
    def create_widgets(self):
        self.add_button = tk.Button(self.master, text='Add', command=self.add_alias)
        self.add_button.pack()
        self.list_button = tk.Button(self.master, text='List', command=self.list_aliases)
        self.list_button.pack()
        self.remove_button = tk.Button(self.master, text='Remove', command=self.remove_alias)
        self.remove_button.pack()
    def add_alias(self):
        name = input('Enter alias name: ')
        hostname = input('Enter hostname: ')
        user = input('Enter user: ')
        port = input('Enter port: ')
        key_file = input('Enter key file: ')
        self.manager.add_alias({'name': name, 'hostname': hostname, 'user': user, 'port': port, 'key_file': key_file})
    def list_aliases(self):
        for alias in self.manager.list_aliases():
            print(alias['name'])
    def remove_alias(self):
        name = input('Enter alias name: ')
        self.manager.remove_alias(name)
def main():
    root = tk.Tk()
    root.title('SSH Alias Manager')
    app = SSHAliasManagerGUI(root)
    root.mainloop()
if __name__ == '__main__':
    main()