import unittest
from .solutions import *

class TestValidPalindrome(unittest.TestCase):
        
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
            ("123456", False),
            ("Not a palindrome!", False)
        ]
        
        def test_valid_palindrome(self):
            print("\nRunning tests for 'Valid Palindrome'")
            for idx, (string, expected) in enumerate(self.test_cases, start=1):
                with self.subTest(test=idx):
                    result = valid_palindrome(string)
                    self.assertEqual(
                        result, expected,
                        f"Test case {idx} failed: string={string}, expected={expected} but got {result}"
                    )

if __name__ == '__main__':
    unittest.main()
