import tkinter as tk
from tkinter import font
from tkinter import messagebox
from tkinter import Frame
import ia
from ia import Difficulty


# Constantes
BACKGROUND_COLOR = "white"
BUTTON_COLOR = "light blue"
WINNER_FONT = ("Helvetica", 16, "bold")
OK_BUTTON_FONT = ("Helvetica", 12, "bold")

class TicTacToe:
    def __init__(self):
        self.init_window()
        self.init_constants()
        self.init_game()
        self.create_main_frame()
        self.create_buttons()
        self.create_reset_button()
        self.center_window()

    def init_window(self):
        """Initialise la fenêtre tkinter."""
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.configure(bg=BACKGROUND_COLOR)

    def create_main_frame(self):
        self.main_frame = Frame(self.window, bg=BACKGROUND_COLOR)
        self.main_frame.grid(row=0, column=0, padx=(10, 0), pady=20)

    def init_constants(self):
        global BUTTON_FONT, WINNER_FONT, OK_BUTTON_FONT
        BUTTON_FONT = font.Font(family="Helvetica", size=20, weight="bold")
        WINNER_FONT = ("Helvetica", 16, "bold")
        OK_BUTTON_FONT = ("Helvetica", 12, "bold")

    def init_game(self):
        self.player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.first_move = True

    def create_buttons(self):
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.main_frame, text="", width=10, height=3, bg=BUTTON_COLOR, font=BUTTON_FONT,
                                   command=lambda r=row, c=col: self.play(r, c))
                button.grid(row=row, column=col, padx=5, pady=5)
                self.buttons[row][col] = button

        self.create_difficulty_buttons(self.window)

    def create_difficulty_buttons(self, frame):
        """Crée les boutons de sélection de la difficulté."""
        self.difficulty_buttons = []
        for i, difficulty in enumerate(ia.Difficulty):
            button = tk.Button(frame, text=difficulty.name, width=10, height=1, bg=BUTTON_COLOR, font=BUTTON_FONT,
                               command=lambda d=difficulty: self.set_difficulty(d))
            button.grid(row=3, column=i, padx=2, pady=5)
            self.difficulty_buttons.append(button)

    def create_bottom_frame(self):
        bottom_frame = tk.Frame(self.window, bg=BACKGROUND_COLOR)
        bottom_frame.grid(row=3, column=0, columnspan=3)
        self.create_difficulty_buttons(bottom_frame)
        self.create_reset_button(bottom_frame)

    def hide_difficulty_buttons(self):
        for button in self.difficulty_buttons:
            button.grid_remove()

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
        self.ai_player = "O"  # Ajoutez cette ligne pour définir l'attribut ai_player
        self.ia_instance = ia.AI(
            difficulty.name.lower())  # Crée une instance de la classe AI avec le nom de la difficulté en minuscules
        self.hide_difficulty_buttons()

    def center_window(self):
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.window.geometry(f"{width}x{height}+{x}+{y}")

    def play(self, row, col):
        if self.make_move(row, col):
            self.post_play()

    def post_play(self):  # Ajoutez la méthode 'post_play' ici
        if self.check_winner(self.player):
            messagebox.showinfo("Tic Tac Toe", f"{self.player} wins!")
            self.new_game()
        elif all([cell != "" for row in self.board for cell in row]):  # Ligne modifiée
            messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            self.new_game()
        else:
            self.player = "O" if self.player == "X" else "X"
            if self.player == self.ai_player:
                self.ia_play()

    def ia_play(self):
        flat_board = [cell for row in self.board for cell in row]
        move = self.ia_instance.ia(flat_board, self.ai_player)
        row, col = divmod(move, 3)
        self.play(row, col)

    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.buttons[row][col].config(text=self.player, disabledforeground="black", state="disable")
            self.board[row][col] = self.player
            return True
        return False

    def check_winner(self, sign):
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] == sign:
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] == sign:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == sign:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == sign:
            return True
        return False

    def is_full(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == "":
                    return False
        return True

    def reset_board(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="", state="normal")
        self.init_game()

    def create_reset_button(self):
        reset_button = tk.Button(self.window, text="Reset", width=10, height=2, bg="lightblue", font=("Helvetica", 14),
                                 command=self.reset_game)
        reset_button.grid(row=4, column=1, padx=10, pady=10)

    def reset_game(self):
        for row in range(3):
            for col in range(3):
                self.board[row][col].config(text="")
                self.game_board[row][col] = ""

        self.player = "X"
        self.game_over = False

class WinnerWindow(tk.Toplevel):
    def __init__(self, winner):
        super().__init__()
        self.init_window(winner)
        self.create_message(winner)
        self.create_ok_button()
        self.center_window()

    def init_window(self, winner):
        """Initialise la fenêtre des résultats."""
        self.title("Résultat")
        self.configure(bg=BACKGROUND_COLOR)
        self.geometry("300x100")

    def create_message(self, winner):
        """Crée le message de résultat."""
        message = f"Le joueur {winner} a gagné !" if winner else "Match nul !"
        label = tk.Label(self, text=message, font=WINNER_FONT, bg=BACKGROUND_COLOR)
        label.pack(pady=10)

        def create_ok_button(self):
            """Crée le bouton OK."""
            ok_button = tk.Button(self, text="OK", font=OK_BUTTON_FONT, command=self.destroy)
            ok_button.pack(pady=5)

        def center_window(self):
            self.update_idletasks()
            width = self.winfo_width()
            height = self.winfo_height()
            screen_width = self.winfo_screenwidth()
            screen_height = self.winfo_screenheight()

            x = (screen_width // 2) - (width // 2)
            y = (screen_height // 2) - (height // 2)
            self.geometry(f"{width}x{height}+{x}+{y}")

def main():
    game = TicTacToe()
    game.window.mainloop()

if __name__ == "__main__":
    main()