fname = input('\nEnter a file name: ')

try:
	fhand = open(fname)
except:
	if fname == 'na na boo boo' :
		print("\n--------------------\nNA NA BOO BOO TO YOU - You have been punk'd!\n--------------------\n")
	else:
		print('File cannot be opened:',fname)
	quit()

myList = []

for line in fhand :
	words = line.split()
	for wd in words :
		if wd not in myList :
			myList.append(wd)

myList.sort()
print(myList)