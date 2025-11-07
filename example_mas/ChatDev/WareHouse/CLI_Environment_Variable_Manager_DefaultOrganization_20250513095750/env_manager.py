'''
This module contains the EnvironmentManager class which provides methods to list, set, and unset environment variables.
'''
import os
class EnvironmentManager:
    def list_env_vars(self):
        '''List all current environment variables.'''
        return os.environ.copy()
    def set_env_var(self, name, value, persistent=False):
        '''Set an environment variable.'''
        os.environ[name] = value
        if persistent:
            self._add_to_shell_profile(name, value)
    def unset_env_var(self, name, persistent=False):
        '''Unset an environment variable.'''
        if name in os.environ:
            del os.environ[name]
        if persistent:
            self._remove_from_shell_profile(name)
    def _get_shell_profile_path(self):
        '''Get the shell profile path based on the user's shell.'''
        shell = os.environ.get('SHELL', '')
        if 'bash' in shell:
            return os.path.expanduser('~/.bashrc')
        elif 'zsh' in shell:
            return os.path.expanduser('~/.zshrc')
        elif 'fish' in shell:
            return os.path.expanduser('~/.config/fish/config.fish')
        elif 'csh' in shell or 'tcsh' in shell:
            return os.path.expanduser('~/.cshrc')
        # Add more shell checks as needed
        else:
            raise EnvironmentError("Unsupported shell. Please manually add the environment variable to your shell profile.")
    def _add_to_shell_profile(self, name, value):
        '''Add an environment variable to the shell profile for persistence.'''
        profile_path = self._get_shell_profile_path()
        with open(profile_path, 'a') as file:
            file.write(f'\nexport {name}="{value}"\n')
    def _remove_from_shell_profile(self, name):
        '''Remove an environment variable from the shell profile.'''
        profile_path = self._get_shell_profile_path()
        with open(profile_path, 'r') as file:
            lines = file.readlines()
        with open(profile_path, 'w') as file:
            for line in lines:
                if not line.strip().startswith(f'export {name}='):
                    file.write(line)