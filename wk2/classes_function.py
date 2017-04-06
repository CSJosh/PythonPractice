import copy

#Time records the time of day
class Time:
	pass

time = Time()
time.hours = 11
time.minutes = 59
time.seconds = 30

def printTime(time):
	timeString = str(time.hours) + ':' + str(time.minutes) + ':' + str(time.seconds)
	print timeString
	return timeString

assert printTime(time) == "11:59:30"

def after(before, after):
	if before.hours < after.hours:
		return True
	elif before.hours == after.hours:
		if before.minutes < after.minutes:
			return True
		elif before.minutes == after.minutes:
			if before.seconds < after.seconds:
				return True
	
	return False

t2 = Time()
t2.hours = 11
t2.minutes = 59
t2.seconds = 40
assert printTime(t2) == "11:59:40"
assert after(time, t2) == True
assert after(t2, time) == False
t3 = copy.copy(t2)
t2.hours = 1
assert printTime(t3) == "11:59:40"
assert printTime(t2) == "1:59:40"


#13.2 Pure Functions - don't modify arguments, but return a new object
def addTime(t1, t2):
	rsum = Time()
	rsum.hours = t1.hours + t2.hours
	rsum.minutes = t1.minutes + t2.minutes
	rsum.seconds = t1.seconds + t2.seconds
	if rsum.seconds >= 60:
		rsum.seconds -= 60
		rsum.minutes += 1
	if rsum.minutes >= 60:
		rsum.minutes -= 60
		rsum.hours += 1
	return rsum
	
assert printTime(addTime(t2, t3)) == "13:59:20"

#13.3 MOdifiers - functions that MODIFY the arguments
def increment(time, seconds):
	time.seconds += seconds
	while time.seconds >= 60:
		time.seconds -= 60
		time.minutes += 1
	while time.minutes >= 60:
		time.minutes -= 60
		time.hours += 1

increment(t2, 20)
assert printTime(t2) == "2:0:0"

def increment2(time, seconds):
	time.seconds += seconds
	if time.seconds >= 60:
		time.minutes += time.seconds / 60
		time.seconds = time.seconds % 60

	if time.minutes >= 60:
		time.hours += time.minutes / 60
		time.minutes = time.minutes % 60

t2.hours = 11
t2.minutes = 59
t2.seconds = 40
increment2(t2, 20)
assert printTime(t2) == "12:0:0" 

def convertToSeconds(t):
	minutes = t.hours * 60 + t.minutes
	seconds = minutes * 60 + t.seconds
	return seconds

test = Time()
test.hours = 0
test.minutes = 2
test.seconds = 30
assert convertToSeconds(test) == 150
assert convertToSeconds(t2) == 43200

def makeTime(seconds):
	time = Time()
	time.hours = seconds // 3600
	time.minutes = (seconds % 3600) // 60
	time.seconds = seconds % 60
	return time

def addTime2(t1, t2):
	seconds = convertToSeconds(t1) + convertToSeconds(t2)
	return makeTime(seconds)

assert printTime(addTime2(t2, test)) == "12:2:30"

def increment3(time, seconds):
	secondsSum = convertToSeconds(time) + seconds
	return makeTime(secondsSum)

#test = 0:2:30
test = increment3(test, 40)
assert printTime(test) == "0:3:10"

