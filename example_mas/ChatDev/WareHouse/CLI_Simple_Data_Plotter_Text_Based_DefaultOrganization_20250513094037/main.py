'''
Main application file for CLI data plotter. Handles user input and coordinates plotting.
'''
import sys
from plotter import plot_bar_chart, plot_line_graph
def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <mode> <source>")
        print("<mode>: 'bar' or 'line'")
        print("<source>: 'stdin' or a filename")
        sys.exit(1)
    mode = sys.argv[1]
    source = sys.argv[2]
    if source == 'stdin':
        numbers = read_numbers_from_stdin()
    else:
        numbers = read_numbers_from_file(source)
    if mode == 'bar':
        plot_bar_chart(numbers)
    elif mode == 'line':
        plot_line_graph(numbers)
    else:
        print("Invalid mode. Use 'bar' or 'line'.")
        sys.exit(1)
def read_numbers_from_stdin():
    print("Enter numbers separated by spaces:")
    input_line = input()
    return list(map(float, input_line.split()))
def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        return list(map(float, file.read().split()))
if __name__ == "__main__":
    main()