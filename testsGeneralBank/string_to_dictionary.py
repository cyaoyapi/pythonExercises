import ast # Or import json

def string_to_dictionary(param_string):

	""" Change a string formated like a dictionnary to a real dictionary """

	return ast.literal_eval(param_string) # return json.loads(param_string)


# The program

    # If we use json, the delimiter must be simple quotes ''
family_dict = "{'Father':'Cyrille','Mother':'Agnès','Daughter':'Dabira'}" 


print(string_to_dictionary(family_dict))