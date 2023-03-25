import tkinter as tk
from tkinter import messagebox, Toplevel, Label, Button


class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.config(bg="white")
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'


        for i in range(3):
            for j in range(3):
                button = tk.Button(self.window, text='', width=10, height=3, bg="white", font=("Arial", 16), command=lambda i=i, j=j: self.play(i, j))
                button.grid(row=i, column=j, padx=5, pady=5)
                self.board[i][j] = button

        self.menu = tk.Menu(self.window)
        self.filemenu = tk.Menu(self.menu, tearoff=0)
        self.filemenu.add_command(label="Nouvelle partie", command=self.reset_board)
        self.filemenu.add_command(label="Règles", command=self.show_rules)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Quitter", command=self.window.quit)
        self.menu.add_cascade(label="Menu", menu=self.filemenu)
        self.window.config(menu=self.menu)
        self.center_window()

    def play(self, i, j):
        if not self.board[i][j]['text']:
            self.board[i][j].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Félicitations", f"Le joueur {self.current_player} a gagné! Vous êtes le champion du monde... de ce match!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Match nul", "La partie est terminée. C'est un match nul. Vous êtes tous les deux des génies!")
                self.reset_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'


    def check_winner(self):
        for i in range(3):
            if self.board[i][0]['text'] == self.board[i][1]['text'] == self.board[i][2]['text'] != '':
                return True
            if self.board[0][i]['text'] == self.board[1][i]['text'] == self.board[2][i]['text'] != '':
                return True

        if self.board[0][0]['text'] == self.board[1][1]['text'] == self.board[2][2]['text'] != '':
            return True
        if self.board[0][2]['text'] == self.board[1][1]['text'] == self.board[2][0]['text'] != '':
            return True

        return False

    def show_rules(self):
        rules_window = Toplevel(self.window)
        rules_window.title("Règles du jeu")
        rules_window.config(bg="white")

        title = Label(rules_window, text="Règles du Tic Tac Toe", font=("Arial", 20, "bold"), bg="white")
        title.pack(pady=10)

        rules_text = ("1. Le joueur X commence toujours.\n"
                      "2. Les joueurs placent alternativement leur symbole dans une case vide.\n"
                      "3. Le premier joueur qui aligne 3 symboles (horizontalement, verticalement ou diagonalement) remporte la partie.\n"
                      "4. Si le plateau est rempli sans qu'aucun joueur n'ait aligné 3 symboles, c'est un match nul.\n"
                      "5. Amusez-vous bien et n'oubliez pas de célébrer vos victoires avec un grand sourire!")
        rules_label = Label(rules_window, text=rules_text, font=("Arial", 14), bg="white", justify="left")
        rules_label.pack(padx=20)
        close_button = Button(rules_window, text="Fermer", font=("Arial", 12), bg="white", command=rules_window.destroy)
        close_button.pack(pady=10)

    def check_draw(self):
        for i in range(3):
            for j in range(3):
                if not self.board[i][j]['text']:
                    return False
        return True

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j].config(text='')
        self.current_player = 'X'

    def center_window(self):
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (width / 2))
        y_cordinate = int((screen_height / 2) - (height / 2))
        self.window.geometry(f"{width}x{height}+{x_cordinate}+{y_cordinate}")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()