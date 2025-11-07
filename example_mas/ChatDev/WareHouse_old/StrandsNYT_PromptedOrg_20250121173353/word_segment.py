'''
WordSegment class represents a segment of a word or phrase in the puzzle.
'''
class WordSegment:
    def __init__(self, segment):
        '''
        Initialize a word segment with the given text.
        :param segment: A string representing part of a word or phrase.
        '''
        self.segment = segment
    def __str__(self):
        '''
        Return the string representation of the word segment.
        :return: The segment as a string.
        '''
        return self.segment