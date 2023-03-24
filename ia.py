import random
from enum import Enum

class Difficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3
    EXTREME = 4
def check_winner(board, sign):
    lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
             (0, 3, 6), (1, 4, 7), (2, 5, 8),
             (0, 4, 8), (2, 4, 6)]

    for line in lines:
        if all([board[pos] == sign for pos in line]):
            return True
    return False

class AI:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def ia(self, board, sign):
        if self.difficulty == Difficulty.EASY:
            return self.easy_ai(board, sign)
        elif self.difficulty == Difficulty.MEDIUM:
            return self.medium_ai(board, sign)
        elif self.difficulty == Difficulty.HARD:
            return self.hard_ai(board, sign)
        elif self.difficulty == Difficulty.EXTREME:
            return self.extreme_ai(board, sign)
        else:
            return False

    def easy_ai(self, board, sign):
        empty_cells = [i for i, cell in enumerate(board) if cell == "."]
        return random.choice(empty_cells)

    def medium_ai(self, board, sign):
        empty_cells = [i for i, cell in enumerate(board) if cell == "."]
        for cell in empty_cells:
            new_board = board.copy()
            new_board[cell] = sign
            if check_winner(new_board, sign):
                return cell
        return random.choice(empty_cells)

    def hard_ai(self, board, sign):
        empty_cells = [i for i, cell in enumerate(board) if cell == "."]
        for cell in empty_cells:
            new_board = board.copy()
            new_board[cell] = sign
            if check_winner(new_board, sign):
                return cell

        opponent_sign = "O" if sign == "X" else "X"
        for cell in empty_cells:
            new_board = board.copy()
            new_board[cell] = opponent_sign
            if check_winner(new_board, opponent_sign):
                return cell

        return random.choice(empty_cells)

    def extreme_ai(self, board, sign):
        def minimax(board, depth, maximizing_player, alpha, beta):
            if check_winner(board, 1):
                return -1
            elif check_winner(board, 2):
                return 1
            elif not any(cell == 0 for cell in board):
                return 0

            if maximizing_player:
                max_eval = float("-inf")
                for i in range(9):
                    if board[i] == 0:
                        new_board = board.copy()
                        new_board[i] = sign
                        eval = minimax(new_board, depth + 1, False, alpha, beta)
                        max_eval = max(max_eval, eval)
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            break
                return max_eval
            else:
                min_eval = float("inf")
                opponent_sign = 1 if sign == 2 else 2
                for i in range(9):
                    if board[i] == 0:
                        new_board = board.copy()
                        new_board[i] = opponent_sign
                        eval = minimax(new_board, depth + 1, True, alpha, beta)
                        min_eval = min(min_eval, eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break
                return min_eval

        best_value = float("-inf")
        best_move = None
        for i in range(9):
            if board[i] == 0:
                new_board = board.copy()
                new_board[i] = sign
                move_value = minimax(new_board, 0, False, float("-inf"), float("inf"))
                if move_value > best_value:
                    best_value = move_value
                    best_move = i

        return best_move