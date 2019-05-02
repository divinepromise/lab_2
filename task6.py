def addition_of_strings(word):
	suffix = "ing"
	if len(word) >= 3:
		if word.endswith(suffix):
			return word + "ly"
		else:
			return word + "ing"
	else:
		return word


result = addition_of_strings("willing")
print(result)
