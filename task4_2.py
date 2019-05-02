
def reverse_2(string):
	hold = ""

	for i in string:
		hold = i + hold

	print(hold)

reverse_2("battery")
