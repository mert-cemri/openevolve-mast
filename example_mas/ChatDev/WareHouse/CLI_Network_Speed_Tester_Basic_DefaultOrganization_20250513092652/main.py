'''
Main application file for the CLI network speed tester.
'''
from speed_test import perform_speed_test
def main():
    '''
    Run the network speed test and print the results.
    '''
    print("Starting network speed test...")
    try:
        download_speed, upload_speed = perform_speed_test()
        print(f"Download Speed: {download_speed:.2f} Mbps")
        print(f"Upload Speed: {upload_speed:.2f} Mbps")
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()