""" This program display a triangle with rigth angle.

		*
		**
		***
		****
		*****
		******
		*******
		********
		*********
"""

size = int(input("Enter the size of the triangle (> 1) \n"))
cpt = 1
print("Your rigth trinagle")
print("=======================")
while cpt <= size:
	print(cpt*"*")
	cpt += 1

