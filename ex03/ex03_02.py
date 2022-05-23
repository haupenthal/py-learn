hour = input('Enter Hours: ')
rate = input('Enter Rate: ')
try:
	fh = float(hour)
	fr = float(rate)
except:
	if type(hour) != int:	
		print("Hour values can't be expressed as words such as '",hour,"'. Please use a number")
	elif type(rate) != int:
			print("Rate values can't be expressed as words such as '",rate,"'. Please use a number")
	else :
		print("Hour and Rate values can't be expressed as words such as '",hour,"or",rate,"'. Please use a number")
	quit()

pay = fh * fr

# print(fh, fr)

if fh > 40 :
	oth = fh - 40.0
	otp = oth * fr * 1.5
	print("Overtime Hours:",oth)
	print("Overtime Pay:",otp)
	print("Total Compensation:",pay + otp,"dollars")
else :
	print("Regular Compensation")
	print("Pay:",pay,"dollars")
print("All Done")
