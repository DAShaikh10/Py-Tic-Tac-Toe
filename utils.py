"""
@Author: DAShaikh
"""

import os


LOGO = """
████████ ██  ██████     ████████  █████   ██████     ████████  ██████  ███████ 
   ██    ██ ██             ██    ██   ██ ██             ██    ██    ██ ██      
   ██    ██ ██             ██    ███████ ██             ██    ██    ██ █████   
   ██    ██ ██             ██    ██   ██ ██             ██    ██    ██ ██      
   ██    ██  ██████        ██    ██   ██  ██████        ██     ██████  ███████  
"""

def is_tie(board):
    for item in board:
        if item.strip().isdigit():
            return False

    return True

def is_winner(board):
    # Check row, column and diagonals.
    if (board[0] == board[1] == board[2]) or (board[3] == board[4] == board[5]) or \
       (board[6] == board[7] == board[8]) or (board[0] == board[3] == board[6]) or \
       (board[2] == board[4] == board[6]) or (board[1] == board[4] == board[7]) or \
       (board[0] == board[4] == board[8]) or (board[2] == board[5] == board[8]):
        return True

    return False

def display_board(board):
    print(f"""
        |        |
    {board[0]}  |   {board[1]}   |   {board[2]}  
________|________|________
        |        |
    {board[3]}  |   {board[4]}   |   {board[5]}
________|________|________
        |        |
    {board[6]}  |   {board[7]}   |   {board[8]}
        |        |
    """)

def cls():
    """ Clear console screen. """
    
    # For windows.
    if os.name == 'nt':
        _ = os.system('cls')
  
    # For mac and linux.
    elif os.name == 'posix':
        _ = os.system('clear')
