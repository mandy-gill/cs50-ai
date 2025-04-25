"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None

num_moves_played = 0


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
    
    # Get number of Xs on the board
    num_Xs = 0
    for i in len(board):
        for j in len(board[i]):
            if board[i][j] == X:
                num_Xs += 1

    if num_Xs % 2 == 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                actions_set.add((i,j))
    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # Check if action is valid 
    if board[action[0]][action[1]] != EMPTY:
        raise Exception("Invalid action.")

    # Make a deep copy of the board
    board_copy = []
    for i in range(len(board)):
        row = []
        for j in range(len(board[i])):
            row.append(board[i][j])
        board_copy.append(row)

    # Get the player whose turn it is
    player_turn = player(board)

    # Add the player's mark on the deep copy of the board
    board_copy[action[0]][action[1]] = player_turn

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    win_player = None
    
    # Check horizontally
    all_equal = True
    for i in range(len(board)):
        first = board[i][0]
        for j in range(len(board[i])):
            if first != board[i][j]:
                all_equal = False
        if all_equal:
            win_player = first
            return win_player

    # Check vertically
    all_equal = True
    for i in range(len(board)):
        first = board[i][0]
        for j in range(len(board[i])):
            if first != board[j][i]:
                all_equal = False
        if all_equal:
            win_player = first
            return win_player

    # Check main diagonal
    all_equal = True
    first = board[i][0]
    for i in range(len(board)):
        if (first) != board[i][i]:
            all_equal = False
    if all_equal:
        win_player = first
        return win_player
    
    # Check other diagonal
            

    return win_player


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
