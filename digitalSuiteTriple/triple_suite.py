# This program display a sequence of 12 terms. Each term is the triple of the previous term.

print("Suite of 12 terms that each term is the triple of the previous term.")
print("===========================================================================")
print("1", end=" ")
number_of_terms, previous_term = 1, 1
while number_of_terms <= 12:
	print(previous_term * 3, end=" ")
	number_of_terms, previous_term = number_of_terms + 1, previous_term * 3
print("")



