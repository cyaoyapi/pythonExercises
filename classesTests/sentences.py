
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


# Main program

my_sentence = Sentence("Thanks Lord Jesus-Christ . I'm happy to succed to this test .")
print(my_sentence)
print(len(my_sentence))
print("Jesus-Christ." in my_sentence)
