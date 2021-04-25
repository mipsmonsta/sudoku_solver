import tkinter as tk
from tkinter import *
from random import randint

class TableWindow:
    def __init__(self):

        self.window = tk.Tk()
        self.window.geometry("400x400+100+100")
        # self.window.minsize(width=400, height=400)

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
        self.cellVars = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                var = StringVar()
                self.entries[i][j] = Entry(self, width=3, textvariable=var, justify='center', font=('Arial', 10, 'bold'), relief='flat')
                self.entries[i][j].config(highlightbackground="blue", highlightcolor="red")
                self.entries[i][j].grid(row=i, column=j)
                validateDigitEntry = self.entries[i][j].register(self.validDigitEntry)
                self.entries[i][j].config(validate='key', validatecommand = (validateDigitEntry, '%d', '%i', '%P' ))
                self.cellVars[i].append(var)
                #self.entries[i][j].insert(END,0)

# validation of entries
    def validDigitEntry(self, why, where, willBe):
        if len(willBe) > 1:
            return False

        if willBe.isdigit() and willBe != '0': # 1 for addition 
            return True

        return False

    def getMatrixOfValues(self):
        values = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if self.cellVars[i][j].get() == "":
                    values[i].append(0)
                else:
                    values[i].append(self.cellVars[i][j].get())
        return values
