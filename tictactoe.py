"""
Tic Tac Toe Player
"""

import math
import copy


# Defining players and value of EMPTY
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    3x3 matrix with all the positions empty.
    Initial board
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    If there are more Xs on board than Os, next move should be done by O.
    Otherwise, the next move belongs to X.
    """
    x_count =sum(row.count(X) for row in board) # Finding the number of X's on board
    o_count =  sum(row.count(O) for row in board) # Finding number of O's on board
    return O if x_count > o_count else X 
    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    An action is a tuple (i, j) where 'i' is the row and 'j' is the column.
    Only returns empty spaces where a move can be made.
    """
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}
    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    The move is made by the current player, and the function returns a new board
    with the updated move.
    """
    i, j = action
    if board[i][j] is not EMPTY:
        raise ValueError("Invalid action: cell already occupied.") # Ensures the move is valid

    new_board = copy.deepcopy(board) # Creating new version of board for not modifying original board
    current_player = player(board) # Calling player() function to determine which player should play next and marking returned value as current_player
    new_board[i][j] = current_player # Marking the player's selected cell with player's sign
    return new_board
    # raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    Checks all rows, columns, and diagonals for three of the same symbol (X or O).
    For rows and columns i is iterared 3 times as the board is 3x3 matrix.
    For diagonals iterating over 3 is not needed as there are only 2 diagonals on board.
    """

    # Checking rows to determine if there is a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not EMPTY:
            return board[i][0]

    # Checking columns to determine if there is a winner
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not EMPTY:
            return board[0][i]
    
    # Checking diagonals to detemine if there is a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]

    # Returning None in case none of the previous cases are valid -> No winner yet
    return None

    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    The game is over if there winner() function returns a winner or if all the cells on board are marked(board is full).
    """
    return winner(board) is not None or all(cell is not EMPTY for row in board for cell in row)
    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    These values are used for minmax algorithm.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    return 0 # If the game ends as tie
    # raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    Minimax algorithm checks and evaluates all of the possible future steps on the game and
    determines the best action(move) for the current player
    """
    if terminal(board):
        return None # If the game is already ended, then there is no optimal move

    current_player = player(board) # Calling player() function to determine the player

    if current_player == X:
        _, best_action = max_value(board) # Calling max_value() function for X as we define X as maximizing its score
    else:
        _, best_action = min_value(board) # Calling min_value() function for O as we define O as minimizing its score

    return best_action
    # raise NotImplementedError

def max_value(board):
    """
    Recursive function that returns the maximum possible utility for player X.
    This function is called in the minimax algorithm when it is player X's turn to play.
    """
    if terminal(board):
        return utility(board), None # If the game is already ended, just returning the utility, no need to return best_action as there is none
    
    value = -math.inf # Initializing value to be smallest possible value by assigning its value as negative infinity
    best_action = None
    for action in actions(board):
        min_val, _ = min_value(result(board, action)) # Evaluating the results of current move by finding how other player would play after this move
        if min_val > value: # Update the best_action if new value is better
            value = min_val
            best_action = action
    return value, best_action # Returning the best value and the best_action

def min_value(board):
    """
    Recursive function that returns the minimum possible utility for player O.
    This function is called in the minimax algorithm when it is player O's turn to play.
    """
    if terminal(board):
        return utility(board), None # If the game is already ended, just returning the utility, no need to return best_action as there is none
    
    value = math.inf # Initializing value to be largest possible value by assigning its value as positive infinity
    best_action = None
    for action in actions(board):
        max_val, _ = max_value(result(board, action)) # Evaluating the results of current move by finding how other player would play after this move
        if max_val < value: # Update the best_action if new value is better
            value = max_val
            best_action = action
    return value, best_action # Returning the best value and the best_action