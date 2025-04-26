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
    num_Os = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == X:
                num_Xs += 1
            elif board[i][j] == O:
                num_Os += 1

    if num_Xs <= num_Os:
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
                actions_set.add((i, j))
    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # Check if action is valid 
    row_i = action[0]
    col_i = action[1]
    if row_i not in range(len(board)) or col_i not in range(len(board)) or board[action[0]][action[1]] != EMPTY:
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

    # Check horizontally and vertically
    for i in range(len(board)):
        hor_eq = True
        ver_eq = True
        first_el_hor = board[i][0]
        first_el_ver = board[0][i]
        for j in range(len(board)):
            if hor_eq and first_el_hor != board[i][j]:
                hor_eq = False
            if ver_eq and first_el_ver != board[j][i]:
                ver_eq = False
        if hor_eq and first_el_hor != EMPTY:
            return first_el_hor
        if ver_eq and first_el_ver != EMPTY:
            return first_el_ver

    # Check main diagonal
    m_diag_eq = True
    first_m_diag_el = board[0][0]
    for i in range(len(board)):
        if (first_m_diag_el) != board[i][i]:
            m_diag_eq = False
    if m_diag_eq and first_m_diag_el != EMPTY:
        return first_m_diag_el
    
    # Check other diagonal
    o_diag_eq = True
    first_o_diag_el = board[0][len(board)-1]   
    for i in range(len(board)):
        if (first_o_diag_el) != board[i][len(board)-1-i]:
            o_diag_eq = False
    if o_diag_eq and first_o_diag_el != EMPTY:
        return first_o_diag_el
            
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    # Check if someone won
    if (winner(board)):
        return True

    # Check if the board is filled
    filled = True
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] == EMPTY):
                filled = False
    if filled:
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    # Check if board is termal state
    if terminal(board):
        return None
    
    else:  

        # Get all possible actions
        pos_actions = list(actions(board))

        if (player(board)) == X:
            action_vals = []
            for action in pos_actions:
                action_vals.append(min_value(result(board, action)))
            return pos_actions[action_vals.index(max(action_vals))]
        else:
            action_vals = []
            for action in pos_actions:
                action_vals.append(max_value(result(board, action)))
            return pos_actions[action_vals.index(min(action_vals))]


def max_value(board):
    v = float('-inf')
    if (terminal(board)):
        return utility(board)
    else:
        # Get all possible actions
        pos_actions = actions(board)
        for action in pos_actions:
            v = max(v, min_value(result(board, action)))
        return v


def min_value(board):
    v = float('inf')
    if (terminal(board)):
        return utility(board)
    else:
        # Get all possible actions
        pos_actions = actions(board)
        for action in pos_actions:
            v = min(v, max_value(result(board, action)))
        return v