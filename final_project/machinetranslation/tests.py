import unittest
from translator import english_to_french
from translator import french_to_english

class TestTranslator(unittest.TestCase):

    def test_english_to_french_translation(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('Good bye'), 'Au revoir')
    
    def test_french_to_english_translation(self):
        self.assertEqual(french_to_english('Hello'), 'Bonjour')
        self.assertEqual(french_to_english('Good bye'), 'Au revoir')

if __name__ == '__main__':
    unittest.main()
