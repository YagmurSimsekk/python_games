import numpy as np
import game.rules as rules
import game.io as io


def play_tic_tac_toe():
    
    board = np.zeros([3, 3])

    # Player number is either zero or 1
    player = 0


    # Repeat until one of the players has won...
    while (not rules.game_over(board)):

        # Request current player to input a move
        move = input(f"player {player}'s move. Enter row and column index.\n")

        # validate the input 
        try:
            move = io.to_integer_tuple(move) 
        except:
            print('Invalid input. Enter a row and column index as two numbers separated by a space.')
            continue;
        
        # if we have arrived here, the input is valid! We can try to execute the move
        board = rules.do_move(board, move, player)
        
        # switch players
        player = 1 - player

        io.print_board(board)

    print(f'Game over! Player {1 - player} has won the game!')
