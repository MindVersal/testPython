from tkinter import *
import random
import time

print('Chapter 13.')
print('Game')

tk = Tk()
tk.title("My Games")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

print('THE END.')
