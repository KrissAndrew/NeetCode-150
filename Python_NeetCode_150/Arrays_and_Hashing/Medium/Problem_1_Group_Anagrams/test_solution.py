import unittest
from .solutions import *

class TestGroupAnagrams(unittest.TestCase):

        test_cases = [
            ([[2,3,4,2,6,5], 1], []),
            ([[3, 3], 6], [0, 1]),
            ([[3, 2, 4], 6], [1, 2]),
            ([[2, 7, 11, 15], 9], [0, 1])
        ]
        
        def test_group_anagrams(self):
            print("\nRunning tests for 'Two Sum'")
            for list_target, expected in self.test_cases:
                with self.subTest(list_target=list_target):
                     self.assertEqual(group_anagrams(list_target[0], list_target[1]), expected)
                 

if __name__ == '__main__':
    unittest.main()
