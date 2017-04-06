

def getIndex(letterList, letter):
	if letter.isalpha() == False or len(letterList) < 1:
		return -1

	idx = 0
	for x in letterList:
		if x == letter:
			return idx
		else:
			idx += 1
	return -1


def getLetter(letterList, idx):
	if len(letterList) < 1 or idx >= len(letterList):
		return '$'

	return letterList[idx]



def encrypt(phrase, shft):
	ephrase = ""
	lows = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	upps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

	if shft > 25:
		 shft %= 26

	for c in phrase:
		if c.isalpha():
			if c.isupper():
				i = getIndex(upps, c)
				ephrase += getLetter(upps, (i+shft)%26)
			else:
				i = getIndex(lows, c)
				ephrase += getLetter(lows, (i+shft)%26)
		else:
			ephrase += c

	return ephrase







phrase = raw_input("Enter a phrase to encode: ")

ephrase = ""

for c in phrase:
	ephrase += c

print "Output1-->", ephrase

ephrase = ""

for c in phrase:
	if c.isalpha():
		if c.isupper(): 
			ephrase += 'X'
		else: 
			ephrase += 'x'
	else:
		ephrase += c

print "Output2-->", ephrase

validInt = False

while validInt == False:
	num = raw_input("Enter the shift value: ")
	
	try:
		num = int(num) 
		validInt = True
	except ValueError:
		print "Enter a valid integer..."

print "You entered the phrase <", phrase, "> which we will encrypt by shifting each letter", num, "times"

ephrase = encrypt(phrase, num)

print "Output3-->", ephrase







