import tkinter as tk
from tkinter import messagebox

# Backtracking Sudoku Solver
def solve(board):
    empty = find_empty(board)
    if not empty:
        return True  # Puzzle Solved
    row, col = empty

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0  # Undo

    return False

def is_valid(board, num, pos):
    row, col = pos

    # Check row
    if any(board[row][i] == num for i in range(9)):
        return False

    # Check column
    if any(board[i][col] == num for i in range(9)):
        return False

    # Check 3x3 grid
    box_x, box_y = col // 3, row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num:
                return False

    return True

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # Row, Col
    return None

# GUI Part
class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Sudoku Solver")

        self.board = [[0] * 9 for _ in range(9)]
        self.entries = [[None] * 9 for _ in range(9)]

        self.setup_ui()

    def setup_ui(self):
        # Create Sudoku grid
        for i in range(9):
            for j in range(9):
                e = tk.Entry(self.root, width=3, font=("Arial", 18), justify="center")
                e.grid(row=i, column=j, padx=2, pady=2, ipadx=5, ipady=5)
                self.entries[i][j] = e

        # Solve button
        solve_button = tk.Button(self.root, text="Solve", command=self.solve_sudoku, width=10)
        solve_button.grid(row=10, column=4, columnspan=2, pady=20)

        # Reset button
        reset_button = tk.Button(self.root, text="Reset", command=self.reset_board, width=10)
        reset_button.grid(row=10, column=2, columnspan=2, pady=20)

    def get_board(self):
        for i in range(9):
            for j in range(9):
                value = self.entries[i][j].get()
                if value == '':
                    self.board[i][j] = 0
                else:
                    try:
                        num = int(value)
                        if 1 <= num <= 9:
                            self.board[i][j] = num
                        else:
                            messagebox.showerror("Invalid input", "Please enter numbers between 1 and 9.")
                            return False
                    except ValueError:
                        messagebox.showerror("Invalid input", "Please enter numbers only.")
                        return False
        return True

    def display_board(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].insert(0, str(self.board[i][j]))

    def solve_sudoku(self):
        if self.get_board():
            if solve(self.board):
                self.display_board()
            else:
                messagebox.showinfo("No Solution", "This Sudoku puzzle cannot be solved.")

    def reset_board(self):
        """Clears the Sudoku grid."""
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                self.board[i][j] = 0

# Main Function
if __name__ == "__main__":
    root = tk.Tk()
    gui = SudokuGUI(root)
    root.mainloop()
