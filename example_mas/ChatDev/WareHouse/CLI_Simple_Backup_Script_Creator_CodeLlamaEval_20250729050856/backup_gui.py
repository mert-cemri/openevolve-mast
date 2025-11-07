import tkinter as tk
from tkinter import filedialog
# Create the GUI window
window = tk.Tk()
window.title("Backup Script Creator")
# Create a label and entry field for the source directories
source_dirs_label = tk.Label(window, text="Source Directories:")
source_dirs_label.pack()
source_dirs_entry = tk.Entry(window)
source_dirs_entry.pack()
# Create a label and entry field for the target directory
target_dir_label = tk.Label(window, text="Target Directory:")
target_dir_label.pack()
target_dir_entry = tk.Entry(window)
target_dir_entry.pack()
# Create a button to create the backup script
create_script_button = tk.Button(window, text="Create Backup Script", command=create_backup_script)
create_script_button.pack()
# Create a button to exit the GUI
exit_button = tk.Button(window, text="Exit", command=window.destroy)
exit_button.pack()
# Run the GUI
window.mainloop()