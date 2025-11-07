'''
Utility module for handling text translation using the googletrans library.
'''
from googletrans import Translator
def translate(text, target_language):
    '''
    Translate the given text to the specified target language.
    :param text: The text to translate.
    :param target_language: The language code to translate the text into.
    :return: Translated text.
    '''
    translator = Translator()
    try:
        result = translator.translate(text, dest=target_language)
        return result.text
    except Exception as e:
        raise RuntimeError("Translation failed. Please check your network connection or try again later.") from e