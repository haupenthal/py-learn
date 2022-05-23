myList = list()
count = 0

print('\n\nHelp me generate a list of items!\nIn each prompt, please enter a word or a number\nType "done" when finished and I will give you the resulting list.\n\n')

while True :
	count = count + 1
	listItem = input('Please enter iteman item ' + str(count) + ':')
	
	if listItem == 'done' :
		count = 0
		print('\n--------------------\nHere is the list:\n--------------------\n')
		
		# Go through the list and output each item in a separate line
		for i in myList :	
			count = count + 1
			print('- Item ' + str(count) + ':', i)
		print('\n--------------------\n--------------------\n')
		quit()

	else :
		myList.append(listItem)
