import unittest
from .solutions import longest_non_repeat_substring

class TestNonRepeatSub(unittest.TestCase):

    test_cases = [
        ("abcabcbb", 3), #  1
        ("zxyzxyz", 3),  #  2
        ("xxxx", 1),     #  3
        ("aabbcc", 2),   #  4
        ("abcabcbb", 3), #  5
        ("au", 2),       #  6
        ("aab", 2),      #  7
    ]

    def test_longest_non_repeat_substring(self):
        print("\nRunning tests for 'Best Time to Buy and Sell Stock'")
        for idx, (input, expected) in enumerate(self.test_cases, start=1):
            with self.subTest(test=idx):
                result = longest_non_repeat_substring(input)
                self.assertEqual(
                    result, expected,
                    f"Test case {idx} failed: input={input}, expected={expected} but got {result}"
                )

if __name__ == '__main__':
    unittest.main()
