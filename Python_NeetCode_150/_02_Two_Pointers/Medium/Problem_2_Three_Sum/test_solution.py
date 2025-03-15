import unittest
from .solutions import *

class TestThreeSum(unittest.TestCase):
        
    test_cases = [
        # Basic test cases:
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),     # 1: Standard example with two valid triplets.
        ([0, 0, 0, 0], [[0, 0, 0]]),                            # 2: Multiple zeros produce a single triplet.
        ([1, 2, 3], []),                                        # 3: No triplet exists that sums to 0.
        ([], []),                                               # 4: Empty list.
        ([1, 2], []),                                           # 5: List with fewer than 3 elements.
        
        # Additional test cases:
        ([-2, 0, 0, 2, 2], [[-2, 0, 2]]),                       # 6: Mixed negatives and positives.
        ([-1, -1, 0, 1, 1], [[-1, 0, 1]]),                      # 7: Duplicate numbers yielding one unique triplet.
    ]
        
    def test_three_sum(self):
        print("\nRunning tests for 'Three Sum'")
        for idx, (numbers, expected) in enumerate(self.test_cases, start=1):
            with self.subTest(test=idx):
                result = three_sum(numbers)
                self.assertEqual(
                    result, expected,
                    f"Test case {idx} failed: numbers={numbers}, expected={expected} but got {result}"
                )

if __name__ == '__main__':
    unittest.main()
