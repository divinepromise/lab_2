def is_abecedarian(word):
	i=0
	while i < len(word):
		if word[i] <= word[i+1]:
			return True
		else:
			return False
	i+=1



result = is_abecedarian("zabcdefghjkl")
print (result)
