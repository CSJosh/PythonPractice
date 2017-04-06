#14 

class Time:
	#add initilization method
	def __init__(self, hours=0, minutes=0, seconds=0):
		self.hours = hours
		self.minutes = minutes
		self.seconds = seconds

	def printTime(time): #same as 'printTime(self)'
		timeString = str(time.hours) + ':' + \
                     	     str(time.minutes) + ':' + \
                             str(time.seconds)
		print timeString
		return timeString

	def increment(self, seconds):
		self.seconds += seconds
		
		while self.seconds >= 60:
			self.seconds -= 60
			self.minutes += 1
		while self.minutes >= 60:
			self.minutes -= 60
			self.hours += 1

	def convertToSeconds(self):
		minutes = self.hours * 60 + self.minutes
		seconds = minutes * 60 + self.seconds
		return seconds

	def after(self, t2):
		if t2.hours < self.hours:
			return True
		elif t2.hours == self.hours:
			if t2.minutes < self.minutes:
				return True
			elif t2.minutes == self.minutes:
				if t2.seconds < self.seconds:
					return True	
		return False
	
time = Time()
time.hours = 11
time.minutes = 59
time.seconds = 30

assert time.printTime() == "11:59:30"
time.increment(30)
assert time.printTime() == "12:0:0"

time2 = Time()
time2.hours = 0
time2.minutes = 2
time2.seconds = 12
assert time2.printTime() == "0:2:12"
assert time2.convertToSeconds() == 132 
assert time.after(time2) == True
assert time2.after(time) == False






#14.5 Optional Arguments
'''def find(str, ch):
	index = 0
	while index < len(str):
		if str[index] == ch:
			return index
		index += 1
	return -1

def find(str, ch, start=0):
	index = start
	while index < len(str):
		if str[index] == ch:
			return index
		index += 1
	return -1
'''
#pick randomly large 'canary' value for 'end's' default
#set to length of first argument if canary persists after call
def find(str, ch, start=0, end=-141414):
	index = start
	if end == -141414:	
		end = len(str)
	while index < end:
		if str[index] == ch:
			return index
		index += 1
	return -1

string = "apple"
indexx = "01234"
assert find(string, 'a') == 0
assert find(string, 'p') == 1
assert find(string, 'p', 2) == 2
assert find(string, 'x') == -1
assert find(string, 'a', 1) == -1
assert find(string, 'e', 3) == 4
assert find(string, 'e', 4) == 4
assert find(string, 'e', 2, 4) == -1





#14.6 added __init__ to Time class
currentTime = Time(7, 33, 0) #add all argument
assert currentTime.printTime() == "7:33:0"
blank = Time() #use all default values for arguments
assert blank.printTime() == "0:0:0"
hourAndMinute = Time(3, 10) #first 2 args set; last is default
assert hourAndMinute.printTime() == "3:10:0"
minutesAndSeconds = Time(seconds=13, minutes=45) #set args out of order
assert minutesAndSeconds.printTime() == "0:45:13"





#14.7 Points Revisited using the str() method
class Point:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __str__(self):
		return '(' + str(self.x) + ', ' + str(self.y) + ')'

	def __add__(self, other):
		return Point(self.x + other.x, self.y + other.y)

	def __sub__(self, other): #self.__sub__(other) <=> self - other
		return Point(self.x - other.x, self.y - other.y)

	def __mul__(self, other): #self.__mul__(other) <=> self * other <=> dot product of self and other; e.g. p1 * p2
		return (self.x * other.x) + (self.y * other.y)

	def __rmul__(self, other): #self.__rmul__(other) <=> self * other <=> scalar multiplication; e.g. 4 * p1 (NOT p1 * 4)!!!!
		return Point(other * self.x, other * self.y)

	def reverse(self):
		self.x, self.y = self.y, self.x
#Test
p = Point(3, 4)
assert str(p) == "(3, 4)"
print p #print will use the __str__ method if its been written

#14.8 Operator Overloading
	# <updated above Point class>
#Test
p1 = Point(3, 4)
p2 = Point(5, 7)
p3 = p1 + p2  #equivalent to 'p1.__add__(p2)'
assert str(p3) == "(8, 11)"
print p3
p4 = p3 - p2
assert str(p4) == "(3, 4)"
print p4

dotProduct = p1 * p2
assert dotProduct == 43

p6 = 2 * p2
assert str(p6) == "(10, 14)"



#14.9 Polymorphism
def multadd(x, y, z):
	return x * y + z

assert multadd(1, 2, 3) == 5
assert str(multadd(2, p1, p2)) == "(11, 15)"  #2*(3, 4)=(6, 8); (6, 8)+(5, 7)=(11, 15)
assert multadd(p1, p2, 1) == 44 #p1*p2=44; 44*1 = 44


def frontAndBack(front):
	import copy
	back = copy.copy(front)
	back.reverse()
	print str(front) + str(back)

myList = [1, 2, 3, 4]
frontAndBack(myList)
#NEED TO ADD 'reverse()' TO POINT CLASS TO ALLOW USE OF: frontAndBack()
frontAndBack(p1)









