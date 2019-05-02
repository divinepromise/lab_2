def avoids(word,letters):
	for letter in word:
		if letter in letters:
			return True
	return False



def user_input():
	forbidden_string = str(input("enter the forbidden strings  "))

	words = open("words.txt")

	for word in words:
		word=word.strip()
		if avoids(word,forbidden_string) == False:
			print (word)

user_input()
