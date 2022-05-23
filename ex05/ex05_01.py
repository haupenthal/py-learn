# Some space
# Some space

count = 0
total = 0

while True:
	string_value = input ("Enter a number: ")
	if string_value == 'done' :
			break
	try:
		tempval = float(string_value)
	except:
		print('Please enter a number')
		continue

	count = count + 1
	total = total + tempval


# Results are printed here 

print ("Last Value:",tempval)
print ("Count:",count)
print ("Running Total:",total)
print ("Running Average:",total/count)
