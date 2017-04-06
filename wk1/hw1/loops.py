



#Exercise 1.8

#1
for x in range(2, 11):
	print "1/" + str(x) + " ==> " + str(1/float(x))

#2
num = raw_input("Enter a number to count down from: ")
num = int(num)
while(num > -1):
	print "Count Down ==>", num
	num -= 1

#3
print "\nExponent calculation time ==> base^exponent"
base = raw_input("Enter the base-->")
exp = raw_input("Enter the exponent-->")
try:
	base = int(base)
	exp = int(exp)
except ValueError:
	print "Setting base and exponent to 2 since you didn't provide real numbers"
	base = exp = 2

if isinstance(base, int) and isinstance(exp, int):
	print "Thanks for providing two ints!"

print "The calculation of " + str(base) + '^' + str(exp) + " is ==> " + str(base**exp)


#4
num = 1
while num % 2 != 0:
	num = raw_input("Enter an even number: ")
	try:
		num = int(num)
	except ValueError:
		print "C'mon are you even trying...???"
		num = 1

	if(num % 2 != 0):
		print "In case you need an example...2...is an even number..."

print "Finally, thanks for entering", num


	


