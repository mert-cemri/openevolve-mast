'''
Main module to run the XML Pretty Printer application as a CLI.
'''
import argparse
from xml_pretty_printer import XMLPrettyPrinter
def main():
    parser = argparse.ArgumentParser(description='XML Pretty Printer CLI')
    parser.add_argument('input_file', help='Path to the input XML file')
    parser.add_argument('-o', '--output', help='Path to the output file (optional)', default=None)
    args = parser.parse_args()
    printer = XMLPrettyPrinter()
    if args.output:
        printer.pretty_print_to_file(args.input_file, args.output)
        print(f"Formatted XML saved to: {args.output}")
    else:
        printer.pretty_print_to_console(args.input_file)
if __name__ == "__main__":
    main()