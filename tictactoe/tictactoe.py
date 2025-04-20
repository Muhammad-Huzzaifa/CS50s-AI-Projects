"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

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
    return X if sum(row.count(X) for row in board) == sum(row.count(O) for row in board) else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] is EMPTY}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError("Invalid action")
    board = deepcopy(board)
    board[action[0]][action[1]] = player(board)
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if any(all(cell == X for cell in row) for row in board) or \
            any(all(board[i][j] == X for i in range(3)) for j in range(3)) or \
            all(board[i][i] == X for i in range(3)) or \
            all(board[i][2-i] == X for i in range(3)):
        return X
    
    elif any(all(cell == O for cell in row) for row in board) or \
            any(all(board[i][j] == O for i in range(3)) for j in range(3)) or \
            all(board[i][i] == O for i in range(3)) or \
            all(board[i][2-i] == O for i in range(3)):
        return O
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or all(cell is not EMPTY for row in board for cell in row)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    return 1 if winner(board) == X else -1 if winner(board) == O else 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(board, alpha, beta):
        if terminal(board):
            return utility(board), None
        best_value = -math.inf
        best_action = None
        for action in actions(board):
            value, _ = min_value(result(board, action), alpha, beta)
            if value > best_value:
                best_value = value
                best_action = action
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return best_value, best_action
    
    def min_value(board, alpha, beta):
        if terminal(board):
            return utility(board), None
        best_value = math.inf
        best_action = None
        for action in actions(board):
            value, _ = max_value(result(board, action), alpha, beta)
            if value < best_value:
                best_value = value
                best_action = action
            beta = min(beta, value)
            if alpha >= beta:
                break
        return best_value, best_action
    
    player_turn = player(board)
    if player_turn == X:
        _, action = max_value(board, -math.inf, math.inf)
    else:
        _, action = min_value(board, -math.inf, math.inf)
    return action