'''
Plotting module for CLI data plotter. Contains functions for generating text-based charts.
'''
def plot_bar_chart(numbers):
    max_height = max(numbers)
    scale_factor = 50 / max_height if max_height > 0 else 1
    for number in numbers:
        bar = '#' * int(number * scale_factor)
        print(f"{number:>5}: {bar}")
def plot_line_graph(numbers):
    max_height = max(numbers)
    scale_factor = 50 / max_height if max_height > 0 else 1
    previous_height = None
    for number in numbers:
        current_height = int(number * scale_factor)
        if previous_height is not None:
            if current_height != previous_height:
                for i in range(min(previous_height, current_height), max(previous_height, current_height)):
                    print(' ' * 5 + '|')
        print(f"{number:>5}: " + ' ' * current_height + '*')
        previous_height = current_height