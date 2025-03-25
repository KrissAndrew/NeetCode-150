import unittest
from .solutions import permutation_in_string

class TestPermutationInString(unittest.TestCase):

    test_cases = [
        (("a", "a"), True),             #  1 - 'a' is a permutation of 'a'
        (("a", "ab"), True),            #  2 - 'a' is a permutation of '(a)b'
        (("ab", "ba"), True),            #  3 - 'ab' is a permutation of '(ba)'
        (("cb", "abc"), True),          #  3 - 'cb' is a permutation of 'a(bc)'
        (("adc", "dcda"), True),        #  4 - 'adc' is a permutation of 'd(cda)'
        (("abc", "lecabee"), True),     #  5 - 'abc' is a permutation of 'le(cab)ee'
        (("abc", "lecaabee"), False), #  6 - 'abc' is not a permutation of 'lecaabee'
    ]

    def test_longest_repeat_char_replacement(self):
        print("\nRunning tests for 'Best Time to Buy and Sell Stock'")
        for idx, (input, expected) in enumerate(self.test_cases, start=1):
            with self.subTest(test=idx):
                result = permutation_in_string(*input)
                self.assertEqual(
                    result, expected,
                    f"Test case {idx} failed: input={input}, expected={expected} but got {result}"
                )

if __name__ == '__main__':
    unittest.main()
