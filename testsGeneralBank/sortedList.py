class SortedList:

	""" Class to create a sorted list a unordered list """

	def __init__(self, param_list):

		self.sorted_list = sorted(param_list)

	def __str__(self):

		return f"{self.sorted_list}"

	def __len__(self):

		return len(self.sorted_list)

	def __contains__(self, elt):

		return elt in self.sorted_list

	def __iter__(self):

		for elt in self.sorted_list:
			yield elt


p = SortedList([1, 34, -1, 7])
print(p)
for nb in p:
	print(nb)