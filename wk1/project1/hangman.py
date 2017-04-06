# Name:
# Section: 
# 6.189 Project 1: Hangman template
# hangman_template.py

# Import statements: DO NOT delete these! DO NOT write code above this!
from random import randrange
from string import *
from hangman_lib import *
# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import hangman words

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = split(line)
    print "  ", len(wordlist), "words loaded."
    print 'Enter play_hangman() to play a game of hangman!'
    return wordlist

# actually load the dictionary of words and point to it with 
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word=words_dict[randrange(0,len(words_dict))]
    return word

# end of helper code
# -----------------------------------


# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES 
secret_word = 'claptrap' 
letters_guessed = []

# From part 3b:
def word_guessed():
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    global secret_word
    global letters_guessed

    ####### YOUR CODE HERE ######
    #pass # This tells your code to skip this function; delete it when you
         # start working on this function
    for letter in secret_word:
	if letter not in letters_guessed:
		return False
    return True




def print_guessed():
    '''
    Prints out the characters you have guessed in the secret word so far
    '''
    global secret_word
    global letters_guessed
    
    ####### YOUR CODE HERE ######
    #pass # This tells your code to skip this function; delete it when you
         # start working on this function
    #guessed = [x for x in secret_word if x in letters_guessed else '-']
    #return "".join(guessed)
    guessed = ""
    for x in secret_word:
	guessed += x if x in letters_guessed else '-'

    return guessed





def play_hangman():
    # Actually play the hangman game
    global secret_word
    global letters_guessed
    # Put the mistakes_made variable here, since you'll only use it in this function
    mistakes_made = 0
   
    # Update secret_word. Don't uncomment this line until you get to Step 8.
    secret_word  = get_word()
    word_len = str(len(secret_word))
    ####### YOUR CODE HERE ######
 
    while word_guessed() == False and mistakes_made < MAX_GUESSES:
	print "\n", MAX_GUESSES - mistakes_made, "guesses left"
	print "The secret word is:", print_guessed(), "(" + word_len + " letters long)"
	print "Letter guessed so far:", '-'.join(letters_guessed)
	print_hangman_image(mistakes_made)	

	already_guessed = True

	#Request user for a letter to guess	
	while already_guessed == True:
	    letter_guess = raw_input("Enter a letter you haven't guessed yet: ")[0].lower()
	    already_guessed = (letter_guess in letters_guessed)
	
	    if already_guessed == True:
		print "Enter a letter that you haven't guessed yet!"

	#Determine if letter guessed is in the secret word
	letters_guessed.append(letter_guess)
	if letter_guess in secret_word:
		print "Good guess! You got a letter!"
	else:
		print "Sorry! The letter '" + letter_guess + "' is not in the secret word"
		mistakes_made += 1	

    #Determine if word is guessed OR guess attempts exceeded
    if word_guessed() == True:
	print "\nNicely done! You guessed the word!"
	print "The secret word was:", secret_word
    else:
	print_hangman_image(mistakes_made)
	print "Guess limit reached!"
	print "Sorry you couldn't guess the word!"

    return None


play_hangman()

 
