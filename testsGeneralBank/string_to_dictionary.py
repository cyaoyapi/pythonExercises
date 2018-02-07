import ast

def string_to_dictionary(param_string):

	""" Change a string formated like a dictionnary to a real dictionary """

	return ast.literal_eval(param_string)

# The program

family_dict = "{'Father':'Cyrille','Mother':'Agnès','Daughter':'Dabira'}"

print(string_to_dictionary(family_dict))