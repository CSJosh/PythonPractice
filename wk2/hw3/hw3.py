# Name:
# Section:
# hw3.py

##### Template for Homework 3, exercises 3.1 - ######

# **********  Exercise 3.1 ********** 

# Define your function here
##### YOUR CODE HERE #####
def list_intersection(list1, list2):
	returnList = []
	for num in list1:
		if num in returnList: 
			continue
		elif num in list2:
			returnList.append(num)
	return returnList

# Test Cases for Exercise 3.1
##### YOUR CODE HERE #####
list1 = [1, 2, 3, 4, 5]
list2 = [1, 1, 5, 6, 7, 8]
list3 = [10, 11, 12]
commonList = list_intersection(list1, list2)
print commonList
assert str(commonList) == "[1, 5]"
commonList = list_intersection(list1, list3)
print commonList
assert str(commonList) == "[]"










# **********  Exercise 3.2 **********
class Ball:   #UNUSED CLASS...just for practice
	def __init__(self, x=0, y=0, r=0):
		self.x = x
		self.y = y
		self.r = r
	
	def distance(self, ball2):
		import math
		dx = ball1.x - ball2.x
		dy = ball1.y - ball2.y
		dsquared = dx**2 + dy**2
		return math.sqrt(dsquared)

	def ball_collide(self, ball2):
		ball_dist = self.distance(ball2)
		return (ball_dist <= (self.r + ball2.r))



# Define your function here NON-Class version
#TRUE if the balls collide; False otherwise
def ball_collide(ball1, ball2):
	import math
	dx = ball1[0] - ball2[0]
	dy = ball1[1] - ball2[1]
	dsquared = dx**2 + dy**2
	result = math.sqrt(dsquared)
	return (result <= (ball1[2] + ball2[2]))

# Test Cases for Exercise 3.2
print ball_collide((0, 0, 1), (3, 3, 1)) # Should be False
print ball_collide((5, 5, 2), (2, 8, 3)) # Should be True
print ball_collide((7, 8, 2), (4, 4, 3)) # Should be True












# **********  Exercise 3.3 **********
#NOTE use of the GLOBAL dictionary, 'my_classes'

# Define your dictionary here - populate with classes from last term
my_classes = {'CS410':'Intro to Network Security', 'CS487':'Database Implementation', 'CS421':'Capstone I'}

def add_class(class_num, desc):
	##### YOUR CODE HERE #####
	my_classes[class_num] = desc

# Here, use add_class to add the classes you're taking next term
add_class('CS410a', 'Introduction to Python')

def print_classes(course):
	##### YOUR CODE HERE #####
	courseNums = my_classes.keys()
	count = 0;

	for key in courseNums:
		if key[:5] == course:
			count += 1
			print key + ' - ' + my_classes[key]
	if count == 0:
		print "No course",  course, "classes taken" 

# Test Cases for Exercise 3.3
print "Test1...CS410"
print_classes('CS410')
print "Test2...CS421"
print_classes('CS421')
print "Test2...PH202"
print_classes('PH202')












# **********  Exercise 3.4 **********

NAMES = ['Alice', 'Bob', 'Cathy', 'Dan', 'Ed', 'Frank',
                 'Gary', 'Helen', 'Irene', 'Jack', 'Kelly', 'Larry']
AGES = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]

# Define your functions here
def combine_lists(key_list, val_list):
	if len(key_list) != len(val_list):
		print "Error <combine_lists>: args should be the same length"
		return {}
	#else
	comb_dict = {}
	index = 0

	for key in key_list:
		comb_dict[key] = val_list[index]
		index += 1

	return comb_dict


combined_dict = combine_lists(NAMES, AGES) # Finish this line...
print combined_dict
print 'Alice' in combined_dict   #True
print 21 in combined_dict   #False

def people(age):
	# Use combined_dict within this function...
	names = combined_dict.keys()
	ages = combined_dict.values()
	people = []
	count = 0
	
	for num in ages:
		if num == age:
			people.append(names[count])
		count += 1
	
	return people 


#aside reminder
list3 = [1, 2]
list3.append(3)
print list3 #prints--> [1, 2, 3]	
##############
print "People(19)-->", people(19)


#Test Cases for Exercise 3.4 (all should be True)
print 'Dan' in people(18) and 'Cathy' in people(18)
print 'Ed' in people(19) and 'Helen' in people(19) and\
       'Irene' in people(19) and 'Jack' in people(19) and 'Larry'in people(19)
print 'Alice' in people(20) and 'Frank' in people(20) and 'Gary' in people(20)
print people(21) ==   ['Bob']
print people(22) ==   ['Kelly']
print people(23) ==   []











# **********  Exercise 3.5 **********

def zellers(month, day, year):
	##### YOUR CODE HERE #####
	months = { "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12, "January":1, "February":2 }
	
	days = ["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday"]
	
	if month not in months:
		return "Enter a valid date" 

	year = str(year) #set year to a string
	A = months[month] #A = number value for the month
	B = day #b is an int
	C = int(year[2:]) #C = int
	D = int(year[:2]) #D = int
	
	print "A:", A, "B:", B, "C:", C, "D:", D
	print "Date provided-->", A, str(day) +  ",", year

	W = (13*A - 1) / 5
	X = C / 4
	Y = D / 4
	Z = W + X + Y + B + C - 2*D
	R = Z % 7

	print days[R]	
	return days[R] 



# Test Cases for Exercise 3.5
print zellers("March", 10, 1940) == "Sunday" # This should be True
print zellers("April", 4, 2017) == "Tuesday" #True
##### YOUR CODE HERE #####




# ************ 3.6 Class Queue ******************
class Queue:
	line = []

	def __init__(self, to_add=[]):
		import copy
		self.line = copy.copy(to_add)

	def insert(self, to_add):
		self.line.append(to_add)

	def remove(self):
		if len(self.line) == 0:
			print "The queue is empty"
		else:
			val = self.line[0]
			self.line = self.line[1:]
			return val	

queue = Queue([1, 2, 3]) #<empty queue>
queue.insert(5) #5
queue.insert(6) #6->5
print queue.remove() #6
queue.insert(7) #7->6
print queue.remove() #7
print queue.remove() #<empty queue>
queue.remove() #get empty message
