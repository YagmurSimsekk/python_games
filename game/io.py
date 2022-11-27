def to_integer_tuple(input_value):
    '''Validate the input string to extract a tuple of integers.
    
    Parameters
    ----------
    input_value : string
        The user input

    Returns
    -------
    int_list : list(int)
        the input as a list of integers
    '''
    int_list = [int(char) for char in input_value.split()]

    if len(int_list) != 2:
        raise ValueError
    
    return int_list


def _cell_to_char(cell):
    '''returns board cell to appropriate character'''
    if cell == -1:
        return 'x'
    if cell == 1:
        return 'o'
    return ' '


def print_board(board):
    '''Convert the board to string and print it.
    
    Parameters
    ----------
    board: np.ndarray(N,N)
        a 2d numpy array representing the current game status. A board cell can 
        contain the following values:
        - -1: player 0 occupies this cell.
        - 0: empty cell
        - 1: player 1 occupies this cell
    '''
    board_as_string = ''
    delimiter = '|'
    vertical_delimiter = '\n-------\n'
    board_as_string += vertical_delimiter
    for row in board:
        board_as_string += delimiter
        for item in  row:
            board_as_string += _cell_to_char(item) + delimiter
        board_as_string += vertical_delimiter
    print(board_as_string)
    