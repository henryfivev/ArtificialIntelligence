from __future__ import print_function
from random import shuffle
from board import *
from a_star import a_star
import globals
import psutil
import time
import gc
import os


def intro():
    print('Welcome to the 15 Puzzle Program.')
    print('Directions:')
    print('Type "r" to randomize the start board WARNING: You may end up with a '
          'board that will run you out of memory or is not possible to solve.\n or')

    print('USE THIS: 1 2 3 4 5 6 7 8 13 9 12 15 0 11 10 14\n')
    print('Copy paste this and hit enter')
    return input("Please enter here: ")


def check_input(user_input):
    """
    :param user_input: Determines how to create the board based on user input
    :return: Returns true if valid entry, false otherwise
    """

    if user_input == 'r' or user_input == 'R':
        return True

    check_against = GOAL_STATE_15_AS_SLIST
    user_input = user_input.split(" ")

    if len(user_input) != 16:
        return False
    for num in check_against:
        if num not in user_input:
            return False
    return True


def randomize_board ():
    """
    :return: USERS_BOARD is the board used to begin the program, shuffles board is user presses 'r'
    """

    users_board = GOAL_STATE_15_AS_SLIST
    return shuffle(users_board)


def print_board(users_board):
    """
    Prints the board.
    :return:
    """
    board = ""
    count = 0
    for num in users_board:
        if count % EDGE_LENGTH == 0 and count != 0:
            board += '\n'
        if len(num) == 1:
            if num == '0':
                board += '   '
            else:
                board += num + '  '
        else:
            board += num + ' '
        count += 1
    print(board)


def main():
    """
    Main is the function used to run/drive the program.
    :return:
    """

    user_input = intro()
    users_board = -999
    is_valid = check_input(user_input)
    if is_valid:
        if user_input == 'r' or user_input == 'R':
            users_board = randomize_board()
        else:
            users_board = user_input.split(' ')
        print('Successful input. Solving the board.')
        print('Your board: ')
        print_board(users_board)
    else:
        print('Incorrect input. Terminating program. Try again.')
        exit(0)

    print('Time to solve your Puzzle using A*.\n\n')

    process = psutil.Process(os.getpid())
    memory = process.memory_info().rss
    memory_main = memory / 1000000

    globals.memory_main = memory_main


    # Manhattan Heuristic used with A*
    manhattan_astar_start_time = time.time()
    a_star(users_board, 'M')
    manhattan_astar_time = time.time() - manhattan_astar_start_time
    gc.collect()

    # Displaced Tiles Heuristic used with A*
    displaced_astar_start_time = time.time()
    a_star(users_board, 'D')
    displaced_astar_time = time.time() - displaced_astar_start_time
    gc.collect()

    # 1 2 3 4 5 6 7 8 13 9 12 15 0 11 10 14
    # 1 2 3 4 5 6 7 8 0 9 10 15 13 14 12 11

    print('\n------------')
    print('Result of Time Elapsed:')
    print('------------')
    print('Manhattan A* Time Elapsed: ', manhattan_astar_time * 1000, 'ms')
    print('Displaced A* Time Elapsed: ', displaced_astar_time * 1000, 'ms')
    print('------------')

if __name__ == "__main__":
    main()
