'''
Helper function to interact with the Google Translate API.
'''
import os
import requests
def translate(text, target_language):
    '''
    Translate the given text to the target language using Google Translate API.
    Parameters:
    text (str): The text to translate.
    target_language (str): The target language code (e.g., 'es' for Spanish).
    Returns:
    str: The translated text.
    '''
    # Retrieve the API key from an environment variable
    api_key = os.getenv('GOOGLE_TRANSLATE_API_KEY')
    if not api_key:
        raise Exception("API key not found. Please set the 'GOOGLE_TRANSLATE_API_KEY' environment variable.")
    url = f"https://translation.googleapis.com/language/translate/v2?key={api_key}"
    data = {
        'q': text,
        'target': target_language
    }
    response = requests.post(url, json=data)  # Use 'json' to send the payload as JSON
    if response.status_code != 200:
        raise Exception(f"Error: {response.status_code} - {response.text}")
    result = response.json()
    return result['data']['translations'][0]['translatedText']