

def palindromes(word):
	length = len(word)
	#print "\nTesting-->", word
	if length == 1 or length == 0:
		return True

	return ( (word[0] == word[length-1]) and palindromes(word[1:length-1]) )

assert palindromes("a") == True
print "*************************"
assert palindromes("aba") == True
print "*************************"
assert palindromes("abba") == True
print "*************************"
assert palindromes("able was i ere i saw elba") == True
print "*************************"
assert palindromes("the") == False
