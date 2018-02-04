# This program display a suite of terms of fibonacci suite.

nb = int(input("Enter the number of the terms\n"))
a, b = 1, 1
cpt = 1
while cpt <= nb:
	print(b, end=" ")
	a, b, cpt = b, a+b, cpt+1
print("")
