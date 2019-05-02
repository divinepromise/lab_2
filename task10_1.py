def has_no_e(word):
        for letter in word:
                if letter == "e":
                        return False
        return True


def word_play2():
	words = open("words.txt")
	
	for line in words:
		line = line.strip()
		if has_no_e(line) == True:
			print(line)

word_play2()
