'''
Module to handle IP address lookup using a public API.
'''
import requests
import logging
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def get_ip_info(ip):
    '''
    Function to fetch IP information from the API.
    '''
    url = f"http://ip-api.com/json/{ip}"
    try:
        logging.info(f"Fetching IP information for: {ip}")
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        if response.headers['Content-Type'] == 'application/json':
            logging.info(f"Successfully fetched IP information for: {ip}")
            return response.json()
        else:
            logging.error(f"Response is not in JSON format for IP: {ip}")
            return {"status": "fail", "message": "Response is not in JSON format"}
    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTP error occurred for IP: {ip} - {e}")
        return {"status": "fail", "message": f"HTTP error: {e}"}
    except requests.exceptions.ConnectionError as e:
        logging.error(f"Connection error occurred for IP: {ip} - {e}")
        return {"status": "fail", "message": f"Connection error: {e}"}
    except requests.exceptions.Timeout as e:
        logging.error(f"Timeout error occurred for IP: {ip} - {e}")
        return {"status": "fail", "message": f"Timeout error: {e}"}
    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred for IP: {ip} - {e}")
        return {"status": "fail", "message": f"An error occurred: {e}"}