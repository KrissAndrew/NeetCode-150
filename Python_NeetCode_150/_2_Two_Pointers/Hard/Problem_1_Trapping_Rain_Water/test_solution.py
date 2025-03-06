import unittest
from .solutions import *

class TestContainerWithMostWater(unittest.TestCase):
        
    test_cases = [
        # Basic test cases:
        ([1,7,2,5,4,7,3,6], 36),                 # 1: Standard example with two valid triplets.
        ([2,2,2], 4),                            # 2: Multiple zeros produce a single triplet.
    ]



    def test_container_with_most_water(self):
        print("\nRunning tests for 'Three Sum'")
        for idx, (numbers, expected) in enumerate(self.test_cases, start=1):
            with self.subTest(test=idx):
                result = max_container(numbers)
                self.assertEqual(
                    result, expected,
                    f"Test case {idx} failed: numbers={numbers}, expected={expected} but got {result}"
                )

if __name__ == '__main__':
    unittest.main()
