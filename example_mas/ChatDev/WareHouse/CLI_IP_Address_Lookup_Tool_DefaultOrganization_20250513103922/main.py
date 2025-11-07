'''
This file contains the main application logic for the IP lookup tool using a command-line interface.
'''
import argparse
import requests
def fetch_ip_info(ip_address):
    '''
    Make an API request to ip-api.com and return the geolocation and ISP information.
    '''
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    data = response.json()
    if data['status'] != 'success':
        raise Exception("Failed to retrieve data. Please check the IP address and try again.")
    return data
def main():
    '''
    Parse command-line arguments and fetch IP information.
    '''
    parser = argparse.ArgumentParser(description='IP Lookup Tool')
    parser.add_argument('ip', type=str, help='IP address to look up')
    args = parser.parse_args()
    try:
        info = fetch_ip_info(args.ip)
        print(f"IP: {info['query']}")
        print(f"Country: {info['country']}")
        print(f"Region: {info['regionName']}")
        print(f"City: {info['city']}")
        print(f"ISP: {info['isp']}")
        print(f"Latitude: {info['lat']}")
        print(f"Longitude: {info['lon']}")
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()