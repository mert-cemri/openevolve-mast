import tkinter as tk
def create_gui(file_path, permissions):
    # Create the GUI window
    window = tk.Tk()
    window.title("File Permissions")
    # Create the file path label
    file_path_label = tk.Label(window, text=file_path)
    file_path_label.pack()
    # Create the permissions label
    permissions_label = tk.Label(window, text=permissions)
    permissions_label.pack()
    # Create the change permissions button
    change_permissions_button = tk.Button(window, text="Change Permissions", command=lambda: change_permissions(file_path, permissions))
    change_permissions_button.pack()
    # Create the exit button
    exit_button = tk.Button(window, text="Exit", command=window.destroy)
    exit_button.pack()
    # Run the GUI
    window.mainloop()
def change_permissions(file_path, permissions):
    # Change the file permissions
    permissions.change_permissions(file_path, permissions)
    # Display the current permissions
    print("Current permissions:", permissions.get_permissions(file_path))