def is_palindrome(word):
	if word == word[::-1]:
		print("Yes it is a palindrome")
	else:
		print("It is not a palindrome")

	
is_palindrome("bababab")

