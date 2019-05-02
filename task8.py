def rotate_letter(letter,n):
	if letter.isupper():
		start = ord("A")
	elif letter.islower():
		start = ord("a")
	else:
		start = ord(letter)


	new_shift = ord(letter) + n
	first = new_shift - start
	second = first % 26
	third = second + start
	new_letter = chr(third)

	return new_letter

def word_shift(word,n):
	holder = ""
	for letter in word:
		letter = rotate_letter(letter,n)
		holder = holder + letter
	return holder


result = word_shift("cheer",7)
print(result)

