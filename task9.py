def word_play1():
	word = open("words.txt")

	for line in word:
		line = line.strip()
		if len(line) > 20:
			print(line)


word_play1()
