'''
This module contains the implementation of the Strongest_Extension function,
which determines the strongest extension based on the number of uppercase and
lowercase letters in the extension names.
'''
def Strongest_Extension(class_name, extensions):
    """Determine the strongest extension based on the number of uppercase and
    lowercase letters in the extension names.
    Args:
        class_name (str): The name of the class.
        extensions (list of str): A list of extension names.
    Returns:
        str: The class name concatenated with the strongest extension name.
    """
    max_strength = float('-inf')
    strongest_extension = ""
    for extension in extensions:
        cap_count = sum(1 for char in extension if char.isupper())
        sm_count = sum(1 for char in extension if char.islower())
        strength = cap_count - sm_count
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension
        elif strength == max_strength and strongest_extension == "":
            strongest_extension = extension
    return f"{class_name}.{strongest_extension}"