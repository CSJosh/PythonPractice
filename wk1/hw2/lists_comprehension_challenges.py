

#1
def give_ints_back(mixedList):
	int_list = [x for x in mixedList if isinstance(x, int)]
	return int_list

#Test
a = 'a'
num = 10
string = "here is a string"
num2 = 37
string2 = "la la la"

mixed_list = []
mixed_list.append(a)
mixed_list.append(num)
mixed_list.append(string)
mixed_list.append(num2)
mixed_list.append(string2)

print "Mixed list-->", mixed_list
print "Ints removed-->", give_ints_back(mixed_list)
assert give_ints_back(mixed_list) == [10, 37]



#2
#y = x^2 + 1
def list_comp():
	sol_list = [[x, y] for x in range(-5, 6) for y in range(11) if y == (x**2 + 1)]
	print "Solutions for y = x^2 + 1"
	for j in sol_list:
		print j
#Test #2
list_comp()



#3 r^2 = x^2 + y^2
def circle_radius(r):
	sol_list = [[x, y] for x in range(-5, 6) for y in range(11) if (r**2) == ((x**2)+(y**2))]
	print "Solutions for " + str(r) + "^2 = x^2 + y^2"
	for j in sol_list:
		print j
#Test #3
circle_radius(5) 


#4









