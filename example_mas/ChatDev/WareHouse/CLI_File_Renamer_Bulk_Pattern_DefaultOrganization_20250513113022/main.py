'''
CLI File Renamer application that renames multiple files in a directory based on a specified pattern.
'''
import os
import argparse
def rename_files(directory, prefix, substring_to_replace, replacement_substring, start_number):
    if not os.path.isdir(directory):
        print("Error: Please select a valid directory.")
        return
    files = get_files_in_directory(directory)
    if not files:
        print("Info: No files found in the selected directory.")
        return
    for i, filename in enumerate(files):
        new_name = filename
        # Add prefix
        if prefix:
            new_name = add_prefix(new_name, prefix)
        # Replace substring
        if substring_to_replace and replacement_substring:
            new_name = replace_substring(new_name, substring_to_replace, replacement_substring)
        # Add sequential numbers
        new_name = add_sequential_numbers(new_name, start_number + i)
        # Rename the file
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
    print("Success: Files have been renamed successfully.")
def add_prefix(filename, prefix):
    return prefix + filename
def replace_substring(filename, old, new):
    return filename.replace(old, new)
def add_sequential_numbers(filename, number):
    name, ext = os.path.splitext(filename)
    return f"{name}_{number}{ext}"
def get_files_in_directory(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI File Renamer")
    parser.add_argument("directory", help="Directory containing files to rename")
    parser.add_argument("--prefix", help="Prefix to add to filenames", default="")
    parser.add_argument("--replace", help="Substring to replace in filenames", default="")
    parser.add_argument("--replacement", help="Replacement substring", default="")
    parser.add_argument("--start-number", type=int, help="Starting number for sequential numbering", default=1)
    args = parser.parse_args()
    # Check if both replace and replacement are provided
    if args.replace and not args.replacement:
        print("Error: Please provide a replacement substring using --replacement when using --replace.")
        exit(1)
    if args.replacement and not args.replace:
        print("Error: Please provide a substring to replace using --replace when using --replacement.")
        exit(1)
    rename_files(args.directory, args.prefix, args.replace, args.replacement, args.start_number)