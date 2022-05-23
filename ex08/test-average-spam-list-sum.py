fname = input('\nEnter a file name: ')

try:
	fhand = open(fname)
except:
	if fname == 'na na boo boo' :
		print("\n--------------------\nNA NA BOO BOO TO YOU - You have been punk'd!\n--------------------\n")
	else:
		print('File cannot be opened:',fname)
	quit()

vList = []

print('\n--------------------\nSelected file =',fhand,'\n--------------------\n')

for fline in fhand:	
	fline = fline.rstrip() # strips extra spaces

	# way to skip UNWANTED lines
	if not fline.startswith('X-DSPAM-Confidence:') : continue
	# now I can work with WANTED lines
	
	lineList = fline.split() # splits the line into a list using space as a delimeter
	vList.append(lineList[1])
	vList = list(map(float, vList))

# print(vList)
# Print additions and counters

print('Ocurrences: ', str(len(vList)))
print('Total SPAM Confidence: %d' % sum(vList))
print('Average spam confidence: ', str(sum(vList)/len(vList)))
print('\n--------------------\n--------------------\n')
