import unittest
from translator import french_to_english
from translator import english_to_french

class Test_e2f(unittest.TestCase):
    def test_e2f1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    def test_e2f2(self):
        self.assertEqual(english_to_french('How are you?'), 'Comment es-tu?')
    def test_e2f3(self):
        self.assertEqual(english_to_french('Good evening!'), 'Bonsoir !')
    def test_e2f4(self):
        self.assertNotEqual(english_to_french('None'), '')


class Test_f2e(unittest.TestCase):
    def test_f2e1(self):
        self.assertEqual(french_to_english('Bonjour !'), 'Hello!')
    def test_f2e2(self):
        self.assertEqual(french_to_english('Comment es-tu?'), 'How are you?')
    def test_f2e3(self):
        self.assertEqual(french_to_english('Bonsoir !'), 'Good evening.')
    def test_f2e4(self):
        self.assertNotEqual(french_to_english('None'), '')

unittest.main()
