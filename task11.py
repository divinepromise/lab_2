def avoids(word,letters="aeiou"):
	for letter in word:
		if letter in letters:
			return True
	return False


result = avoids("bbbbbbbbbbbb")
print(result)
	
