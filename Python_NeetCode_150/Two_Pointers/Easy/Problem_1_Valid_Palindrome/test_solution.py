import unittest
from .solutions import *

class TestValidAnagram(unittest.TestCase):
        
        test_cases = [
            # Edge cases:
            ("", True),                                # Empty string is a palindrome.
            ("a", True),                               # Single character is always a palindrome.
            ("     ", True),                           # Only spaces (cleaned becomes empty) → palindrome.
            (",.!?", True),                            # Only non-alphanumeric characters → cleaned to empty → palindrome.

            # Basic palindromes:
            ("racecar", True),
            ("RaceCar", True),                         # Case-insensitive check.
            ("12321", True),                           # Numeric palindrome.

            # Complex palindromes with punctuation and spaces:
            ("A man, a plan, a canal: Panama", True),
            ("Madam, in Eden, I'm Adam", True),
            ("No 'x' in Nixon", True),
            ("Was it a car or a cat I saw?", True),

            # Non-palindromes:
            ("hello", False),
            ("123456", False),~~
            ("Not a palindrome!", False)
        ]
        
        def test_contains_duplicate(self):
            print("\nRunning tests for 'Valid Palindrome'")
            for word, expected in self.test_cases:
                with self.subTest(word=word):
                     self.assertEqual(valid_palindrome(word), expected)
                 


if __name__ == '__main__':
    unittest.main()
