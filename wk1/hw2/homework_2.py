import math
import random


def f1(x):
	print x + 1

def f2(x):
	return x + 1

#2.3 Math Module
def multadd(a, b, c):
	return a * b + c

def yikes(x):
	return multadd(x, pow(math.e, -x), math.sqrt(1-(pow(math.e, -x))))

assert multadd(2, 3, 4) == 10
assert multadd(0, 10, 23) == 23
assert multadd(2, 3, 4) != 14

print "sin(pi/4) + cos(pi/4)/2 is:"
print multadd(0.5, math.cos(math.pi/4), math.sin(math.pi/4))

print "ceiling(276/19) + 2 log_7(12) is:"
print multadd(2, math.log(12, 7), math.ceil(276.0/19.0))

print "yikes(5) is:"
print yikes(5)





#2.4 More Functions
def rand_divis_3(lo, hi):
	if(lo > hi):
		temp = lo
		lo = hi
		hi = temp

	num = random.randint(lo, hi)
	print num
	return (num % 3 == 0)

assert rand_divis_3(3, 3) == True
assert rand_divis_3(4, 4) == False

def roll_dice(sides, dieCount):
	while dieCount > 0:
		rand_divis_3(1, sides)
		dieCount -= 1
	print "That's all!"

roll_dice(6, 3)






#2.5 Qudratic Formula
def roots(a, b, c):
	num = pow(b, 2) - 4*a*c

	#print "Test-->", num

	if(num >= 0):
		num2 = math.sqrt(num)
		plus_b = -b + num2
		minus_b = -b - num2
		plus_b = plus_b / 2*a
		minus_b = minus_b / 2*a
	
		if(plus_b == minus_b):	
			return plus_b
		return plus_b, minus_b
	else:
		return "Complex roots detected"
		'''
		num2 = math.sqrt(-num)  #*i
		#print complex(num, 0)
		#num2 = math.sqrt(complex(num, 0.0))
		#num2 = num**0.5
		#print "Test imaginary-->", num2
		'''


print "Roots(1, 2, 3)-->", roots(1, 2, 3)
print "Roots(1, 100, 2)-->", roots(1, 100, 2)
print "Roots(1, -10, 25)-->", roots(1, -10, 25)
#print math.sqrt(0)


