import unittest
from .solutions import *

class TestTwoSum(unittest.TestCase):

        test_cases = [
            ([2,3,4,2,6,5], 1, []),
            ([3, 3], 6, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([2, 7, 11, 15], 9, [0, 1])
        ]
        
        def test_two_sum_one(self):
            print("\nRunning tests for 'Two Sum One (unsorted)'")
            for idx, (numbers, target, expected) in enumerate(self.test_cases, start=1):
                with self.subTest(test=idx):
                    result = two_sum(numbers, target)
                    self.assertEqual(
                        result, expected,
                        f"Test case {idx} failed: numbers={numbers}, target={target}, expected={expected} but got {result}"
                    )

if __name__ == '__main__':
    unittest.main()
