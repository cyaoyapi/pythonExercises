# This program display the firt 20 terms of the multiplication of 7. Add (*) when the term is a mulptuple of 3.

print("Multiplication table of 7 === First 20 terms")
print("================================================")
term = 1
while term < 21:
	result = 7 * term
	print(result, end="")
	if result % 3 == 0:
		print("(*)", end="")
	print(end=" ")
	term += 1
print("")
