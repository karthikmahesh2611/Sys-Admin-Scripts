'''
Script to check root password of server from a list of passwords

Usage check_password.py host_file password_file output_file
'''

import paramiko
import logging
import sys
import csv

if not len(sys.argv) == 4:
	print(__doc__)
	sys.exit(1)


logging.basicConfig(filename = "logs.txt", level = logging.DEBUG, filemode = 'w', format = "%(levelname)s %(asctime)s - %(message)s")

logger = logging.getLogger()

host_file = str(sys.argv[1])
pass_file = str(sys.argv[2])
out_file = str(sys.argv[3])

file1 = open(host_file)
file2 = open(pass_file)
file3 = open(out_file,mode='w')
f_writer = csv.writer(file3)
f_writer.writerow(['Hostname','Password'])

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


for line1 in file1:
	file2.seek(0)
	for line2 in file2:
		try:
			ssh.connect(str(line1).strip('\n'), '22', 'root', str(line2).strip('\n'))
		except:
			logger.info("Password {} did not work for host {}".format(str(line2).strip('\n'),str(line1).strip('\n')))
		else:
			f_writer.writerow([str(line1).strip('\n'), str(line2).strip('\n')])
			break
	ssh.close()


file1.close()
file2.close()
file3.close()
print('Script completed')
