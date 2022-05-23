fname = input('Enter a file name: ')

try:
	fhand = open(fname)
except:
	if fname == 'na na boo boo' :
		print("NA NA BOO BOO TO YOU - You have been punk'd!")
	else:
		print('File cannot be opened:',fname)
	quit()

count = 0
totalvalue = 0

print('Selected file',fhand)

for fline in fhand:	
	fline = fline.rstrip() # strips extra spaces

	# way to skip UNWANTED lines
	if not fline.startswith('X-DSPAM-Confidence:'):
		continue
	# now I can work with WANTED lines
	colon_pos = fline.find(':') + 1 # finds the colon position and adds one to the position
	lvalue = fline[colon_pos:] # define the line value
	computvalue = float(lvalue) # makes it a float variable. Could have used "strip" to strip spaces before.
	
	# additions and counters

	count = count + 1
	totalvalue = totalvalue + computvalue

print('Line count:',count)
print('Total SPAM Confidence:',totalvalue)
print('Average spam confidence:',totalvalue/count)
