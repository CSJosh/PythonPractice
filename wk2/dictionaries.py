

#English to Spanish
eng2sp = {}
eng2sp['one'] = 'uno'
eng2sp['two'] = 'dos'
print "eng2sp-->", eng2sp


#Can also do...
eng2sp = {'one':'uno', 'two':'dos', 'three':'tres'}
print "eng2sp-->", eng2sp
print "eng2sp['two']-->", eng2sp['two']
print "eng2sp.keys()-->", eng2sp.keys()
print "eng2sp.values()-->", eng2sp.values()
print "eng2sp.items()-->", eng2sp.items()
print "eng2sp.has_key('one')-->", eng2sp.has_key('one')
print "eng2sp.has_key('duck')-->", eng2sp.has_key('duck')

alias = eng2sp
copy = eng2sp.copy()
print "alias-->", alias
print "copy-->", copy
print "eng2sp-->", eng2sp

print "\nalias['one'] = 'cookie'"
alias['one'] = 'cookie'

print "\nalias-->", alias
print "copy-->", copy
print "eng2sp-->", eng2sp



#fibonacci
previous = {0:1, 1:1}

def fib(n):
	if previous.has_key(n):
		return previous[n]
	#else
	newValue = fib(n-1) + fib(n-2)
	previous[n] = newValue
	return newValue

print "Fib(1)-->", fib(1)
print "Fib(2)-->", fib(2)
print "Fib(5)-->", fib(5)
print "Fib(10)-->", fib(10)
print "Fib(50)-->", fib(50)




#counting letters
letterCounts = {}
for letter in "Mississippi":
	letterCounts[letter] = letterCounts.get(letter, 0) + 1 # '0' is the value get() returns if 'letter' is not in the dictionary
print "Letter counts-->", letterCounts
letter_items = letterCounts.items()
sorted_letters = letter_items.sort()
print "Sorted-->", sorted_letters









