import unittest
from .solutions import *

class TestValidAnagram(unittest.TestCase):
        
        test_cases = [
            (["dog", "god"], True),
            (["DOG", "god"], True),
            (["Dogg", "God"], False),
            (["rat", "car"], False),
            (["hello", "bello"], False)
        ]
        
        def test_contains_duplicate(self):
            print("\nRunning tests for 'Valid Anagram'")
            for words, expected in self.test_cases:
                with self.subTest(words=words):
                     self.assertEqual(valid_anagram(words[0], words[1]), expected)
                 


if __name__ == '__main__':
    unittest.main()
