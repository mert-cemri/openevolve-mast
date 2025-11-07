'''
Provides functionality to strip HTML tags from a string.
'''
import re
class HTMLStripper:
    @staticmethod
    def strip_tags(html_content: str) -> str:
        '''
        Remove HTML tags from the given string.
        :param html_content: A string containing HTML content.
        :return: A string with HTML tags removed.
        '''
        # Regular expression to match HTML tags
        clean = re.compile('<.*?>')
        return re.sub(clean, '', html_content)