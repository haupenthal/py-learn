count = 0
word = input('Enter a word: ')
wordlengh = len(word)

def letter_seek() :
	while True:
		count = 0
		seekletter = input('Choose a letter to search for in ' + str(word) + ': ')

		if seekletter == 'done' :
			break
		else:
			for letter in word :
				if letter == seekletter :
					count = count + 1
			if count == 0 :
				print('There are no letters',seekletter,'in',word)
			else : print('There are a total of',count,'letters',seekletter,'in',word)


for letter in word :
		if letter == 'a' :
			count = count + 1

print(word,'has',wordlengh,'characters')
print('There are a total of',count,'letters a in',word)

letter_seek()
