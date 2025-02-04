from typing import List

def valid_sudoku_blind(board: List[List[str]]) -> bool:
    for row in board:
        dotless_row = [i for i in row if i != '.' ]
        if len(set(dotless_row)) < len(dotless_row): return False
    
    columns = [[] for _ in range(9)]
    
    for i in range(len(board)):
        for j in range(len(board)):
            columns[j].append(board[i][j])
    
    cubes = [[] for _ in range(9)]
    # for i in range(3):

        


    
    return True

if __name__ == "__main__":
    true_board =   [["1","2",".",".","3",".",".",".","."],
                    ["4",".",".","5",".",".",".",".","."],
                    [".","9","8",".",".",".",".",".","3"],
                    ["5",".",".",".","6",".",".",".","4"],
                    [".",".",".","8",".","3",".",".","5"],
                    ["7",".",".",".","2",".",".",".","6"],
                    [".",".",".",".",".",".","2",".","."],
                    [".",".",".","4","1","9",".",".","8"],
                    [".",".",".",".","8",".",".","7","9"]]
    
    false_board =  [["1","2","1",".","3",".",".",".","."],
                    ["4",".",".","5",".",".",".",".","."],
                    [".","9","1",".",".",".",".",".","3"],
                    ["5",".",".",".","6",".",".",".","4"],
                    [".",".",".","8",".","3",".",".","5"],
                    ["7",".",".",".","2",".",".",".","6"],
                    [".",".",".",".",".",".","2",".","."],
                    [".",".",".","4","1","9",".",".","8"],
                    [".",".",".",".","8",".",".","7","9"]]
    
    print("Result of true_board: " + ("True" if valid_sudoku_blind(true_board) else "False"))
    print("Result of false_board: " + ("True" if valid_sudoku_blind(false_board) else "False"))
