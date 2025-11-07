'''
Module for handling the speed testing logic using speedtest-cli.
This module uses the speedtest library to perform download and upload tests
and returns the results in a dictionary format.
'''
import speedtest
class SpeedTestCLI:
    def __init__(self):
        try:
            self.st = speedtest.Speedtest()
        except AttributeError as e:
            print("Error: The speedtest module does not have a 'Speedtest' class.")
            raise e
        except Exception as e:
            print(f"An unexpected error occurred while initializing Speedtest: {e}")
            raise e
    def run_speed_test(self):
        '''
        Runs the speed test by performing download and upload tests.
        Returns the results as a dictionary.
        '''
        try:
            self.st.download(timeout=10)  # Set a timeout for the download test
            self.st.upload(timeout=10)    # Set a timeout for the upload test
            results = self.st.results.dict()
            return results
        except speedtest.SpeedtestException as e:
            print(f"An error occurred during the speed test: {e}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred during the speed test: {e}")
            return None