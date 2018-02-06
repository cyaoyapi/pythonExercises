""" This program display a list of palindromes """

numbers = (x**2 for x in range(1000))
palindromes = (x for x in numbers if str(x) == str(x)[::-1])
print(list(palindromes))
