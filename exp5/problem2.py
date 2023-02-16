# II. Write a Python program to find the first repeated word in a given string.

from collections import Counter

def firstRepeat(input):
	
	
	words = input.split(' ')
	
	
	dict = Counter(words)

	
	for key in words:
		if dict[key]>1:
			print (key)
			return

if __name__ == "__main__":
	input = 'Tortodise had been saying that he had been there'
	firstRepeat(input)