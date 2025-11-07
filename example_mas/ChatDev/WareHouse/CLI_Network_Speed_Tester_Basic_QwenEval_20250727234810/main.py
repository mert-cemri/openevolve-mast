'''
Main entry point for the network speed tester application.
This script initializes the SpeedTestCLI class, runs the speed test,
and prints the download and upload speeds to the console.
'''
from speedtest_cli import SpeedTestCLI
def main():
    try:
        speed_test_cli = SpeedTestCLI()
        results = speed_test_cli.run_speed_test()
        if results:
            download_speed = results['download'] / 1_000_000  # Convert to Mbps
            upload_speed = results['upload'] / 1_000_000  # Convert to Mbps
            print(f"Download Speed: {download_speed:.2f} Mbps")
            print(f"Upload Speed: {upload_speed:.2f} Mbps")
        else:
            print("Speed test failed. Please check your network connection and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    main()