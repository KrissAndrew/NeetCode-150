import unittest
from .solutions import *

class TestValidAnagram(unittest.TestCase):
        
        test_cases = [
            ("dog", "god", True),
            ("DOG", "god", True),
            ("Dogg", "God", False),
            ("rat", "car", False),
            ("hello", "bello", False)
        ]
        
        def test_valid_anagram(self):
            print("\nRunning tests for 'Valid Anagram'")
            for idx, (string1, string2, expected) in enumerate(self.test_cases, start=1):
                with self.subTest(test=idx):
                    result = valid_anagram(string1, string2)
                    self.assertEqual(
                        result, expected,
                        f"Test case {idx} failed: string1={string1}, string2={string2}, expected={expected} but got {result}"
                    )

if __name__ == '__main__':
    unittest.main()
