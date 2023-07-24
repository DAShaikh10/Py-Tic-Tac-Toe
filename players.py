"""
@Author: DAShaikh
"""

import random

from utils import *


class Human:
    """ Class to handle human player actions. """

    def __init__(self):
        self.symbol = None
        self.opponent = None

    def pick_symbol(self):
        choice = input("Select [❌\⭕]: ").upper()
        while choice not in ["X", "O"]:
            cls()
            choice = input(f"Invalid choice ({choice}) Try again!\nSelect [❌\⭕]: ").upper()
   
        self.symbol = "❌" if choice == "X" else "⭕"
        self.opponent = "⭕" if self.symbol == "❌" else "❌"

    def next_move(self, board):
        while True:
            choice = input("Enter move [1 - 9]: ")
            
            # Handle user input if it is not integer.
            try:
                choice = int(choice) - 1
                if board[choice].strip().isdigit():
                    board[choice] = self.symbol
                    return
                else:
                    cls()
                    print(LOGO)
                    display_board(board)
                    print(f"Invalid choice ({choice}) Try again!")
            except:
                cls()
                print(LOGO)
                display_board(board)
                print(f"Invalid choice ({choice}) Please try again!")

class AI:
    """
    Class to handle AI player actions.
    AI: Minimax algorithm + α-β Optimization (Alpha-beta pruning).
    """

    def __init__(self):
        self.symbol = None
        self.opponent = None

    @staticmethod
    def _moves_left(board):
        for item in board:
            if item.strip().isdigit():
                return True

        return False

    def pick_symbol(self):
        self.symbol = random.choice(["❌", "⭕"])
        self.opponent = "⭕" if self.symbol == "❌" else "❌"

    def _evaluate_board(self, board, depth):
        """ Heuristic function to calculate score of moves. """

        # If AI player (Maximizing player) wins return '50 - depth' as the score. 
        # This forces the AI player to make a move which will lead to faster victory instead of a draw or delayed victory.
        # If human player (Minimizing player) wins return '-50 + depth' as the score.
        # Return 'None' if the game has not ended.

        if (board[0] == board[1] == board[2]) or board[0] == board[3] == board[6]:
            return (50 - depth) if board[0] == self.symbol else (-50 + depth)
        elif (board[3] == board[4] == board[5]) or (board[0] == board[4] == board[8]) or \
             (board[2] == board[4] == board[6]) or (board[1] == board[4] == board[7]):
            return (50 - depth) if board[4] == self.symbol else (-50 + depth)
        elif (board[6] == board[7] == board[8]) or (board[2] == board[5] == board[8]):
            return (50 - depth) if board[8] == self.symbol else (-50 + depth)

    def _minimax(self, board, is_maximizing, alpha, beta, depth):
        """ Minimax algorithm implementation with alpha beta pruning optimization. """

        # Get score for win conditions or if it is a tie.
        score = self._evaluate_board(board, depth)
        if score is not None:
            return score
        elif not self._moves_left(board):
            return 0

        if is_maximizing:
            best_score = -50
            for position, item in enumerate(board):
                if item.strip().isdigit():
                    board[position] = self.symbol
                    best_score = max(best_score, self._minimax(board, not is_maximizing, alpha, beta, depth + 1))
                    board[position] = str(position + 1) + " "

                # Alpha-beta pruning.
                if best_score >= beta: return best_score
                alpha = max(best_score, alpha)

            return best_score
        else:
            best_score = 50
            for position, item in enumerate(board):
                if item.strip().isdigit():
                    board[position] = self.opponent
                    best_score = min(best_score, self._minimax(board, not is_maximizing, alpha, beta, depth + 1))
                    board[position] = str(position + 1) + " "

                # Alpha-beta pruning.
                if best_score <= alpha: return best_score
                beta = min(best_score, beta)

            return best_score

    def next_move(self, board):
        best_move_val = -50
        best_move = None
        for position, item in enumerate(board):
            if item.strip().isdigit():
                board[position] = self.symbol
                current_move_val = self._minimax(board, False, -50, 50, 0)
                board[position] = str(position + 1) + " "
                if current_move_val > best_move_val:
                    best_move_val = current_move_val
                    best_move = position

        # AI play's it's turn.
        board[best_move] = self.symbol
