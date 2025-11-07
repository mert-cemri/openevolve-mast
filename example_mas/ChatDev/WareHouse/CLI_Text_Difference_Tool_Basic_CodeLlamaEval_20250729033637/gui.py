import tkinter as tk
# Create a GUI window
root = tk.Tk()
root.title("Text Difference Tool")
# Create a label and entry field for the first text file
label1 = tk.Label(root, text="First Text File:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()
# Create a label and entry field for the second text file
label2 = tk.Label(root, text="Second Text File:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()
# Create a button to start the difference calculation
button = tk.Button(root, text="Calculate Difference", command=calculate_difference)
button.pack()
# Create a label and entry field for the output file
label3 = tk.Label(root, text="Output File:")
label3.pack()
entry3 = tk.Entry(root)
entry3.pack()
# Create a button to write the output to a file
button2 = tk.Button(root, text="Write Output", command=write_output)
button2.pack()
# Start the GUI event loop
root.mainloop()