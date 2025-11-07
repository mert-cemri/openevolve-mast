'''
Utility functions for performing network speed tests using speedtest-cli.
'''
import speedtest
def perform_speed_test():
    '''
    Perform a network speed test and return download and upload speeds.
    '''
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    return download_speed, upload_speed