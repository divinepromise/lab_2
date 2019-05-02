def has_no_e(word):
	index=1
	while index < len(word):
		if word[index] != "e":
			return True
		else:
			return False


result = has_no_e("bsnana")
print(result)
