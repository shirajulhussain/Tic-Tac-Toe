#!/usr/bin/env python3

# Tic-tac-toe game

# create list for board positions. Position [0] has no use.
from random import randint

board = ['', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def intro():
    print('''
    Hello, let\'s play Tic-Tac-Toe. You (the player) are O and the Computer is X.

    To win, get 3 in a row

    Enter a number between 1 and 9 according to the arrangement below 

    The board:  1 | 2 | 3          
                --------- 
                4 | 5 | 6 
                --------- 
                7 | 8 | 9 

        ''')

def gameboard():
    print(board[1] + '|' + board[2] + '|' + board[3]
          + '\n' + '-----'
          + '\n' + board[4] + '|' + board[5] + '|' + board[6]
          + '\n' + '-----'
          + '\n' + board[7] + '|' + board[8] + '|' + board[9] + '\n')

def tiecheck():
    tie = True
    for i in board[1:]:
        if i == ' ':
            tie = False
    if tie == True:
        print('Game ended in a Tie!')

while True:
    intro()
    gameboard()

    while True:
        move = input('# Make your move ![1-9] : ')
        move = int(move)
        if board[move] == 'O' or board[move] == 'X':
            print('Invalid number ! Try Again !')
            continue
        else:
            board[move] = 'O'
            break

    if ((board[1] == 'O' and board[2] == 'O' and board[3] == 'O')
        or (board[4] == 'O' and board[5] == 'O' and board[6] == 'O')
        or (board[7] == 'O' and board[8] == 'O' and board[9] == 'O')
        or (board[1] == 'O' and board[4] == 'O' and board[7] == 'O')
        or (board[2] == 'O' and board[5] == 'O' and board[8] == 'O')
        or (board[3] == 'O' and board[6] == 'O' and board[9] == 'O')
        or (board[1] == 'O' and board[5] == 'O' and board[9] == 'O')
        or (board[3] == 'O' and board[5] == 'O' and board[7] == 'O')):
        gameboard()
        print('CONGRATULATIONS! YOU WON!')
        break
    else: pass

    tiecheck()

    while True:
        cmove = randint(1, 9)
        if board[cmove] == 'O' or board[cmove] == 'X':
            continue
        else:
            board[cmove] = 'X'
            break

    if ((board[1] == 'X' and board[2] == 'X' and board[3] == 'X')
        or (board[4] == 'X' and board[5] == 'X' and board[6] == 'X')
        or (board[7] == 'X' and board[8] == 'X' and board[9] == 'X')
        or (board[1] == 'X' and board[4] == 'X' and board[7] == 'X')
        or (board[2] == 'X' and board[5] == 'X' and board[8] == 'X')
        or (board[3] == 'X' and board[6] == 'X' and board[9] == 'X')
        or (board[1] == 'X' and board[5] == 'X' and board[9] == 'X')
        or (board[3] == 'X' and board[5] == 'X' and board[7] == 'X')):
        gameboard()
        print('THE COMPUTER WON! YOU LOSE')
        break
    else: pass

    tiecheck()
