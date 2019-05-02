def has_no_e(word):
	for letter in word:
		if letter == "e":
			return False
	return True

result = has_no_e("bnebabab")
print(result)

