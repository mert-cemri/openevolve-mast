'''
Handles sorting logic.
'''
class Sorter:
    def sort(self, lines, reverse=False):
        '''
        Sorts a list of lines alphabetically or reverse-alphabetically.
        Parameters:
        lines (list of str): The lines to be sorted.
        reverse (bool): If True, sorts the lines in reverse-alphabetical order.
        Returns:
        list of str: The sorted lines.
        '''
        return sorted(lines, reverse=reverse)