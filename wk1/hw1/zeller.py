#OPT.1 - Zeller's Algorithm

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
months = ["March", "April", "May", "June", "July", "August", "September", "October", "November", "December", "January", "February"]

fname = raw_input("Enter your first name: ")
lname = raw_input("Enter your last name: ")
valid = False

while valid == False:
	print "Enter your date of birth:"
	A = raw_input("Month as a number (Mar = 1, Feb = 12)--> ")
	dy = raw_input("Day--> ")
	yr = raw_input("Year? ")

	try:
		A = int(A)
		B = int(dy)
		C = int(yr[2:])
		D = int(yr[:2])
		valid = True
	except ValueError:
		print "Enter a valid date!"

print "A:", A, "B:", B, "C:", C, "D:", D

print fname, lname, "was born on", months[A-1], dy+",", yr

W = (13*A - 1) / 5
X = C / 4
Y = D / 4
Z = W + X + Y + B + C - 2*D
R = Z % 7

print fname, lname, "was born on", days[R]
