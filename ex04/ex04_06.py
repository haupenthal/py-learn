def computepay(hours, rate):
	print("In computepay", hours, rate)
	if hours > 40 :
		othours = hours - 40.0
		otpay = othours * rate * 1.5
		pay = (hours * rate) + otpay
		print("Overtime Hours:",othours)
		print("Overtime Pay:",otpay)
	else:
		pay = hours * rate
		print("Regular Compensation")
	return pay

statehours = input('Enter Hours: ')
staterate = input('Enter Rate: ')
try:
	fh = float(statehours)
	fr = float(staterate)
except:
	print("Hour and Rate values can't be expressed as words. Please use a number")
	quit()

totalcomp = computepay(fh,fr)

print("Total compensation:",totalcomp,"dollars")
