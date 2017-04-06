

def maxval(some_list):
	max_val = None
	for val in some_list: 
		if val > max_val:
			max_val = val
	return max_val
#test
assert maxval([1, 5, 3, 4]) == 5
assert maxval([5, 3, 7, 5]) == 7



def alllessthansix(some_list):
	return maxval(some_list) < 6
#Test
assert alllessthansix([1, 2, 3, 4, 5]) == True
assert alllessthansix([1, 2, 3, 4, 6]) == False
assert alllessthansix([]) == True



def minval(some_list):
	if some_list == []:
		return None

	min_val = some_list[0]

	for val in some_list:
		if val < min_val:
			min_val = val
	return min_val  
#Test
assert minval([1, 2, 3, 4]) == 1
assert minval([]) == None
assert minval([5, 5, 5]) == 5



def onelessthansix(some_list):
	return minval(some_list) < 6
#Test
assert onelessthansix([1, 33, 100]) == True
assert onelessthansix([40, 50, 100]) == False
assert onelessthansix([6, 10, 12]) == False
		
