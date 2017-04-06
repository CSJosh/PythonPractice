
class Point:
	pass #only necessary if a compound statement has nothing in its body


blank = Point()
blank.x = 3.0
blank.y = 4.0

print blank
print "blank's id-->", id(blank)
print "blank's id in hex-->", hex(id(blank))

def printPoint(p):
	printString = '(' + str(p.x) + ', ' + str(p.y) + ')'
	#print printString
	return printString
#Test
assert printPoint(blank) == "(3.0, 4.0)"



def distance(point1, point2):
	import math 
	dx = point2.x - point1.x
	dy = point2.y - point1.y
	dsquared = dx**2 + dy**2
	result = math.sqrt(dsquared)
	return result
#Test
p2 = Point()	
p2.x = 10
p2.y = 7

print "P2-->", printPoint(p2)
print "The distance between p1", printPoint(blank), "and p2", printPoint(p2), "is", distance(blank, p2) 


#Class containing other class objects as members
class Rectangle:
	pass

box = Rectangle()
box.width = 100.0
box.height = -200.0
box.corner = Point() #corner = upper-left corner
box.corner.x = 0.0
box.corner.y = 0.0

def findCenter(box):
	p = Point()
	p.x = box.corner.x + box.width/2.0
	p.y = box.corner.y + box.height/2.0
	return p

def samePoint(p1, p2):
	return (p1.x == p2.x) and (p1.y == p2.y)

def printRec(box):
	print "Upper left corner at-->", printPoint(box.corner)
	print "Center at-->", printPoint(findCenter(box))

center = findCenter(box)
print "Center of 'box' is at-->", printPoint(center)
testCenter = Point()
testCenter.x = 50.0
testCenter.y = -100.0

#Test
assert samePoint(center, testCenter)

#12.7 Mutable Objects
def growRect(box, dwidth, dheight):
	box.width += dwidth 
	box.height += dheight

def movRect(box, dx, dy):
	box.corner.x += dx
	box.corner.y += dy
	
bob = Rectangle()
bob.width = 100.0
bob.height = 200.0
bob.corner = Point()
bob.corner.x = 0.0
bob.corner.y = 0.0

print "\nHere is Bob..."
printRec(bob)

growRect(bob, 50, 100)

print "\nHere is Bob AFTER GROW function call..."
printRec(bob)

movRect(bob, 10, 20)

print "\nHere is Bob AFTER MOVE function call..."
printRec(bob)

#12.8 Copying
def growRectNew(box, dwidth, dheight):
	import copy
	newBox = copy.deepcopy(box) #deepcopy is in copy library
	newBox.width += dwidth
	newBox.height += dheight
	return newBox

newBox = growRectNew(bob, 10, 20)
print "\nBob..."
printRec(bob)
print "\nNewBox..."
printRec(newBox)

def moveRectNew(box, dx, dy):
	import copy
	newBox = copy.deepcopy(box) #deepcopy is in copy library
	newBox.corner.x += dx
	newBox.corner.y += dy
	return newBox

newBox = moveRectNew(bob, 10, 20)
print "\nBob..."
printRec(bob)
print "\nNewBox..."
printRec(newBox)



 











