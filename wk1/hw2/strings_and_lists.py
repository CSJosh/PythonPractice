# Name:
# Section:
# strings_and_lists.py

# **********  Exercise 2.7 **********

def sum_all(number_list):
    # number_list is a list of numbers
    total = 0
    for num in number_list:
        total += num

    return total

# Test cases
print "sum_all of [4, 3, 6] is:", sum_all([4, 3, 6])
print "sum_all of [1, 2, 3, 4] is:", sum_all([1, 2, 3, 4])



def csum(alist, total, index):
   if alist == [] or index >= len(alist):
	return 0

   total += alist[index]
   index += 1
   csum(alist, total, index) 

   index -= 1
   alist[index] = total 


def cumulative_sum(number_list):
    # number_list is a list of numbers
    ##### YOUR CODE HERE #####
    return csum(number_list, 0, 0)

# Test Cases
##### YOUR CODE HERE #####
alist = [1, 2, 3, 4, 5]
print "Test list BEFORE-->", alist
cumulative_sum(alist)
print "Test list AFTER-->", alist

# **********  Exercise 2.8 **********

def report_card():
        ##### YOUR CODE HERE #####
        valid = False

        while valid == False:
	        class_count = raw_input("How many classes did you take? ")
	        try:
	    	    class_count = int(class_count)
		    valid = True
	        except ValueError:
		    print "Enter a valid number of classes"

        class_list = []
        grade_list = []	
	num = 0
	valid = False
	grade_total = 0.0

	while num < class_count:
		name = raw_input("What what the name of this class? ")

		while valid == False:
			float_grade = raw_input("What was your grade? ")
		    
			try:
				float_grade = float(float_grade)
				valid = True
			except ValueError:
				print "Enter a valid grade (e.g. 95.15 or 80)"

		grade_total += float_grade
		class_list.append(name)
		grade_list.append(float_grade)
		num += 1
		valid = False

	num = 0

	print "...\nREPORT CARD:"
	while num < class_count:
		print class_list[num] + " - " + str(grade_list[num])
		num += 1

	print "Overall GPA", float(grade_total/float(class_count))

# Test Cases
#report_card()
## In comments, show the output of one run of your function.




# **********  Exercise 2.9 **********

# Write any helper functions you need here.
VOWELS = ['a', 'e', 'i', 'o', 'u']

def pig_latin(word):
	# word is a string to convert to pig-latin
	##### YOUR CODE HERE #####
	if word == []:
		return ""
	elif word[0] in VOWELS:
		new_word = word + "hay"
	else:
		new_word = word[1:] + word[0] + "ay"
	return new_word    

# Test Cases
##### YOUR CODE HERE #####
assert pig_latin("boot") == "ootbay"
assert pig_latin("image") == "imagehay"
#print pig_latin("boot")
#print pig_latin("image")
#print pig_latin("secret")
word = ""
while 'q' not in word:
	word = raw_input("Enter a word to translate to pig latin-->")
	print pig_latin(word)


# **********  Exercise 2.10 **********
#1
cubes = [i**3 for i in range(1, 11)]
print "Cubes 1 through 10-->", cubes

#2
coin = ['h', 't']
two_coins = [x+y for x in coin for y in coin]
print "Two coins flip possibilities-->", two_coins 

#3
def vowels(word):
	only_vowels = "".join([c for c in word if c not in VOWELS]) 
	return only_vowels

print vowels("Mississippi")
assert vowels("Mississippi") == "Msssspp"
assert vowels("aeiou") == ""


# **********  Exercise OPT.1 **********
# If you do any work for this problem, submit it here 
