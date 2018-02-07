def annograms(words, word):
	""" return a list of annograms of a given words from a list of words"""

	words = words[:]
	words_len_fliter = {w for w in words if len(w) == len(word)}
	annograms = []
	for w in words_len_fliter:
		annogram_bool = True
		for ch in w:
			if (ch.lower() not in word.lower()) or (w.count(ch.lower()) != word.lower().count(ch)):
				annogram_bool = False
		if annogram_bool:
			annograms.append(w)
	return annograms


# Main program

my_words = ["Python","train", "drive","Noytph"]
print(annograms(my_words,"thonpy"))



