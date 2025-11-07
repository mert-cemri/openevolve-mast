'''
This module contains the implementation of the Strongest_Extension function.
The function calculates the strength of each extension based on the number of uppercase and lowercase letters,
and returns the strongest extension in the format: ClassName.StrongestExtensionName.
'''
def Strongest_Extension(class_name, extensions):
    def calculate_strength(extension):
        cap_count = sum(1 for c in extension if c.isupper())
        sm_count = sum(1 for c in extension if c.islower())
        return cap_count - sm_count
    strongest_extension = None
    max_strength = float('-inf')
    for extension in extensions:
        strength = calculate_strength(extension)
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension
    return f"{class_name}.{strongest_extension}"
# Example usage:
# print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']))  # Output: 'Slices.SErviNGSliCes'
# print(Strongest_Extension('my_class', ['AA', 'Be', 'CC']))  # Output: 'my_class.AA'