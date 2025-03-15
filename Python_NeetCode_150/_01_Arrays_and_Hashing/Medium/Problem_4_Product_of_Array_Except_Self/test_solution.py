import unittest
from .solutions import *

class TestProductofArrayExceptSelf(unittest.TestCase):

        test_cases = [
            ([1,2,4,6], [48,24,12,8]),
            ([0, 0, 0, 0], [0, 0, 0, 0]),
            ([10, 10, 10, 10], [1000, 1000, 1000, 1000]),
        ]
        
        def test_product_of_array_except_self(self):
            print("\nRunning tests for 'Product of Array Except Self'")
            for idx, (numbers, expected) in enumerate(self.test_cases, start=1):
                with self.subTest(test=idx):
                    result = product_except_self(numbers)
                    self.assertEqual(
                        result, expected,
                        f"Test case {idx} failed: numbers={numbers}, expected={expected} but got {result}"
                    )

if __name__ == '__main__':
    unittest.main()
