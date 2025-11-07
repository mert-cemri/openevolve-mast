def sort_lines(lines, reverse=False):
    """Sort lines of a text file alphabetically or reverse-alphabetically.
    Args:
        lines (list): List of lines to be sorted.
        reverse (bool, optional): Sort lines in reverse alphabetical order. Defaults to False.
    Returns:
        list: Sorted list of lines.
    """
    if reverse:
        return sorted(lines, reverse=True)
    else:
        return sorted(lines)