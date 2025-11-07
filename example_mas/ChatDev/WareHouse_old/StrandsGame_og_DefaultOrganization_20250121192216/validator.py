'''
Defines the StrandsValidator class for validating strand combinations.
'''
class StrandsValidator:
    def __init__(self, valid_words):
        self.valid_words = set(valid_words)
    def is_valid(self, text):
        # Check if the text can be segmented into valid words
        return self.can_segment(text)
    def can_segment(self, text):
        # Dynamic programming approach to check if the text can be segmented
        n = len(text)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and text[j:i] in self.valid_words:
                    dp[i] = True
                    break
        return dp[n]