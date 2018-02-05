#!/usr/bin/python3.6
#-*- coding:utf-8 -*-

# My first Graphical User Interface with tkinter module

from tkinter import *

wind = Tk()
lab1 = Label(wind, text="Clin on the button to quit the program", fg='red')
lab1.pack()
btn1 = Button(wind, text="Quit", command=wind.destroy)
btn1.pack()
wind.mainloop()