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