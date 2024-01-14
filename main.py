import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [" " for _ in range(9)]

        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    master,text=" ",font=("Helvetica",20), width=5, height=2,
                    command=lambda row=i, col = j: self.on_button_click(row,col)
                )
                button.grid(row=i, column=j)
                self.buttons.append(button)
    
    def on_button_click(self, row, col):
        index = 3 * row + col
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)

            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe",f"pemain{self.current_player} menang!")
                self.reset_game()
            elif " " not in self.board:
                messagebox.showinfo("Tic Tac Toe", "Seri!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
    
    def check_winner(self):
        winning_combinations = [
            (0,1,2), (3,4,5), (6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6) 
        ]

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return True
        
        return False
    
    def reset_game(self):
        for i in range(9):
            self.board[i]=" "
            self.buttons[i].config(text=" ")

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()
