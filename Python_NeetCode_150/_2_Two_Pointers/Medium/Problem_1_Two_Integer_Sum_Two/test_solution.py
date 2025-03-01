import unittest
from .solutions import *

class TestTwoSum(unittest.TestCase):
        
    test_cases = [
        # Basic test cases:
        ([2, 7, 11, 15], 9, [1, 2]),          # 1 - 2 + 7 = 9, so one-indexed indices [1, 2]
        ([2, 3, 4], 6, [1, 3]),               # 2 - 2 + 4 = 6, indices [1, 3]
        ([0, 0, 3, 4], 0, [1, 2]),            # 3 - 0 + 0 = 0, indices [1, 2]
        
        # Cases with negative numbers:
        ([-3, -1, 0, 1, 2, 4, 5], 1, [1, 6]),  # 4 - -3 + 4 = 1, indices [2, 5]
        
        # Case with duplicates:
        ([1, 2, 3, 4, 4, 9, 56, 90], 8, [4, 5]), # 5 - 4 + 4 = 8, indices [4, 5]
        
        # Another basic test:
        ([5, 25, 75], 100, [2, 3]),           # 6 - 25 + 75 = 100, indices [2, 3]
        
        # No solution exists:
        ([1, 2, 3], 10, []),                  # 7 - No two numbers add up to 10.
    ]
        
    def test_two_sum_two(self):
        print("\nRunning tests for 'Two Sum Two (ascending list)'")
        for idx, (numbers, target, expected) in enumerate(self.test_cases, start=1):
            with self.subTest(test=idx):
                result = two_sum(numbers, target)
                self.assertEqual(
                    result, expected,
                    f"Test case {idx} failed: numbers={numbers}, target={target}, expected={expected} but got {result}"
                )

if __name__ == '__main__':
    unittest.main()
