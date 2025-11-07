import os
def change_permissions(file_path, permissions):
    # Check if the file or directory exists
    if not os.path.exists(file_path):
        raise FileNotFoundError("File or directory not found.")
    # Get the current permissions
    current_permissions = get_permissions(file_path)
    # Change the permissions
    os.chmod(file_path, permissions)
    # Return the new permissions
    return get_permissions(file_path)
def get_permissions(file_path):
    # Check if the file or directory exists
    if not os.path.exists(file_path):
        raise FileNotFoundError("File or directory not found.")
    # Get the current permissions
    return oct(os.stat(file_path).st_mode)[-3:]