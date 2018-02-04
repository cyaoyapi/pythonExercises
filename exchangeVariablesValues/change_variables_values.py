# This program allows to exchange or to switch the values of 2 variables

# In general in other language

print("Technique used in others languages. Using temporary variable.")
print("=================================================================")
a = 10
b = 23
print("Before the exchange :")
print("a =",a," and b =",b)
c = a  # We use a temporary variable
a = b
b = c
print("After the exchange :")
print("a =",a," and b =",b)

# In python language

print("Technique used in python langage. Using multiple assignment")
print("=================================================================")
a, b = 10, 23
print("Before the exchange :")
print("a =",a," and b =",b)
b, a = a, b  # We use multiple assignment
print("After the exchange :")
print("a =",a," and b =",b)
