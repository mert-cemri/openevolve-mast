'''
Main application file for the CLI network speed tester.
'''
import speedtest
class SpeedTester:
    '''
    Handles the network speed testing using the speedtest-cli library.
    '''
    def __init__(self):
        self.st = speedtest.Speedtest()
    def test_download_speed(self):
        '''
        Measures and returns the download speed in Mbps.
        '''
        return self.st.download() / 1_000_000  # Convert to Mbps
    def test_upload_speed(self):
        '''
        Measures and returns the upload speed in Mbps.
        '''
        return self.st.upload() / 1_000_000  # Convert to Mbps
def main():
    '''
    Main function to run the speed test and print the results.
    '''
    speed_tester = SpeedTester()
    print("Testing network speed...")
    download_speed = speed_tester.test_download_speed()
    upload_speed = speed_tester.test_upload_speed()
    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
if __name__ == "__main__":
    main()