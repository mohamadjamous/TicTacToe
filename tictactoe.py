"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    
    # counters
    x_count = 0
    o_count = 0

    for row in board:
        for cell in row:
            if cell == "X":
                x_count += 1
            elif cell == "O":
                o_count += 1
             
             
    if x_count == 1 and o_count == 0:
        return O
    elif x_count == o_count:
        return X
    elif x_count > o_count:
        return O
    else:
        return X              
    
    
    return player_value


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    result = set()
    
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == None:
                result.add((i, j))

    
    return result


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action

    if not (0 <= i < len(board) and 0 <= j < len(board[i])) or board[i][j] is not None:
        raise Exception("Invalid move")

    newBoard = [row.copy() for row in board]

    if player(board) == X:
        newBoard[i][j] = "X"
    else:
        newBoard[i][j] = "O"
    
    return newBoard



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for row in board:
        if row[0] is not None and row[0] == row[1] == row[2]:
            return row[0]
    
    for i in range(3):
        if board[0][i] is not None and board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    
    if board[0][0] is not None and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    
    if board[0][2] is not None and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    if winner(board) is not None:
        return True

    for row in board:
        for cell in row:
            if cell is None:
                return False
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    if terminal(board): 
        return None
    
    current_player = player(board)

    if current_player == "X":
        best_action = None
        best_value = float('-inf')

        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_action = action
        
        return best_action

    else: 
        best_action = None
        best_value = float('inf')

        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_action = action
        
        return best_action


def max_value(board):
    
    if terminal(board):
        return utility(board)

    v = float('-inf')

    for action in actions(board):
        v = max(v, min_value(result(board, action)))

    return v


def min_value(board):
    
    if terminal(board):
        return utility(board)

    v = float('inf')

    for action in actions(board):
        v = min(v, max_value(result(board, action)))

    return v





