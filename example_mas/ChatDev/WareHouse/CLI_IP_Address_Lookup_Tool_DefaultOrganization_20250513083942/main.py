'''
This script is a CLI tool for IP address lookup using the ip-api.com API.
It takes an IP address as input and returns geolocation and ISP information.
'''
import requests
import argparse
def fetch_ip_info(ip_address):
    '''
    Make an API request to ip-api.com and return the response.
    '''
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()
def display_result(data):
    '''
    Display the fetched IP information in the console.
    '''
    if data['status'] == 'success':
        result = (
            f"IP: {data['query']}\n"
            f"Country: {data['country']}\n"
            f"Region: {data['regionName']}\n"
            f"City: {data['city']}\n"
            f"ISP: {data['isp']}\n"
            f"Latitude: {data['lat']}\n"
            f"Longitude: {data['lon']}\n"
        )
    else:
        result = "Error: Unable to fetch data. Please check the IP address."
    print(result)
def main():
    '''
    Parse command-line arguments and perform IP address lookup.
    '''
    parser = argparse.ArgumentParser(description='IP Address Lookup CLI Tool')
    parser.add_argument('ip_address', type=str, help='IP address to look up')
    args = parser.parse_args()
    try:
        data = fetch_ip_info(args.ip_address)
        display_result(data)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()