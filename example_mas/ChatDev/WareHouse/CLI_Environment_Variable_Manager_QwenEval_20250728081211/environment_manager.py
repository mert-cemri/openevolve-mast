'''
Manages environment variables, including listing, setting, and unsetting them.
'''
import os
from shell_profile_manager import ShellProfileManager
class EnvironmentManager:
    def __init__(self):
        self.shell_profile_manager = ShellProfileManager()
    def list_variables(self):
        '''
        Returns a dictionary of all environment variables.
        '''
        return os.environ
    def set_variable(self, name, value, persistent=False):
        '''
        Sets an environment variable for the current session.
        If persistent is True, also adds the variable to the shell profile.
        '''
        os.environ[name] = value
        if persistent:
            self.shell_profile_manager.add_to_profile(name, value)
    def unset_variable(self, name):
        '''
        Unsets an environment variable for the current session.
        If the variable is persistent, also removes it from the shell profile.
        '''
        if name in os.environ:
            del os.environ[name]
            if self.shell_profile_manager.is_persistent(name):
                self.shell_profile_manager.remove_from_profile(name)