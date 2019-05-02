def word_play1():
	word = open("words.txt")

	for line in word:
		line = line.strip()
		print(line)


word_play1()
