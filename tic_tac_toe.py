"""
@Author: DAShaikh
"""

import time
import random

from utils import *
from players import Human, AI


while True:
    # Set the game variables on start of the game.
    TURN = 0
    board = ["1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 "]

    # Game mode setup.
    while True:
        print(LOGO)
        print("""   --- GAME MODE ---
    1 - Human vs. Human
    2 - Human vs. AI
    3 - AI vs. AI
    """)

        option = input("Select game mode: ")
        cls()

        # Handle user input if it is not integer.
        try:
            option = int(option)
            if option == 1:
                p1 = Human()
                p2 = Human()
                break
            if option == 2:
                p1 = Human()
                p2 = AI()
                break
            if option == 3:
                p1 = AI()
                p2 = AI()
                break
            
            print(f"Invalid choice ({option}) Try again!")
        except:
            print(f"Invalid choice ({option}) Try again!")

    # Pause duration variable to handle pauses between two AI moves.
    PAUSE = 0

    print(LOGO)
    if isinstance(p1, Human) and isinstance(p2, Human):
        print("PLAYER 1: HUMAN\nPLAYER 2: HUMAN")
    elif isinstance(p1, Human) and isinstance(p2, AI):
        print("PLAYER 1: HUMAN\nPLAYER 2: AI")
    else:
        print("PLAYER 1: AI\nPLAYER 2: AI")
        PAUSE = 1

    # Randomly select who start's the game.
    TURN = random.randint(0, 1)
    if TURN:
        print("\nPLAYER 2 will start the game.")
        p2.pick_symbol()
        p1.symbol = "⭕" if p2.symbol == "❌" else "❌"
        p1.opponent = "⭕" if p1.symbol == "❌" else "❌"
    else:
        print("\nPLAYER 1 will start the game.")
        p1.pick_symbol()
        p2.symbol = "⭕" if p1.symbol == "❌" else "❌"
        p2.opponent = "⭕" if p2.symbol == "❌" else "❌"

    # Play game untill a player wins or the game ends in a draw.
    while True:
        cls()
        print(LOGO)
        print("PLAYER 1:", p1.symbol)
        print("PLAYER 2:", p2.symbol)

        # Display board before a move.
        display_board(board)
        p2.next_move(board) if TURN else p1.next_move(board)
        
        cls()

        # Display board after a move.
        print(LOGO)
        display_board(board)

        # Check game status.
        if is_winner(board):
            print("PLAYER", TURN + 1, "is the winner! 🎉")
            break
        if is_tie(board):
            print("Game ended in a Draw! ☹️")
            break

        # Switch turn.
        TURN = int(not TURN)
        time.sleep(PAUSE)
        
    play_again = input("Enter 'y' to play again: ").lower()
    cls()
    if play_again != "y":
        print("Thank you for playing the game! 😀\nGoodbye 👋")
        break
