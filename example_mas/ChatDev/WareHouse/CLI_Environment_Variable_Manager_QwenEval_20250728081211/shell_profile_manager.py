'''
Manages the shell profile to persistently set environment variables.
'''
import os
class ShellProfileManager:
    def __init__(self):
        '''
        Initializes the ShellProfileManager with the path to the shell profile.
        Detects the user's shell and sets the appropriate profile path.
        '''
        shell = os.environ.get('SHELL', '')
        if 'zsh' in shell:
            self.profile_path = os.path.expanduser("~/.zshrc")
        elif 'bash' in shell:
            self.profile_path = os.path.expanduser("~/.bashrc")
        elif 'fish' in shell:
            self.profile_path = os.path.expanduser("~/.config/fish/config.fish")
        else:
            raise Exception("Unsupported shell. Please manually specify the profile path.")
    def add_to_profile(self, name, value):
        '''
        Adds an environment variable to the shell profile.
        '''
        if not os.path.exists(self.profile_path):
            with open(self.profile_path, "w") as file:
                pass
        with open(self.profile_path, "a") as file:
            if 'fish' in self.profile_path:
                file.write(f'set -x {name} "{value}"\n')
            else:
                file.write(f'export {name}="{value}"\n')
    def remove_from_profile(self, name):
        '''
        Removes an environment variable from the shell profile.
        '''
        if not os.path.exists(self.profile_path):
            return
        with open(self.profile_path, "r") as file:
            lines = file.readlines()
        with open(self.profile_path, "w") as file:
            for line in lines:
                if not (line.startswith(f'export {name}=' if 'fish' not in self.profile_path else f'set -x {name} ')):
                    file.write(line)
    def is_persistent(self, name):
        '''
        Checks if an environment variable is persistent in the shell profile.
        '''
        if not os.path.exists(self.profile_path):
            return False
        with open(self.profile_path, "r") as file:
            for line in file:
                if line.startswith(f'export {name}=' if 'fish' not in self.profile_path else f'set -x {name} '):
                    return True
        return False