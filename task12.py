def uses_all(word,letters):
	for i in letters:
		if i in word:
			return True
	return False



result = uses_all("bzxzxcy","aeiou")
print(result)
