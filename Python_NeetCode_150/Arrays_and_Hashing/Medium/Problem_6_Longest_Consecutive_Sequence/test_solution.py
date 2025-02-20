import unittest
from .solutions import *

class TestLongestConsecutiveSequence(unittest.TestCase):

        test_cases = [
             ([2,20,4,10,3,4,5], 4),
             ([0,3,2,5,4,6,1,1], 7),
        ]
    
        
        def test_longest_consecutive_sequence(self):
            print("\nRunning tests for 'Longest Consecutive Sequence'")
            for board, expected in self.test_cases:
                with self.subTest(board=board):
                     self.assertEqual(longest_consecutive_sequence(board), expected)

if __name__ == '__main__':
    unittest.main()
