'''
Contains the EnvVarManager class for managing environment variables.
'''
import os
class EnvVarManager:
    def list_vars(self):
        '''List all current environment variables.'''
        return os.environ.items()
    def set_var(self, name, value, persistent=False):
        '''Set an environment variable.'''
        os.environ[name] = value
        if persistent:
            self._update_shell_profile(name, value)
    def unset_var(self, name, persistent=False):
        '''Unset an environment variable.'''
        if name in os.environ:
            del os.environ[name]
        if persistent:
            self._remove_from_shell_profile(name)
    def _get_shell_profile_path(self):
        '''Determine the shell profile path based on the user's shell.'''
        shell = os.environ.get('SHELL', '')
        if 'bash' in shell:
            return os.path.expanduser("~/.bashrc")
        elif 'zsh' in shell:
            return os.path.expanduser("~/.zshrc")
        # Add more conditions for other shells if needed
        else:
            raise EnvironmentError("Unsupported shell environment")
    def _update_shell_profile(self, name, value):
        '''Update the shell profile to persist the environment variable.'''
        profile_path = self._get_shell_profile_path()
        with open(profile_path, "a") as file:
            file.write(f'\nexport {name}="{value}"\n')
    def _remove_from_shell_profile(self, name):
        '''Remove the environment variable from the shell profile.'''
        profile_path = self._get_shell_profile_path()
        with open(profile_path, "r") as file:
            lines = file.readlines()
        with open(profile_path, "w") as file:
            for line in lines:
                if not line.startswith(f'export {name}='):
                    file.write(line)