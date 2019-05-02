def rotate_letter(letter,n):
	if letter.isupper():
		start = ord("A")
	elif letter.islower():
		start = ord("a")
	else:
		start = ord(letter)


	new_shift = start + n
	first = new_shift - start
	second = first % 26
	third = second + start
	new_letter = chr(third)

	return new_letter


result = rotate_letter("a",9)
print(result)

