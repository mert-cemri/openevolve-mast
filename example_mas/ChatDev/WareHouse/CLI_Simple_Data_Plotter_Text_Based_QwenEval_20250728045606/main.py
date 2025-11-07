'''
Main file for the CLI data plotter application.
Handles command-line arguments and orchestrates the program flow.
'''
import sys
import argparse
from dataloader import DataLoader
from plotter import Plotter
from gui import GUI
def main():
    parser = argparse.ArgumentParser(description='CLI Data Plotter')
    parser.add_argument('-f', '--file', type=str, help='Input file containing numbers')
    parser.add_argument('-g', '--gui', action='store_true', help='Launch GUI')
    args = parser.parse_args()
    if args.gui:
        gui = GUI()
        gui.run()
    else:
        data_loader = DataLoader()
        if args.file:
            data = data_loader.load_from_file(args.file)
        else:
            data = data_loader.load_from_stdin()
        plotter = Plotter(data)
        plotter.plot_bar_chart()
        plotter.plot_line_graph()
if __name__ == '__main__':
    main()