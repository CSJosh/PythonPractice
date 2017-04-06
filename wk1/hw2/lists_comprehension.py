


S = [x**2 for x in range(10)] #print x^2 up to 9
V = [2**i for i in range(13)] #print 2^i up to 12
M = [x for x in S if x % 2 == 0] #print the even values from S

print "(x^2)-->", S
print "(2^i)-->", V
print "Evens from (x^2)-->", M


#PRIMES
noprimes = [j for i in range(2, 8) for j in range(2*i, 100, i)]
primes = [x for x in range(2, 100) if x not in noprimes]
print "Primes-->", primes


#Lists with Strings
words = "The quick brown fox jumps over the lazy dog".split()
print "Words-->", words

word_info = [[w.upper(), w.lower(), len(w)] for w in words]
for i in word_info:
	print i

print "Now trying with lambda..."

word_info2 = map(lambda w: [w.upper(), w.lower(), len(w)], words)
for i in word_info2:
	print i
