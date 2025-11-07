import unittest
from morse_code import translate
class TestMorseCode(unittest.TestCase):
    def test_translate_text_to_morse_code(self):
        text = "Hello, World!"
        morse_code = translate(text)
        self.assertEqual(morse_code, ".... . .-.. .-.. --- .-- --- .-. .-.. -..")
    def test_translate_morse_code_to_text(self):
        morse_code = ".... . .-.. .-.. --- .-- --- .-. .-.. -.."
        text = translate(morse_code)
        self.assertEqual(text, "Hello, World!")
if __name__ == "__main__":
    unittest.main()