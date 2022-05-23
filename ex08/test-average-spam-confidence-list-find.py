fname = input('\nEnter a file name: ')

try:
	fhand = open(fname)
except:
	if fname == 'na na boo boo' :
		print("\n--------------------\nNA NA BOO BOO TO YOU - You have been punk'd!\n--------------------\n")
	else:
		print('File cannot be opened:',fname)
	quit()

count = 0
totalvalue = 0

print('\n--------------------\nSelected file =',fhand,'\n--------------------\n')

for fline in fhand:	
	fline = fline.rstrip() # strips extra spaces

	# way to skip UNWANTED lines
	if not fline.startswith('X-DSPAM-Confidence:') : continue
	# now I can work with WANTED lines

	values = fline.split() # splits the line into a list using space as a delimeter
	computvalue = float(values[1]) # defines value as the second (0,1...) item and makes it a float variable.
	
	# additions and counters

	count = count + 1
	totalvalue = totalvalue + computvalue

print('Line count:',count)
print('Total SPAM Confidence:',totalvalue)
print('Average spam confidence:',totalvalue/count)
print('\n--------------------\n--------------------\n')
