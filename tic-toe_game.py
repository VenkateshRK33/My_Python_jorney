def tic_tac_toe_game(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] in ("X","O"):
            return row[O]
        
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] in ("X","O"):
            return board[0][col]
        
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] in ("X","O"):
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board [0][2] in ("X","O"):
        return board[0][2]