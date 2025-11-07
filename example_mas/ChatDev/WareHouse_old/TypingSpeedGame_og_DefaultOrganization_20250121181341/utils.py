'''
Utility functions for the typing practice game.
'''
def load_words():
    with open("words.txt", "r") as file:
        words = file.read().splitlines()
    return words
def calculate_wpm(correct_words, elapsed_time):
    minutes = elapsed_time / 60
    wpm = correct_words / minutes
    return round(wpm, 2)
def calculate_accuracy(typed_words, correct_words):
    total_words = len(typed_words)
    if total_words == 0:
        return 0
    accuracy = (correct_words / total_words) * 100
    return round(accuracy, 2)