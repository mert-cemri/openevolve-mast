'''
Class definition for the Strands puzzle game.
'''
class StrandPuzzle:
    def __init__(self, strands, solutions):
        '''
        Initializes the puzzle with strands and solutions.
        :param strands: List of initial strands.
        :param solutions: List of valid merged solutions.
        '''
        self.strands = strands
        self.solutions = solutions
        self.completed_merges = []
    def display_strands(self):
        '''
        Displays the current available strands with their indices.
        '''
        print("🔤 Available strands:")
        for idx, strand in enumerate(self.strands):
            print(f"{idx}: '{strand}'")
    def merge_strands(self, indices):
        '''
        Attempts to merge strands at given indices.
        :param indices: List of indices to merge.
        :return: Tuple containing merged strand and boolean indicating validity.
        '''
        if not indices or any(i < 0 or i >= len(self.strands) for i in indices):
            raise IndexError("Indices out of range or empty.")
        merged_strand = ''.join([self.strands[i] for i in indices])
        if merged_strand in self.solutions:
            # Remove merged strands and add merged result
            for i in sorted(indices, reverse=True):
                del self.strands[i]
            self.completed_merges.append(merged_strand)
            return merged_strand, True
        return merged_strand, False
    def is_completed(self):
        '''
        Checks if all solutions have been found.
        :return: True if puzzle is completed, False otherwise.
        '''
        return sorted(self.completed_merges) == sorted(self.solutions)