from tkinter import *
from tkinter import messagebox
import sys
def main(window):
    window.title("Automatic Hypodermic Tube Bending Machine")
    lbl = Label(window, text="Hello", font=("Arial Bold", 50))
    lbl.grid(column=0, row=0)
    window.geometry('1280x720')
    btn = Button(window, text="Click Me", bg="lightblue", fg="white", command=clicked)
    btn.grid(column=1, row=0)
    makeMenu(window)
    window.protocol("WM_DELETE_WINDOW", ask_quit)
    window.mainloop()

def ask_quit():
    exitProgram(window)
def exitProgram(window):
    if messagebox.askyesno('Quit','Do you want to quit?'):
        window.destroy()

def makeMenu(window):
    menu = Menu(window)
    new_item = Menu(menu,tearoff=0)
    new_item.add_command(label='New',command=newFile)
    new_item.add_separator()
    new_item.add_command(label='Edit',command=openFile)
    new_item.add_separator()
    new_item.add_command(label='Save',command=saveFile)
    new_item.add_separator()
    new_item.add_command(label='Update',command=updateCode)
    new_item.add_separator()
    new_item.add_command(label='Exit',command=ask_quit)
    menu.add_cascade(label='File', menu=new_item)
    window.config(menu=menu)

def clicked():
    print("Clicked")
def newFile():
    print("new")
def openFile():
    print("open")
def saveFile():
    print("save")
def updateCode():
    print("update")
window = Tk()
main(window)
quit()