import unittest
from .solutions import *

class TestContainsDulpicate(unittest.TestCase):
        
        test_cases = [
             ([1, 2, 3, 4], False),
             ([1, 2, 3, 4, 1], True),
             ([1], False),
             ([], False),
             ([1, 1, 1], True),
        ]
        
        def test_contains_duplicate(self):
            print("\nRunning tests for 'Contains Duplicate'")
            for nums, expected in self.test_cases:
                 with self.subTest(nums=nums):
                     self.assertEqual(contains_duplicate(nums), expected)

if __name__ == '__main__':
    unittest.main()