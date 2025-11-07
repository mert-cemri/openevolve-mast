'''
Module to handle XML pretty printing operations.
'''
from lxml import etree
class XMLPrettyPrinter:
    def pretty_print_to_console(self, file_path):
        '''
        Reads an XML file and prints the formatted XML to the console.
        '''
        try:
            with open(file_path, 'rb') as file:
                xml_content = file.read()
                parser = etree.XMLParser(remove_blank_text=True)
                dom = etree.XML(xml_content, parser)
                pretty_xml_as_string = etree.tostring(dom, pretty_print=True, encoding='unicode')
                print(pretty_xml_as_string)
        except etree.XMLSyntaxError as e:
            print(f"XML Syntax Error: {e}")
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
        except Exception as e:
            print(f"Error: {e}")
    def pretty_print_to_file(self, input_file_path, output_file_path):
        '''
        Reads an XML file and writes the formatted XML to a new file.
        '''
        try:
            with open(input_file_path, 'rb') as file:
                xml_content = file.read()
                parser = etree.XMLParser(remove_blank_text=True)
                dom = etree.XML(xml_content, parser)
                pretty_xml_as_string = etree.tostring(dom, pretty_print=True, encoding='unicode')
            with open(output_file_path, 'w', encoding='utf-8') as file:
                file.write(pretty_xml_as_string)
        except etree.XMLSyntaxError as e:
            print(f"XML Syntax Error: {e}")
        except FileNotFoundError:
            print(f"Error: The file {input_file_path} was not found.")
        except Exception as e:
            print(f"Error: {e}")