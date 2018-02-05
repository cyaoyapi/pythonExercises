#!/usr/bin/python3.6
#-*- coding:utf8 -*-

#This program draw multiple lines

from random import randrange
from tkinter import *

# Functions definitions

def drawline():
	""" Function to draw a line. """
	global x1, y1, x2, y2, color
	canv.create_line(x1,y1,x2,y2,fill=color)
	y1, y2 = y1 + 10, y2 -10

def change_color():
	""" Function to change the line color. """

	global color
	colors_list = ['red','orange','yellow','green','blue','indigo','purple','pink']
	color = colors_list[randrange(8)]


# Main Program

x1, y1, x2, y2, color = 10, 190, 190, 10, 'dark green'
wind = Tk()
canv = Canvas(wind, bg='dark grey', width=200, height=200)
canv.pack(side=LEFT)
btn_quit = Button(wind, text="Quit", command=wind.quit)
btn_quit.pack(side=BOTTOM)
btn_draw_line = Button(wind, text="Draw a new line", command=drawline)
btn_draw_line.pack()
btn_change_color = Button(wind, text="Change line color", command=change_color)
btn_change_color.pack()
wind.mainloop()
wind.destroy()