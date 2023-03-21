import tkinter as tk
from tkinter import font

# Constantes
BACKGROUND_COLOR = "white"
BUTTON_COLOR = "light blue"

class TicTacToe:
    def __init__(self):
        self.init_window()
        self.init_constants()
        self.init_game()
        self.create_buttons()
        self.center_window()

    def init_window(self):
        """Initialise la fenêtre tkinter."""
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.configure(bg=BACKGROUND_COLOR)

    def init_constants(self):
        global BUTTON_FONT, WINNER_FONT, OK_BUTTON_FONT
        BUTTON_FONT = font.Font(family="Helvetica", size=20, weight="bold")
        WINNER_FONT = ("Helvetica", 16, "bold")
        OK_BUTTON_FONT = ("Helvetica", 12, "bold")

    def init_game(self):
        """Initialise les variables de jeu."""
        self.player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]

    def create_buttons(self):
        """Crée les boutons du plateau de jeu et les ajoute à la fenêtre."""
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.window, text="", width=10, height=3, bg=BUTTON_COLOR, font=BUTTON_FONT, command=lambda r=row, c=col: self.play(r, c))
                button.grid(row=row, column=col, padx=5, pady=5)
                self.buttons[row][col] = button

    def center_window(self):
        """Centre la fenêtre sur l'écran."""
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.window.geometry(f"{width}x{height}+{x}+{y}")

    def play(self, row, col):
        if self.board[row][col] == "":
            self.buttons[row][col].config(text=self.player, disabledforeground="black", state="disable")
            self.board[row][col] = self.player

            if self.check_winner(self.player):
                winner_window = WinnerWindow(self.player)
                self.reset_board()
            elif self.is_full():
                winner_window = WinnerWindow(None)
                self.reset_board()
            else:
                self.player = "O" if self.player == "X" else "X"

    def check_winner(self, player):
        for row in range(3):
            if all([self.board[row][col] == player for col in range(3)]):
                return True

        for col in range(3):
            if all([self.board[row][col] == player for row in range(3)]):
                return True

        if all([self.board[i][i] == player for i in range(3)]) or all([self.board[i][2 - i] == player for i in range(3)]):
            return True

        return False

    def is_full(self):
        return all([self.board[row][col] != "" for row in range(3) for col in range(3)])

    def reset_board(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="", state="normal")
                self.board[row][col] = ""

    def run(self):
        self.window.mainloop()

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
        """Centre la fenêtre sur l'écran."""
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

if __name__ == "__main__":
    tic_tac_toe = TicTacToe()
    tic_tac_toe.run()