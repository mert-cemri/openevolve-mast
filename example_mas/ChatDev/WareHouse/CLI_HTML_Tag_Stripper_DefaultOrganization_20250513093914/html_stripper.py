'''
Provides functionality to strip HTML tags from strings.
'''
import re
class HTMLStripper:
    @staticmethod
    def strip_html_tags(text):
        '''
        Removes HTML tags from the given text.
        :param text: String containing HTML content.
        :return: String with HTML tags removed.
        '''
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)