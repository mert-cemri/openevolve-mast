'''
Contains utility functions for calculating WPM and accuracy.
'''
def calculate_wpm(user_input, elapsed_time):
    '''
    Calculates the words per minute (WPM) based on the user input and elapsed time.
    Handles the edge case where elapsed_time is zero to avoid division by zero.
    '''
    words = user_input.split()
    num_words = len(words)
    if elapsed_time == 0:
        wpm = 0  # Return 0 WPM if no time has elapsed
    else:
        wpm = (num_words / elapsed_time) * 60
    return wpm
def calculate_accuracy(user_input, paragraph):
    '''
    Calculates the accuracy of the user input compared to the original paragraph.
    Handles cases where the user input is longer than the paragraph.
    '''
    user_words = user_input.split()
    paragraph_words = paragraph.split()
    correct_words = 0
    for i in range(min(len(user_words), len(paragraph_words))):
        if user_words[i] == paragraph_words[i]:
            correct_words += 1
    accuracy = (correct_words / len(paragraph_words)) * 100 if paragraph_words else 0
    return accuracy