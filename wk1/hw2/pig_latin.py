# Write any helper functions you need here.
VOWELS = ['a', 'e', 'i', 'o', 'u']
def pig_latin(word):
	# word is a string to convert to pig-latin
	##### YOUR CODE HERE #####
	if word == "":
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

def pig_latin_phrase(phrase):
	word_list = phrase.lower().split()
	return " ".join([pig_latin(w) for w in word_list])

phrase = raw_input("Enter a phrase: ")
print pig_latin_phrase(phrase)

	
