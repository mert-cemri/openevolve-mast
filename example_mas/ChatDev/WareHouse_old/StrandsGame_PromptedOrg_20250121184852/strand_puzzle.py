'''
StrandPuzzle class to manage the word-segmentation puzzle logic.
'''
class StrandPuzzle:
    def __init__(self):
        self.strands = []
        self.completed = False
    def load_strands(self, file_path='strands.txt'):
        '''
        Load strands from a specified file.
        '''
        try:
            with open(file_path, 'r') as file:
                self.strands = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print("Strands file not found. Please ensure the file exists.")
            self.strands = []
    def combine_strands(self, strands_to_combine):
        '''
        Combine strands and check if they form a valid word or phrase.
        '''
        # Check if all strands are available
        if not all(strand in self.strands for strand in strands_to_combine):
            print("One or more strands are not available. Try again.")
            return False
        combined = ''.join(strands_to_combine)
        if self.is_valid_combination(combined):
            # Remove used strands
            for strand in strands_to_combine:
                self.strands.remove(strand)
            return True
        elif self.is_valid_prefix(combined):
            print("The combination is a valid prefix, but not a complete word or phrase.")
            return False
        else:
            print("Invalid combination. Try again.")
            return False
    def is_valid_combination(self, combined):
        '''
        Verify if the combined strands form a valid word or phrase.
        '''
        # Example valid words
        valid_words = ["hello", "world"]
        return combined in valid_words
    def is_valid_prefix(self, combined):
        '''
        Verify if the combined strands form a valid prefix of any word or phrase.
        '''
        # Example valid words
        valid_words = ["hello", "world"]
        return any(word.startswith(combined) for word in valid_words)
    def check_completion(self):
        '''
        Check if all strands have been correctly merged.
        '''
        return len(self.strands) == 0