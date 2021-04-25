import tkinter as tk
from tkinter import *
from random import randint
from sudoku import SudokuBrain

class TableWindow:
    def __init__(self):

        self.window = tk.Tk()
        self.window.geometry("400x400+100+100")
        # self.window.minsize(width=400, height=400)

        self.window.title("Sudoku Solver")
        self.window.config(padx=2, bg="white")
        self.window.grid_rowconfigure((0,2),weight=1) # so that Sudoky board is centralised
        self.window.grid_columnconfigure((0,2),weight=1)

        # button 
        self.solveButton = Button(self.window, text="Solve", command=self.solveBoard)
        self.solveButton.grid(row=2,column=1)

        self.sudokuBoard = BoardFrame(self.window)
        self.sudokuBoard.grid(row=1, column=1) # at grid (1,1)

        self.brain = SudokuBrain()
        

        self.window.mainloop()

    # Commands
    def validateBoard(self):
        board = self.sudokuBoard.getBoardInString()
        print(board)
        return self.brain.isValidSudoku(board)
    
    def solveBoard(self):
        boardString = self.sudokuBoard.getBoardInString()
        isValidBoard = self.brain.isValidSudoku(self.sudokuBoard.getBoardInString())
        exceptSet = set([])
        for i in range(len(boardString)): 
            for j in range(len(boardString[0])):
                if boardString[i][j] != ".":
                    exceptSet.add((i,j))
        
        print(f"valid board {isValidBoard}")
        if isValidBoard:
            solBoard = self.brain.solveSudoku(self.sudokuBoard.getBoardInMatrix())
            self.sudokuBoard.setBoard(solBoard, exceptSet)


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

    def setBoard(self, board, exceptSet=None):
        for i in range(len(self.cellVars)):
            for j in range(len(self.cellVars[0])):
                if exceptSet:
                    if (i,j) in exceptSet:
                        continue
                self.entries[i][j].config(highlightbackground="green", highlightcolor="red")
                self.cellVars[i][j].set(str(board[i][j]))
        

# validation of entries
    def validDigitEntry(self, why, where, willBe):
        
        if len(willBe) > 1:
            return False

        if willBe.isdigit() and willBe != '0': 
            return True

        return False

    def getBoardInString(self):
        values = ["" for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if self.cellVars[i][j].get() == "":
                    values[i] += "."
                else:
                    values[i] += str(self.cellVars[i][j].get())
        return values

    def getBoardInMatrix(self):
        values = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if self.cellVars[i][j].get() == "":
                    values[i].append(0)
                else:
                    values[i].append(int(self.cellVars[i][j].get()))
        return values
