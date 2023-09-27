# This file is used to create a gui for the game
# That isn't just text on a screen

from tkinter import *
from tkinter import ttk

class upwords_gui:
    def __init__(self):
        return
        self.root = Tk()
        self.root.title("UPWORDS")

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

    def update(self, board):
        return
        tiles = board.tiles

        for x, col in enumerate(tiles):
            for y, tile in enumerate(col):
                label = ttk.Label(self.root, text=tile[0])
                label.grid(column=x, row=y)
