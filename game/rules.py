import numpy as np


def do_move(board, move, player):
    '''Update the board according to the move and the player. If player 0 does
    the move, set the board cell to -1. If payer 1 makes the move, set the board cell 
    to 1 (empty board cells have value zero).
    
    Parameters
    ----------
    board: np.ndarray(N,N)
        a 2d numpy array representing the current game status. A board cell can 
        contain the following values:
        - -1: player 0 occupies this cell.
        - 0: empty cell
        - 1: player 1 occupies this cell
    move: tuple(int, int)
        the indices of the board cell to update.
    player: int
        the player who is making the move (can be 0 or 1)

    Returns
    -------
    board : the updated board
    '''    
    if player:
        board[move[0], move[1]] = 1
    else:
        board[move[0], move[1]] = -1

    return board


def game_over(board):
    '''Returns true when one of the players has won, i.e. there are 
    either three 'x's or three 'o's in a row on the board. 
    
    
    Parameters
    ----------
    board: np.ndarray(N,N)
        a 2d numpy array representing the current game status. A board cell can 
        contain the following values:
        - -1: player 0 occupies this cell.
        - 0: empty cell
        - 1: player 1 occupies this cell
    
    Returns
    -------
    game_is_over : boolean
        True when one of the players has one the game, False otherwise.
    '''
    diag_sum = np.trace(board)
    diag_sum_2 = np.trace(np.flip(board, 1))

    rowsum = board.sum(0)
    colsum = board.sum(1)

    if 3 in abs(rowsum) or 3 in abs(colsum):
        return True

    if abs(diag_sum) == 3 or abs(diag_sum_2) == 3:
        return True
    
    return False
