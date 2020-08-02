# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tools import clear_screen
from tools import sleep

board_template = '''
-{}-|-{}-|-{}-
-{}-|-{}-|-{}-
-{}-|-{}-|-{}-
'''

board_current = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
players = ('Player 1', 'Player 2')
symbols = {0: 'X', 1: 'O'}
turn_player_index = 0

exit_game = False


def new_game():
    print('***********  Starting new game ******************')


def print_board():
    clear_screen()
    print(board_template.format(board_current[0][0], board_current[0][1], board_current[0][2], board_current[1][0],
                                board_current[1][1],
                                board_current[1][2], board_current[2][0], board_current[2][1], board_current[2][2]))
    print('Turn is on: {}. Symbol is: {}'.format(players[turn_player_index], symbols[turn_player_index]))


def validate_numeric_input(string_to_validate):
    if str(string_to_validate).isdecimal():
        int_value = int(string_to_validate)
        if 1 <= int_value <= 9:
            return True
    return False


def ask_for_input():
    input_is_valid = False
    while not input_is_valid:
        print('E to exit')
        cell = input('All right {}. Cell you select (1 to 9) :'.format(players[turn_player_index]))
        if cell == 'E':
            exit(0)
        input_is_valid = validate_numeric_input(cell)
        if not input_is_valid:
            print('{} is not a valid input. Must be 1 to 9'.format(cell))
    return int(cell)


def switch_user_turn():
    global turn_player_index
    if turn_player_index == 0:
        turn_player_index = 1
    else:
        turn_player_index = 0


def get_indexes_from_location(cell):
    if cell in [1, 4, 7]:
        column_index = 0
    elif cell in [2, 5, 8]:
        column_index = 1
    else:
        column_index = 2

    if cell in [7, 8, 9]:
        row_index = 0
    elif cell in [4, 5, 6]:
        row_index = 1
    else:
        row_index = 2

    return [row_index, column_index]


def validate_board_location_available(cell, board):
    indexes = get_indexes_from_location(cell)
    if board[indexes[0]][indexes[1]] == '-':
        return True
    print('Cell is occupied. Pick another one')
    return False


def check_row_for_endgame(cell, board):
    indexes = get_indexes_from_location(cell)
    current_symbol = symbols[turn_player_index]
    if board[indexes[0]][0] == board[indexes[0]][1] == board[indexes[0]][2] == current_symbol:
        return True
    return False


def check_column_for_endgame(cell, board):
    indexes = get_indexes_from_location(cell)
    current_symbol = symbols[turn_player_index]
    if board[0][indexes[1]] == board[1][indexes[1]] == board[2][indexes[1]] == current_symbol:
        return True
    return False


def check_diagonals_for_endgame(cell, board):
    indexes = get_indexes_from_location(cell)
    current_symbol = symbols[turn_player_index]

    if board[0][0] == board[1][1] == board[2][2] == current_symbol:
        return True
    if board[0][2] == board[1][1] == board[2][0] == current_symbol:
        return True
    return False


def check_full_for_endgame(board):
    if board[0].count('X') + board[1].count('X') + board[2].count('X') + \
            board[0].count('0') + board[1].count('0') + board[2].count('0') == 9:
        return True
    return False


def check_for_endgame(cell, board):
    if check_row_for_endgame(cell, board) or \
            check_column_for_endgame(cell, board) or \
            check_diagonals_for_endgame(cell, board):
        print_board()
        print('{} WINS. GAME ENDS'.format(players[turn_player_index]))
        return True

    if check_full_for_endgame(board):
        print('Board is full. GAME ENDS. ITS A TIE')
        print_board()
        return True


def update_board(cell, board):
    indexes = get_indexes_from_location(cell)
    board[indexes[0]][indexes[1]] = symbols[turn_player_index]


if __name__ == '__main__':
    new_game()
    while not exit_game:
        print_board()
        location = ask_for_input()
        if validate_board_location_available(location, board_current):
            update_board(location, board_current)
            exit_game = check_for_endgame(location, board_current)
            switch_user_turn()
