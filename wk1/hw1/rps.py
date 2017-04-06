

r = "rock"
p = "paper"
s = "scissors"
options = {r, p, s}
p1 = " "
p2 = " "
ready = False
p1w = "Player 1 wins."
p2w = "Player 2 wins."
tie = "It's a TIE!!"


while ready == False:
	while p1 not in options:
		p1 = raw_input("Player 1? ")
		if(p1 not in options):
			print "This is not a valid object selection"
	while p2 not in options:
		p2 = raw_input("Player 2? ")
		if(p2 not in options):
			print "This is not a valid object selection"
		else:
			ready = True
		

if(p1 == r):
	if(p2 == r):
		print tie
	elif(p2 == p):
		print p2w
	else:
		print p1w
elif(p1 == p):
	if(p2 == r):
		print p1w
	elif(p2 == p):
		print tie
	else:
		print p2w
else:
	if(p2 == r):
		print p2w
	elif(p2 == p):
		print p1w
	else:
		print tie




