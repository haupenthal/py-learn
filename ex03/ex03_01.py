hour = input('Enter Hours: ')
rate = input('Enter Rate: ')
fh = float(hour)
fr = float(rate)
try:
	pay = fh * fr
except:
	print("Please use numbers")


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
