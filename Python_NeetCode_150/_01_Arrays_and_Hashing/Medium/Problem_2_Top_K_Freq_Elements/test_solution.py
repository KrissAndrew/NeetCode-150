import unittest
from .solutions import *

class TestMostFrequentElements(unittest.TestCase):

        test_cases = [
            ([1, 1, 1], 1, [1]),
            ([1, 1, 2], 1, [1]),
            ([1, 1, 2, 2], 1, [1]),
            ([1, 1, 2, 2], 2, [1, 2]),
            ([], 1, []),
        ]
        
        def test_most_frequent_elements(self):
            print("\nRunning tests for 'Most Frequent Elements'")
            for idx, (numbers, element_count, expected) in enumerate(self.test_cases, start=1):
                with self.subTest(test=idx):
                    result = most_frequent_elements(numbers, element_count)
                    self.assertEqual(
                        result, expected,
                        f"Test case {idx} failed: numbers={numbers}, element_count={element_count}, expected={expected} but got {result}"
                    )

if __name__ == '__main__':
    unittest.main()
