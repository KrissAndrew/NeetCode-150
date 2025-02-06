import unittest
from .solutions import *

class TestValidSudoku(unittest.TestCase):

        test_cases = [
            ([["1","2",".",".","3",".",".",".","."],
              ["4",".",".","5",".",".",".",".","."],
              [".","9","8",".",".",".",".",".","3"],
              ["5",".",".",".","6",".",".",".","4"],
              [".",".",".","8",".","3",".",".","5"],
              ["7",".",".",".","2",".",".",".","6"],
              [".",".",".",".",".",".","2",".","."],
              [".",".",".","4","1","9",".",".","8"],
              [".",".",".",".","8",".",".","7","9"]], True),
            ([["1","2","1",".","3",".",".",".","."],
              ["4",".",".","5",".",".",".",".","."],
              [".","9","1",".",".",".",".",".","3"],
              ["5",".",".",".","6",".",".",".","4"],
              [".",".",".","8",".","3",".",".","5"],
              ["7",".",".",".","2",".",".",".","6"],
              [".",".",".",".",".",".","2",".","."],
              [".",".",".","4","1","9",".",".","8"],
              [".",".",".",".","8",".",".","7","9"]], False),
            ([["1","2","1",".","3",".",".",".","."],
              ["4","1",".","5",".",".",".",".","."],
              [".","9","1",".",".",".",".",".","3"],
              ["5",".",".",".","6",".",".",".","4"],
              [".",".",".","8",".","3",".",".","5"],
              ["7",".",".",".","2",".",".",".","6"],
              [".",".",".",".",".",".","2",".","."],
              [".",".",".","4","1","9",".",".","8"],
              [".",".",".",".","8",".",".","7","9"]], False),
            ([[".",".",".",".",".",".",".",".","."],
              [".",".",".",".",".",".",".",".","."],
              [".",".",".",".",".",".",".",".","."],
              [".",".",".",".",".",".",".",".","."],
              [".",".",".",".",".",".",".",".","."],
              [".",".",".",".",".",".",".",".","."],
              [".",".",".",".",".",".",".",".","."],
              [".",".",".",".",".",".",".",".","."],
              [".",".",".",".",".",".",".",".","."]], True),
        ]
    
        
        def test_valid_sudoku(self):
            print("\nRunning tests for 'Valid Sudoku'")
            for board, expected in self.test_cases:
                with self.subTest(board=board):
                     self.assertEqual(valid_sudoku_blind(board), expected)

if __name__ == '__main__':
    unittest.main()
