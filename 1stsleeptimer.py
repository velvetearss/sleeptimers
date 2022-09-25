from tkinter import *
import os

root = Tk()

def myClick1():
    myLabel = Label(root, text="GOODNIGHT <3")
    os.system('cmd /c shutdown -s -t 3600')
    myLabel.pack()

def myClick2():
    myLabel = Label(root, text="GOODNIGHT <33")
    os.system('cmd /c shutdown -s -t 7200')
    myLabel.pack()

def myClick3():
    myLabel = Label(root, text="okokok we stopped it")
    os.system('cmd /c shutdown -a')
    myLabel.pack()

myButton1 = Button(root, text="1hr timer", padx=50, command=myClick1)
myButton1.pack()
myButton2 = Button(root, text="2hr timer", padx=50, command=myClick2)
myButton2.pack()
myButton3 = Button(root, text="abort", padx=50, command=myClick3)
myButton3.pack()

root.mainloop()