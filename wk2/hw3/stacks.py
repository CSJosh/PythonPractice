

class Stack:
	data = []
	currentIndex = 0
	currentSize = 0
	
	def __init__(self, size=5):
		if size < 0:
			size *= -1
		self.data = [0] * size
		self.currentIndex =  0  
		self.currentSize = size

	def push(self, to_add):
		import copy

		if self.currentIndex < self.currentSize:
			self.data[self.currentIndex] = to_add
			self.currentIndex += 1
		else:
			tempIndex = 0
			temp = [0] * (2*self.currentSize)
			
			for num in self.data:
				temp[tempIndex] = num
				tempIndex += 1
						
			self.currentSize *= 2
			self.data = copy.copy(temp)
			self.data[self.currentIndex] = to_add
			self.currentIndex += 1
		
	def pop(self):
		if self.currentIndex == 0:
			return "<empty stack>"
		else:
			self.currentIndex -= 1
			return self.data[self.currentIndex + 1]

	def getData(self):
		if self.currentIndex == 0:
			return "<empty stack>"
		else:
			return self.data[:self.currentIndex]


#Testing
stack = Stack()
print "stack-->", stack.getData()
print "pushing a 5..."
stack.push(5)
print "stack-->", stack.getData()

print "popping last value (5)..."
stack.pop()
print "stack-->", stack.getData()

print "pushing a 101..."
stack.push(101)
print "stack-->", stack.getData()
print "pushing a 6..."
stack.push(6)
print "stack-->", stack.getData()
print "pushing a 7..."
stack.push(7)
print "stack-->", stack.getData()
print "pushing a 8..."
stack.push(8)
print "stack-->", stack.getData()
print "pushing a 9..."
stack.push(9)
print "stack-->", stack.getData()
print "pushing a 10..."
stack.push(10)
print "stack-->", stack.getData()
print "pushing an 11..."
stack.push(11)
print "stack-->", stack.getData()
print "pushing a 12..."
stack.push(12)
print "stack-->", stack.getData()
print "pushing a 13..."
stack.push(13)
print "stack-->", stack.getData()
print "pushing a 14..."
stack.push(14)
print "stack-->", stack.getData()
print "pushing a 15..."
stack.push(15)
print "stack-->", stack.getData()
print "pushing a 16..."
stack.push(16)
print "stack-->", stack.getData()









