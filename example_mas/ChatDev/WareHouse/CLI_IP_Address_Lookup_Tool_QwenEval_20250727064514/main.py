'''
Main module for the IP Address Lookup Tool.
Handles CLI initialization.
'''
import sys
import ip_lookup
import logging
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def main():
    '''
    Main function to handle CLI arguments.
    '''
    if len(sys.argv) == 2:
        ip = sys.argv[1]
        cli_lookup(ip)
    else:
        print("Usage: python main.py <IP_ADDRESS>")
        sys.exit(1)
def cli_lookup(ip):
    '''
    Function to handle CLI-based IP lookup.
    '''
    logging.info(f"Looking up IP address: {ip}")
    info = ip_lookup.get_ip_info(ip)
    if info.get("status") == "fail":
        logging.error(f"Error: {info.get('message')}")
        print(f"Error: {info.get('message')}")
    else:
        logging.info(f"IP Address: {ip}")
        logging.info(f"City: {info.get('city', 'N/A')}")
        logging.info(f"Region: {info.get('regionName', 'N/A')}")
        logging.info(f"Country: {info.get('country', 'N/A')}")
        logging.info(f"ISP: {info.get('isp', 'N/A')}")
        logging.info(f"Latitude: {info.get('lat', 'N/A')}")
        logging.info(f"Longitude: {info.get('lon', 'N/A')}")
        print(f"IP Address: {ip}")
        print(f"City: {info.get('city', 'N/A')}")
        print(f"Region: {info.get('regionName', 'N/A')}")
        print(f"Country: {info.get('country', 'N/A')}")
        print(f"ISP: {info.get('isp', 'N/A')}")
        print(f"Latitude: {info.get('lat', 'N/A')}")
        print(f"Longitude: {info.get('lon', 'N/A')}")
if __name__ == "__main__":
    main()