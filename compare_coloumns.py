'''
This scripts will compare and list objects in FileA that are not there in in FileB and vice versa.
version 2: Added options for case insensitive and reverse comparison
'''

import sys
import argparse



def compare_list(file_a,file_b):
	for line1 in file_a:
		file_b.seek(0)
		for line2 in file_b:
			if(args.insensitive):
				word1 = str(line1).strip('\n').strip(' ').lower()
				word2 = str(line2).strip('\n').strip(' ').lower()
			else:
				word1 = str(line1).strip('\n').strip(' ')
				word2 = str(line2).strip('\n').strip(' ')

			if(word1==word2):
				break
		else:
			print(word1)


if __name__ == '__main__':


	parser = argparse.ArgumentParser()
	parser.add_argument("-i","--insensitive", help="Case Insestive compare",action="store_true")
	parser.add_argument("-r","--reverse", help="Reverse Compare",action="store_true")
	parser.add_argument("FileA", help="FileName or path to fileA")
	parser.add_argument("FileB", help="FileName or path to fileB")

	args = parser.parse_args()

	file1 = open(args.FileA,mode='r')
	file2 = open(args.FileB,mode='r')

	if(args.reverse):
		compare_list(file2,file1)
	else:
		compare_list(file1,file2)


	file1.close()
	file2.close()





