# Name:
# Section:
# nims.py

def play_nims(pile, max_stones):
	'''
	An interactive two-person game; also known as Stones.
	@param pile: the number of stones in the pile to start
	@param max_stones: the maximum number of stones you can take on one turn
	'''
	    ## Basic structure of program (feel free to alter as you please):

	#    while [pile is not empty]:
	#        while [player 1's answer is not valid]:
	#            [ask player 1]
	#            [execute player 1's move]
	#       
	#        while [player 2's answer is not valid]:
	#            [ask player 2]
	#            [execute player 2's move]
	#
	#    print "Game over"


	players = ["Player 1", "Player 2"]
	turn_index = 0

	while pile > 0:
		print "There are", pile, "stones remaining;", players[turn_index], "can select between 1 and", max_stones, "stones."
		valid = False
		while valid == False:
			print "\n",players[turn_index]
			choice_string = raw_input("Enter the number of stones to remove: ")

			try:
				choice_int = int(choice_string)

				if choice_int <= pile and choice_int <= max_stones:
					valid = True
				else:
					print "Enter a number between 1 and",  str(pile) if pile < max_stones else str(max_stones)
			except ValueError:
					print "Enter a valid number"

		pile -= choice_int
		
		if pile != 0:
			turn_index += 1
			turn_index %= 2

	print "Game over"
	print players[turn_index], "wins"

play_nims(14, 3)
	
