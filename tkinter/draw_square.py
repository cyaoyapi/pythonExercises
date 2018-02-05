# This program draw a square of certain side according the entered value by the user

#import signal
from turtle import *  

side = int(input("Enter the side of the square :\n"))
color('blue')
width(5)
cpt = 1
while cpt <= 4:	
	forward(side)
	left(90)
	cpt += 1
# We can put the program on pause using signal.pause()
stop = input("Type ENTER to stop the program :\n")
exit()


