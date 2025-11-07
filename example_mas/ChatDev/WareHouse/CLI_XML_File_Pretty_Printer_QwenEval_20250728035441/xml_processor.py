'''
Handles the parsing and pretty-printing of XML files.
'''
import xml.dom.minidom
class XMLProcessor:
    def __init__(self):
        pass
    def pretty_print(self, xml_string):
        '''
        Takes an XML string and returns a well-formatted, indented version.
        Handles XML namespaces gracefully.
        '''
        try:
            dom = xml.dom.minidom.parseString(xml_string)
            return dom.toprettyxml(indent="  ", encoding="UTF-8").decode('utf-8')
        except Exception as e:
            raise ValueError(f"Invalid XML: {e}")
    def read_file(self, file_path):
        '''
        Reads the content of an XML file and returns it as a string.
        '''
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    def write_file(self, file_path, content):
        '''
        Writes the given content to a file.
        '''
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)