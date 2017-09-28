file = open('testfile.txt', 'r')

for line in file.readlines():
	if 'Hello' in line:
		print line
