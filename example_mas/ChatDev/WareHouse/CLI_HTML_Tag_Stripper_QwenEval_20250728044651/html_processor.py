'''
HTML processing logic using BeautifulSoup.
'''
from bs4 import BeautifulSoup
def strip_html_tags(html_content):
    '''
    Strips HTML tags from the given HTML content and returns plain text.
    '''
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text()