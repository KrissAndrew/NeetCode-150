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
            for idx, (numbers, expected) in enumerate(self.test_cases, start=1):
                with self.subTest(test=idx):
                    result = contains_duplicate(numbers)
                    self.assertEqual(
                        result, expected,
                        f"Test case {idx} failed: numbers={numbers}, expected={expected} but got {result}"
                    )

if __name__ == '__main__':
    unittest.main()