#Author: Julian Gonzalez
#python Intro lab

import re
import sys


if len(sys.argv) != 3:# Check if in args are correct if not exit 
	print("Start program with args: wordCount.py (input file) (output file)")
	exit()
	

#open arg files One for reading input and open for output
input_file = open(sys.argv[1],'r')
output_file = open(sys.argv[2],'w')

#store words from input
wordList = {}


for line in input_file:

	for word in re.split('[^a-zA-Z]', line):# only get words in the alphabet 
		word = word.lower()

		if word in wordList:#if word is already in list increment counter
			wordList[word] +=1

		else:
			if word != "":#if word not in list add to list
				wordList[word] = 1
	

input_file.close()

sortedWords = sorted(wordList.items())#get items from list then sort

for line in sortedWords:# input items into new output file
    output_file.write(line[0] + " " + str(line[1]) + '\n')#fixed

output_file.close()