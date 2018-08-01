#Created by: Karthik Mahesh
#Email: karthik224488@gmail.com

import os
import sys
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("Path", help="Directory Path")
parser.add_argument("ExtA", help="Old Extension to be changed. Ex: txt")
parser.add_argument("ExtB", help="New File Extension. Ex: txt")

args = parser.parse_args()

#Regular expression with greedy match
file1 = r"(.*)(\.)(" + args.ExtA + ")"
re_obj = re.compile(file1)

for dirpath, dirnames, filenames in os.walk(args.Path):
	for file in filenames:
		oldpath = os.path.join(dirpath, file)
		new_file = re_obj.sub(r'\1\2' + args.ExtB, file)
		newpath = os.path.join(dirpath, new_file)
		os.rename(oldpath, newpath)

print('Successfully completed')
