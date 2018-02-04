# This program draw a square of certain side according the entered value by the user

import signal
from turtle import *  

side = int(input("Enter the side of the square :\n"))
color('blue')
width(5)
forward(side)
cpt = 1
while cpt <= 3:
	left(90)
	forward(side)
	cpt += 1
stop = input("Type ENTER to stop the program :\n")
exit()


