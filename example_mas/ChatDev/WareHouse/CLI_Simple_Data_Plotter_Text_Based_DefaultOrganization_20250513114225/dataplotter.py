'''
Contains the DataPlotter class and utility functions for reading data.
'''
def read_data_from_file(filename):
    '''
    Reads a list of numbers from a file.
    '''
    with open(filename, 'r') as file:
        data = file.read().strip().split()
    return list(map(float, data))
def read_data_from_stdin():
    '''
    Reads a list of numbers from standard input.
    '''
    print("Enter numbers separated by spaces:")
    data = input().strip().split()
    return list(map(float, data))
class DataPlotter:
    '''
    Class for plotting data as a bar chart or line graph.
    '''
    def __init__(self, data):
        self.data = data
    def plot_bar_chart(self):
        '''
        Plots a bar chart of the data.
        '''
        max_value = max(self.data)
        scale = 50 / max_value if max_value > 0 else 1
        for value in self.data:
            bar = '#' * int(value * scale)
            print(f"{value:>5}: {bar}")
    def plot_line_graph(self):
        '''
        Plots a line graph of the data.
        '''
        max_value = max(self.data)
        scale = 50 / max_value if max_value > 0 else 1
        previous_value = None
        for i, value in enumerate(self.data):
            scaled_value = int(value * scale)
            if previous_value is not None:
                line = ' ' * min(previous_value, scaled_value) + '*' * abs(previous_value - scaled_value)
            else:
                line = ' ' * scaled_value + '*'
            print(f"{i:>3}: {line}")
            previous_value = scaled_value