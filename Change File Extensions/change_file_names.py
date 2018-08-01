#Created by: Karthik Mahesh
#Email: karthik224488@gmail.com

import os
import sys
import argparse
import re

#Get the required arguments from the user which includes:
# Directory Path
# Old File Extension
# Nex File Extension
parser = argparse.ArgumentParser()
parser.add_argument("Path", help="Directory Path")
parser.add_argument("ExtA", help="Old Extension to be changed. Ex: txt")
parser.add_argument("ExtB", help="New File Extension. Ex: txt")

args = parser.parse_args()

#Regular expression with greedy match filenames.ext
file1 = r"(.*)(\.)(" + args.ExtA + ")"
re_obj = re.compile(file1)

#os.walk will find all directories and files in the mentoned directory path
for dirpath, dirnames, filenames in os.walk(args.Path):
	for file in filenames:
		oldpath = os.path.join(dirpath, file)
		#Subsitute the new extenison using re 'sub' method
		new_file = re_obj.sub(r'\1\2' + args.ExtB, file)
		newpath = os.path.join(dirpath, new_file)
		#Rename the files
		os.rename(oldpath, newpath)

#Script completed successfully
print('\nSuccessfully completed')
