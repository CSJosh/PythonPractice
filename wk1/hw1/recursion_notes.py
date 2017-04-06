

def rec_sum(a_list):
	if a_list == []:
		return 0
	else:
		return a_list[0] + rec_sum(a_list[1:])



def fact(n):
	if n < 0:
		return "Error, no negative numbers"
	elif n == 0:
		return 1
	else:
		return n * fact(n-1)



num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print "1+2+3+4+5+6+7+8+9+10 =", rec_sum(num_list)

print "4! =", fact(4)
print "5! =", fact(5)



#optional exercises 


#1
def mult(num1, num2):
	if num1 == 0:
		return 1
	elif num1 == 1:
		return num2
	return num2 + mult(num1-1, num2)

#Test #1
print "6*8 =", mult(6, 8)
assert mult(6, 8) == 48
assert mult(3, 0) == 0



#2
def power(base, exp):
	if exp == 0:
		return 1
	return base * power(base, exp-1)

#Test #2
print "2^16 =", power(2, 16)
assert 2**4 == power(2, 4)
assert 0**5 == power(0, 5)




#3
def range_print(n):
	if n < 0:
		return 0
	print n
	return range_print(n-1)

range_print(15)



#4
def range_print_forward(start, end):
	if start >= end:
		print end
		return start
	print start
	return range_print_forward(start+1, end)

range_print_forward(0, 15)



#5 Reverse
def reverse(phrase):
	if len(phrase) == 0:
		return ""
	return phrase[-1] + reverse(phrase[:-1])
#Test #5
assert reverse("DOG") == "GOD"
print reverse("DOG")
assert reverse("RACECAR") == "RACECAR"
print reverse("RACECAR")
assert reverse("TOMATO") == "OTAMOT"
print reverse("TOMOATO")



#6 Prime Test
def prime_test(num):
	def helper(num, j):
		if j == 1:
			return True
		return num % j != 0 and helper(num, j - 1)
	return helper(num, num-1)

#Test #6
assert prime_test(5)
assert not prime_test(6)




#7 Fibonacci
def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

#Test #7
assert fib(3) == 2
assert fib(4) == 3






