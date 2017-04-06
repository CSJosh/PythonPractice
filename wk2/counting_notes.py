

#9.6 Counting
count = 0
fruit = "banana"
for char in fruit:
	if char == 'a':
		count += 1
print "'a's in 'banana'-->", count

t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
low = 1
high = 10
count = 0

for num in t:
	if low < num < high:
		count += 1
print "Numbers from 1-10, >1, <10, count-->", count

def inBucket(t, low, high):
	count = 0
	for num in t:
		if low < num <= high:
			count += 1
	return count

a = [0.0, 0.11, 0.25, 0.30, 0.43, 0.49, 0.5, 0.75, 0.80, 0.90, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]

low = inBucket(a, 0.0, 0.5)
high = inBucket(a, 0.5, 1)

print "Low-->", low
print "High-->", high

b1 = inBucket(a, 0.0, 0.25)
b2 = inBucket(a, 0.25, 0.5)
b3 = inBucket(a, 0.5, 0.75)
b4 = inBucket(a, 0.75, 1.0)

print "\nb1-->", b1, "b2-->", b2, "b3-->", b3, "b4-->", b4

numBuckets = 4
bucketWidth = 1.0 / numBuckets #width = range of each bucket non-inclusive
print '\n'
for i in range(numBuckets):
	low = i * bucketWidth
	high = low + bucketWidth
	print low, "to", high

buckets = [0] * numBuckets
bucketWidth = 1.0 / numBuckets
for i in range(numBuckets):
	low = i * bucketWidth
	high = low + bucketWidth
	buckets[i] = inBucket(a, low, high)
print "\nBuckets-->", buckets


t = [0.0, 0.25, 0.5, 0.75, 1.0]
a2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

#9.8 A single pass solution
buckets = [0] * numBuckets
for i in a:
	index = int(i * numBuckets)
	if index == len(buckets) : break
	buckets[index] +=1
print "\nBuckets2-->", buckets

'''given a list of positive integers and the number of buckets, 
   returns a list indicating how values are distributed across the buckets
'''
def histogram(alist, numBuckets):
	def maxFunction(alist):
		max_value = 0
		for n in alist:
			if n > max_value:
				mav_value = n
		return max_value 

	buckets = [0] * numBuckets
	m = (maxFunction(alist) / numBuckets)

	if m == 0:
		bucketWidth = m
	else:
		bucketWidth = 1

	for i in range(numBuckets):
		low = i * bucketWidth
		high = low + bucketWidth
		buckets[i] = inBucket(alist, low, high)
		print "Bucket[" + str(i) + "]--> Low:" + str(low) + " High:" + str(high)
	return buckets






list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [1, 2, 3, 4, 5, 20, 30, 100, 17, 42]

print "List1-->", list1
print "List1, 1 Bucket-->", histogram(list1, 1)
print "List1, 2 Buckets-->", histogram(list1, 2)
print "List1, 3 Buckets-->", histogram(list1, 3)
#print "9/2-->", 9/2
print "\nList2-->", list2
print "List2, 1 Bucket-->", histogram(list2, 1)
print "List2, 2 Buckets-->", histogram(list2, 2)
print "List2, 3 Buckets-->", histogram(list2, 3)







