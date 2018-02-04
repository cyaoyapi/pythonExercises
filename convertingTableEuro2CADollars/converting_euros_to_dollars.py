# This program display a converting table, Euros to Canada Dollars
# 1 Euro = 1.65 dollar(s)

print("Converting table, Euro to canada dollar")
print("============================================")
euro_term, dollar_term = 1, 1.65 
while euro_term <= 16384:
	print(euro_term,"euro(s) =",round(dollar_term, 2),"dollar(s)")
	euro_term, dollar_term = euro_term * 2, dollar_term * 2




