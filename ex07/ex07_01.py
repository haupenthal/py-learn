fhand = open('mbox-short.txt')
for fline in fhand:
	printline = fline.rstrip()
	print(printline.upper())