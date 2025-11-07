'''
Manages data visualization for the dashboard application.
'''
import tkinter as tk
class Visualization:
    def create_chart(self, canvas, data):
        # Clear previous chart
        canvas.delete("all")
        # Directly draw the chart
        self._draw_chart(canvas, data)
    def _draw_chart(self, canvas, data):
        # Simulate creating a bar chart
        bar_width = 20
        spacing = 10
        max_value = max(data)
        canvas_height = canvas.winfo_height()
        for i, value in enumerate(data):
            x0 = i * (bar_width + spacing)
            # Scale the bar height relative to the maximum data value and canvas height
            y0 = canvas_height - (value / max_value) * canvas_height
            x1 = x0 + bar_width
            y1 = canvas_height
            canvas.create_rectangle(x0, y0, x1, y1, fill="blue")