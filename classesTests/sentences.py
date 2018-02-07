
class Sentence:
	""" A class to build sentence instance """

	def __init__(self, param_sentence):

		self.sentence = param_sentence
		self.words = param_sentence.split()

	def __str__(self):

		return " ".join(self.words)

	def __len__(self):

		return len(self.words)

	def __contains__(self, param_word):

		return param_word in self.words

	def __iter__(self):

		#return IterSentence(self.words)
		for word in self.words:
			yield word

"""class IterSentence:

	def __init__(self, param_words):

		self.words = param_words[:]

	def __iter__(self):

		return self

	def __next__(self):

		if not self.words:
			raise StopIteration
		return self.words.pop()
"""


# Main program

my_sentence = Sentence("Thanks Lord Jesus-Christ . I'm happy to succed to this test .")
print(my_sentence)
print(len(my_sentence))
print("Jesus-Christ." in my_sentence)
for word in my_sentence:
	print(f"{word}\n")
