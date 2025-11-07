import permissions
import utils
import gui
def main():
    # Get the user input
    file_path = input("Enter the file or directory path: ")
    permissions = input("Enter the new permissions (e.g., 755, 644): ")
    # Validate the input
    if not utils.validate_file_path(file_path):
        print("Invalid file or directory path.")
        return
    if not utils.validate_permissions(permissions):
        print("Invalid permissions.")
        return
    # Change the file permissions
    permissions.change_permissions(file_path, permissions)
    # Display the current permissions
    print("Current permissions:", permissions.get_permissions(file_path))
    # Create the GUI
    gui.create_gui(file_path, permissions)
if __name__ == "__main__":
    main()