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
            for int_list, expected in self.test_cases:
                with self.subTest(int_list=int_list):
                     self.assertEqual(product_except_self(int_list), expected)

if __name__ == '__main__':
    unittest.main()
