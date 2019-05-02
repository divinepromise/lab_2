def has_no_e(word):
        for letter in word:
                if letter == "e":
                        return False
        return True


def word_play2():
	words = open("words.txt")
	count1=0
	count2=0
	for line in words:
		line = line.strip()
		count2 +=1
		if has_no_e(line) == True:
			count1 +=1
			print(line)

	percentage = count1/count2 * 100
	print("words without 'e' is ",count1)
	print('Total word count',count2) 
	print("percentage of occurance of words with no 'e' is  ",int(percentage),"%",sep="" )


word_play2()
