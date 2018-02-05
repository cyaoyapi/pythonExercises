#!/usr/bin/python3.6
#-*- coding:utf-8 -*-

# This program allows to ckeck the presence of a substring in a string entered by the user

main_string = input("Enter the string\n")
searched_string = input("What substring do you search in the main string ?\n")
if searched_string in main_string:
	print("'{}'' is in '{}'".format(searched_string, main_string))
else:
	print("'{}' is not in '{}'".format(searched_string, main_string))
