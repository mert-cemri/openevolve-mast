'''
Main entry point for the CLI data plotter application.
'''
import sys
from dataplotter import DataPlotter, read_data_from_file, read_data_from_stdin
def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_type> [<filename>]")
        print("<input_type>: 'file' to read from a file, 'stdin' to read from standard input")
        return
    input_type = sys.argv[1]
    if input_type == 'file':
        if len(sys.argv) < 3:
            print("Please provide a filename.")
            return
        filename = sys.argv[2]
        data = read_data_from_file(filename)
    elif input_type == 'stdin':
        data = read_data_from_stdin()
    else:
        print("Invalid input type. Use 'file' or 'stdin'.")
        return
    plotter = DataPlotter(data)
    print("Choose plot type: 'bar' for bar chart, 'line' for line graph")
    plot_type = input().strip().lower()
    if plot_type == 'bar':
        plotter.plot_bar_chart()
    elif plot_type == 'line':
        plotter.plot_line_graph()
    else:
        print("Invalid plot type. Use 'bar' or 'line'.")
if __name__ == "__main__":
    main()