def thousands_with_commas(param_nb):
	""" Rigth number with comma seperator """

	number_list = []
	i = 0
	while i < len(str(param_nb)):
		number_list.append(str(param_nb)[i:i+3])
		i += 3
	return ",".join(number_list)

print(thousands_with_commas(1234))
print(thousands_with_commas(123))
print(thousands_with_commas(1235678923))