# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

board_template = '''
---|---|---
---|---|---
---|---|---
'''

board_current = ''
player_name_first = 'Player1'
player_name_second = 'Player2'
player_current = player_name_first


def new_game():
    global board_current
    global player_name_first
    global player_name_second
    board_current = board_template
    player_name_first = input("First player will use X.\nName [default: Player1]")
    player_name_second = input("First player will use O.\nName [default: Player2]")


def print_board():
    print(board_current)
    print('Turn is on{}'.format(player_current))


if __name__ == '__main__':
    new_game()
    print_board()
