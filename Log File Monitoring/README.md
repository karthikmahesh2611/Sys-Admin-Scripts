* The script can used to monitor log files for a particular string sequence.
* Script is cross platform and is tested on both Windows and Linux systems
* Outputs number of matches found
* Script remembers the number of lines already read and the file inode number so that it processes the file from the line it last left
* Can be integrated with monitoring tools like zabbix and nagios
* If the file inode number changes or if the lines are purged the script resets the line_read and starts reading from begining.
* The script will generated files named file_data.bat to store the line_numbers read and file inode number (Do not modify delete these files)
* The 'file path' and the 'regex string' can be provided in the configs.py file
