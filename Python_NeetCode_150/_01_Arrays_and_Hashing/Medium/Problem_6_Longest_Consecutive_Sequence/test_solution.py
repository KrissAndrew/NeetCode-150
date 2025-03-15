import unittest
from .solutions import *

class TestLongestConsecutiveSequence(unittest.TestCase):

        test_cases = [
             ([2,20,4,10,3,4,5], 4),
             ([0,3,2,5,4,6,1,1], 7),
             ([0], 1),
             ([0, 2], 1),
             ([], 0)
        ]
    
        def test_longest_consecutive_sequence(self):
            print("\nRunning tests for 'Longest Consecutive Sequence'")
            for idx, (numbers, expected) in enumerate(self.test_cases, start=1):
                with self.subTest(test=idx):
                    result = longest_consecutive_sequence(numbers)
                    self.assertEqual(
                        result, expected,
                        f"Test case {idx} failed: numbers={numbers}, expected={expected} but got {result}"
                    )
if __name__ == '__main__':
    unittest.main()
