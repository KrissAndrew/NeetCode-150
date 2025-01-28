import unittest
from .solutions import *

class TestMostFrequentElements(unittest.TestCase):

        test_cases = [
            (([1, 1, 1], 1), [1]),
            (([1, 1, 2], 1), [1]),
            (([1, 1, 2, 2], 1), [1]),
            (([1, 1, 2, 2], 2), [1, 2]),
            (([], 1), []),
        ]
        
        def test_most_frequent_elements(self):
            print("\nRunning tests for 'Most Frequent Elements'")
            for arguments, expected in self.test_cases:
                with self.subTest(arguments=arguments):
                     self.assertEqual(most_frequent_elements(arguments[0], arguments[1]), expected)
                 

if __name__ == '__main__':
    unittest.main()
