#Created By: Karthik Mahesh
#Email: karthik224488@gmail.com

'''
Script to monitor log files for matching strings.
Script will store the log file inode number and the number of lines processed using .bat files
Will output number of matches found
'''

import os
import shelve
import hashlib
import configs
import sys
import re



def check_inode():
	global inode
	global line_num
	if (os.stat(configs.file_path).st_ino == inode):
		return		
	else:
		inode = os.stat(configs.file_path).st_ino
		line_num = 1


def check_lines():
	global inode
	global line_num
	my_file.seek(0)

	if (sum(1 for line in my_file) < (line_num-1)):
		line_num = 1
		my_file.seek(0)
	else:
		my_file.seek(0)


def create_regex_obj(regex):
	re_obj = re.compile(regex)
	return re_obj


def jump_lines():
	my_file.seek(0)
	num = 2

	if line_num >= num:
		for line in my_file:
			if line_num == num:
				break
			num = num + 1


def count_string_match():
	count = 0
	global line_num

	for line in my_file:
		line_num += 1
		match = re_object.search(line)
		if (match):
			count += 1
	return count





if __name__ == '__main__':
	#Open the shelve file
	try:
		values = shelve.open('file_data.dat')
		inode = values.setdefault('inode', None)
		line_num = values.setdefault('line_num', 0)
	except:
		print("Error in opening file 'file_data.dat'")
		sys.exit(1)


	try:
		my_file = open(configs.file_path)
	except:
		print("Error in opening file {}".format(configs.file_path))
		sys.exit(1)

	#Check if the file inode is the same
	check_inode()

	#Check if the number of lines in the file is equal or more than lines already read
	check_lines()


	#Create a search string regex
	re_object = create_regex_obj(configs.search_string)

	#Jump the lines already read
	jump_lines()

	matches = count_string_match()
	values['inode'] = inode
	values['line_num'] = line_num

	print(matches)
	values.close()
	my_file.close()
	sys.exit(0)



#Used the setdefault method instead of the below code lines	
'''
	try:
		values['inode']
	except KeyError:
		values['inode'] = None
	finally:
		inode = values['inode']

	try:
		values['line_num']
	except KeyError:
		values['line_num'] = None
	finally:
		line_num = values['line_num']
'''

		
	

	
	












