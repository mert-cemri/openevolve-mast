'''
Parses the fetched RSS feed and extracts article titles and links.
Handles cases where 'title' or 'link' might be missing.
'''
import xml.etree.ElementTree as ET
class RSSParser:
    def parse(self, content):
        try:
            root = ET.fromstring(content)
        except ET.ParseError as e:
            print(f"Error parsing XML: {e}")
            return []
        articles = []
        for item in root.findall('.//item'):
            title = item.find('title').text if item.find('title') is not None else 'No Title'
            link = item.find('link').text if item.find('link') is not None else 'No Link'
            articles.append((title, link))
        return articles