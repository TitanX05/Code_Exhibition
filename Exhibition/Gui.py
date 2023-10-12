import tkinter 
from tkinter import *
import Camera
root = tkinter.Tk()
root.title ("Motion tracking")
root.geometry('640x480')
a = Label(root, text = "Hello! Welcome to motion tracking..!")
a.pack()
btn1 = Button(root, text = "Click to start", command = cv())



root.mainloop()
