'''
This module contains the implementation of the Strongest_Extension function,
which determines the strongest extension for a given class based on the strength
calculated from the number of uppercase and lowercase letters in the extension names.
'''
def Strongest_Extension(class_name, extensions):
    """
    Determines the strongest extension for a given class based on the strength
    calculated from the number of uppercase and lowercase letters in the extension names.
    Parameters:
    class_name (str): The name of the class.
    extensions (list of str): A list of extension names.
    Returns:
    str: The class name concatenated with the strongest extension in the format
         ClassName.StrongestExtensionName.
    """
    max_strength = float('-inf')
    strongest_extension = None
    for extension in extensions:
        cap_count = sum(1 for c in extension if c.isupper())
        sm_count = sum(1 for c in extension if c.islower())
        strength = cap_count - sm_count
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension
    return f"{class_name}.{strongest_extension}"