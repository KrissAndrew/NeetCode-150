def valid_sudoku_blind(board: list[list[str]]) -> bool:
    for row in board:
        dotless_row = [i for i in row if i != '.' ]
        if len(set(dotless_row)) < len(dotless_row): return False
    
    columns = [[] for _ in range(9)]
    
    for i in range(len(board)):
        for j in range(len(board)):
            columns[j].append(board[i][j])

    for column in columns:
        dotless_col = [i for i in column if i != '.' ]
        if len(set(dotless_col)) < len(dotless_col): return False
    
    squares = [[] for _ in range(9)]
    for i in range(len(board)):
        for j in range(len(board)):
            if i <= 2:
                if j <= 2: squares[0].append(board[i][j])
                elif j <= 5: squares[1].append(board[i][j])
                elif j <= 8: squares[2].append(board[i][j])
            elif i <= 5:
                if j <= 2: squares[3].append(board[i][j])
                elif j <= 5: squares[4].append(board[i][j])
                elif j <= 8: squares[5].append(board[i][j])
            elif i <= 8:
                if j <= 2: squares[6].append(board[i][j])
                elif j <= 5: squares[7].append(board[i][j])
                elif j <= 8: squares[8].append(board[i][j])

    for square in squares:
        dotless_cube = [i for i in square if i != '.' ]
        if len(set(dotless_cube)) < len(dotless_cube): return False

    return True

# Improved version
# Define a function to verify valid groups as opposed to creating groups multiple times- exit early upon discovery
# 3x3 cube handling can be siplified using arithmetic to avoid if statements
def valid_sudoku(board: list[list[str]]) -> bool:
    def is_valid_group(group):
        group = [x for x in group if x != '.']
        return len(set(group)) == len(group)
    
    for row in board:
        if not is_valid_group(row):
            return False
    
    for col in zip(*board):
        if not is_valid_group(col): 
            return False
    
    # Check squares
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not is_valid_group(square): 
                for i in range(0, 9, 3):
                    print(square[i:i + 3])
                return False

    return True

