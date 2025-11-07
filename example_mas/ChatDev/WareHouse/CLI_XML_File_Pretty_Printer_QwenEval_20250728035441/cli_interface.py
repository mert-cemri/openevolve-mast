'''
Handles command-line arguments and options for the XML file pretty printer.
'''
import argparse
import os
from xml.etree import ElementTree
from xml_processor import XMLProcessor
class CLIInterface:
    def __init__(self):
        self.xml_processor = XMLProcessor()
        self.parser = argparse.ArgumentParser(description='XML File Pretty Printer')
        self.parser.add_argument('input_file', type=str, help='Input XML file path')
        self.parser.add_argument('-o', '--output', type=str, help='Output file path (optional)')
        self.args = self.parser.parse_args()
    def run(self):
        input_file = self.args.input_file
        output_file = self.args.output
        if not os.path.isfile(input_file):
            print(f"Error: The file {input_file} does not exist.")
            return
        try:
            ElementTree.parse(input_file)  # Validate XML file
        except ElementTree.ParseError as e:
            print(f"Error: The file {input_file} is not a valid XML file: {e}")
            return
        try:
            xml_content = self.xml_processor.read_file(input_file)
            pretty_xml = self.xml_processor.pretty_print(xml_content)
            if output_file:
                self.xml_processor.write_file(output_file, pretty_xml)
                print(f"Pretty-printed XML saved to {output_file}")
            else:
                print(pretty_xml)
        except Exception as e:
            print(f"Error: {e}")