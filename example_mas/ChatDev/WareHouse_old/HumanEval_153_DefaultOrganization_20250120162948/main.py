'''
This module contains the function Strongest_Extension which determines the strongest extension
for a given class name based on the strength calculated from the number of uppercase and lowercase
letters in the extension names.
'''
def Strongest_Extension(class_name, extensions):
    """You will be given the name of a class (a string) and a list of extensions.
    The extensions are to be used to load additional classes to the class. The
    strength of the extension is as follows: Let CAP be the number of the uppercase
    letters in the extension's name, and let SM be the number of lowercase letters 
    in the extension's name, the strength is given by the fraction CAP - SM. 
    You should find the strongest extension and return a string in this 
    format: ClassName.StrongestExtensionName.
    If there are two or more extensions with the same strength, you should
    choose the one that comes first in the list.
    For example, if you are given "Slices" as the class and a list of the
    extensions: ['SErviNGSliCes', 'Cheese', 'StuFfed'] then you should
    return 'Slices.SErviNGSliCes' since 'SErviNGSliCes' is the strongest extension 
    (its strength is -1).
    Example:
    for Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    """
    max_strength = float('-inf')
    strongest_extension = ""
    for extension in extensions:
        cap_count = sum(1 for c in extension if c.isupper())
        sm_count = sum(1 for c in extension if c.islower())
        strength = cap_count - sm_count
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension
    return f"{class_name}.{strongest_extension}"
# Example usage
if __name__ == "__main__":
    print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']))  # Output: Slices.SErviNGSliCes
    print(Strongest_Extension('my_class', ['AA', 'Be', 'CC']))  # Output: my_class.AA