'''
Handles displaying the system uptime in the command line interface.
'''
class CLIInterface:
    def __init__(self, uptime_fetcher):
        '''
        Initializes the CLIInterface with an UptimeFetcher instance.
        '''
        self.uptime_fetcher = uptime_fetcher
    def display_uptime(self):
        '''
        Fetches and displays the system uptime in the command line.
        '''
        uptime = self.uptime_fetcher.get_uptime()
        print(f"System Uptime: {uptime}")