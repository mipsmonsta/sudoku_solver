import tkinter as tk
from tkinter import *
from random import randint

class TableWindow:
    def __init__(self):

        self.window = tk.Tk()
        self.window.geometry("400x400+100+100")
        # self.window.minsize(width=400, height=400)

        # self.window.grid_columnconfigure(8, weight=1)
        # self.window.grid_rowconfigure(8, weight=1)

        self.window.title("Sudoku Solver")
        self.window.config(padx=2, bg="white")
        self.window.grid_rowconfigure((0,2),weight=1) # so that Sudoky board is centralised
        self.window.grid_columnconfigure((0,2),weight=1)
      

        self.sudokuBoard = BoardFrame(self.window)
        self.sudokuBoard.grid(row=1, column=1) # at grid (1,1)

        self.window.mainloop()

    

class BoardFrame(Frame):
    def __init__(self, parent: Tk):
        Frame.__init__(self, parent, bg="white")
        self.parent = parent
        

        self._initSudokuTable()


# UI Helpers
    def _initSudokuTable(self):
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                self.entries[i][j] = Entry(self, width=3, justify='center', font=('Arial', 10, 'bold'))
                self.entries[i][j].config(highlightbackground="blue", highlightcolor="red")
                self.entries[i][j].grid(row=i, column=j)
                self.entries[i][j].insert(END, randint(1, 9))