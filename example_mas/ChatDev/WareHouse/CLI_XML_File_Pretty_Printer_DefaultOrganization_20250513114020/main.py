'''
CLI application for XML Pretty Printer.
'''
import argparse
from xml.dom.minidom import parseString
def pretty_print_xml(xml_content):
    '''
    Pretty print the XML content using xml.dom.minidom.
    '''
    dom = parseString(xml_content)
    return dom.toprettyxml(indent="  ")
def main():
    '''
    Main function to handle command-line arguments and perform XML pretty printing.
    '''
    parser = argparse.ArgumentParser(description='CLI XML Pretty Printer')
    parser.add_argument('input_file', help='Path to the input XML file')
    parser.add_argument('-o', '--output', help='Path to the output file (optional)')
    args = parser.parse_args()
    with open(args.input_file, 'r') as file:
        xml_content = file.read()
        pretty_content = pretty_print_xml(xml_content)
        if args.output:
            with open(args.output, 'w') as output_file:
                output_file.write(pretty_content)
        else:
            print(pretty_content)
if __name__ == "__main__":
    main()