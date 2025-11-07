def plot_line_graph(self):
    print("\nLine Graph:")
    # Find the maximum value in the data to scale the graph
    max_value = max(self.data) if self.data else 0
    # Calculate the scale factor to fit the graph within 50 characters
    scale = 50 / max_value if max_value > 0 else 1
    line_graph = []
    previous_scaled_value = 0
    for i, value in enumerate(self.data):
        # Scale the current value to fit within the graph
        scaled_value = int(value * scale)
        if i == 0:
            # For the first value, just place the '*' at the scaled position
            line = ' ' * scaled_value + '*'
        else:
            # For subsequent values, draw a line from the previous scaled position to the current scaled position
            line = ' ' * previous_scaled_value + '*' + ' ' * (scaled_value - previous_scaled_value) + '*'
        # Append the line to the line graph list with the value
        line_graph.append(f"{value:6.2f} | {line}")
        # Update the previous scaled value for the next iteration
        previous_scaled_value = scaled_value
    # Print and return the line graph
    print("\n".join(line_graph))
    return "\n".join(line_graph)