'''
This module defines the StrandPuzzle class, which manages the word-segmentation puzzle logic.
'''
VALID_WORDS = {"hello", "world", "example", "strand", "puzzle"}
class StrandPuzzle:
    def __init__(self, strands):
        '''
        Initialize the puzzle with a list of strands.
        :param strands: List of string strands.
        '''
        self.strands = strands
        self.completed = False
    def combine_strands(self, indices):
        '''
        Combine strands at specified indices and check if they form a valid word or phrase.
        :param indices: List of indices of strands to combine.
        :return: Boolean indicating if the combination is valid.
        '''
        combined_strand = ''.join([self.strands[i] for i in indices])
        # Check if the combined strand is a valid word or phrase
        if combined_strand.strip() in VALID_WORDS:
            # Remove the combined strands and add the new one
            for i in sorted(indices, reverse=True):
                del self.strands[i]
            self.strands.append(combined_strand)
            return True
        return False
    def is_complete(self):
        '''
        Check if all strands have been correctly combined.
        :return: Boolean indicating if the puzzle is complete.
        '''
        # Check if any further valid combinations can be formed
        for i in range(len(self.strands)):
            for j in range(i + 1, len(self.strands)):
                if ''.join([self.strands[i], self.strands[j]]).strip() in VALID_WORDS:
                    return False
        # Puzzle is complete when no further valid combinations can be formed
        return len(self.strands) == 1