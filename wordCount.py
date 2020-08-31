import re
import sys


if len(sys.argv) != 3:
	print("Start program with args: wordCount.py (input file)  (output file)")
	exit()
	


input_file = open(sys.argv[1],'r')
output_file = open(sys.argv[2],'w')


wordList = {}


for line in input_file:

	for word in re.split('[^a-zA-Z]', line):
		word = word.lower()

		if word in wordList:
			wordList[word] +=1
		else:
			if word != ""
				wordList[word] = 1
	
	input_file.close()

sortedWords = sorted(iter(wordList.keys()))#

for line in sortedWords:
    output_file.write(line[0] + " " + str(line[1]) + '\n')