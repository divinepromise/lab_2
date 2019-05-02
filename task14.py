def triple_double_count(word):
	
	count = 0
	index = 0
	while index < len(word)-1:
		if word[index] == word[index+1]:
			count += 1
			if count == 3:
				return True
			index+=2
		else:
			index += 1
	return False


def word_play3():
	words = open("words.txt")

	for  word in words:
		word=word.strip()
		if triple_double_count(word) == True:
			print(word)


result = word_play3()
print(result)
