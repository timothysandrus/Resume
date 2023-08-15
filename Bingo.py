from tkinter import *
import tkinter

root = Tk()
frame=Frame(root)
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
frame.grid(row=0, column=0, sticky=N+S+E+W)
grid=Frame(frame)
grid.grid(sticky=N+S+E+W, column=0, row=7, columnspan=2)
Grid.rowconfigure(frame, 7, weight=1)
Grid.columnconfigure(frame, 0, weight=1)

active="red"
default_color="white"
Cells = []
global done
done = False
class cell:
    def __init__(self,active, x, y):
        self.active = active
        self.x = x
        self.y = y
def main(height=5,width=5):

  for x in range(width):
    for y in range(height):
        if(x == 2 and y ==2):
            btn = tkinter.Button(frame, bg=active)
            btn.grid(column=x, row=y, sticky=N+S+E+W)
            btn["command"] = lambda btn=btn: click(btn)
            Cells.append(1)
        else:
             btn = tkinter.Button(frame, bg=default_color)
             btn.grid(column=x, row=y, sticky=N+S+E+W)
             btn["command"] = lambda btn=btn: click(btn)
             Cells.append(0)

  for x in range(width):
    Grid.columnconfigure(frame, x, weight=1)

  for y in range(height):
    Grid.rowconfigure(frame, y, weight=1)

  return frame

def click(button):
    global done
    if(button["bg"] != active):
        button["bg"] = active
        Cells[(button.grid_info()['column']*5)+button.grid_info()['row']] = 1
        checkline(button.grid_info()['row'],button.grid_info()['column'])
        if(done == False):
            checkdiag(button.grid_info()['row'],button.grid_info()['column'])
    

def checkline(row, col):
    global done
    yes = 0
    for y in range(5):
        yes += Cells[(y*5)+row]
    if(yes == 5):
        print("bingo")
        done = True
        root.destroy()
    yes = 0
    for x in range(5):
        yes += Cells[(col*5)+x]
    if(yes == 5):
        print("bingo")
        done = True
        root.destroy()
    
def checkdiag(row, col):
    if(row == 0 and col == 0 or row == 1 and col == 1 or row == 3 and col == 3 or row == 4 and col == 4):
        yes = 0
        for x in range(5):
            yes += Cells[(x*5)+x]
        if(yes == 5):
            print("bingo")
            done = True
            root.destroy()
    if(row == 4 and col == 0 or row == 3 and col == 1 or row == 1 and col == 3 or row == 0 and col == 4):
        yes = 0
        for x in range(5):
            yes += Cells[4*x + 4]
        if(yes == 5):
            print("bingo")
            done = True
            root.destroy()
    
w= main(5,5)
tkinter.mainloop()
