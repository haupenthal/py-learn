str = 'X-DAM-Confidence: 0.8475 '

initialvalue = str.find(':') + 1
findvalue = str[initialvalue:]

number = findvalue.strip()

finalvalue = float(number)

print(finalvalue)
print(type(finalvalue))