
class Card:
	SUITLIST = ["Clubs", "Diamonds", "Hearts", "Spades"]
	RANKLIST = ["narf", "Ace", "2", "3", "4", "5", "6", "7", "8", "9",
		    "10", "Jack", "Queen", "King"]

	def __init__(self, suit=0, rank=2):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return (self.RANKLIST[self.rank] + " of " + self.SUITLIST[self.suit])

	def __cmp__(self, other):
		#check the suits
		if self.suit > other.suit : return 1
		if self.suit < other.suit : return -1

		#ACE is high, so need to do a special check for Aces
		if self.rank == 1:
			if other.rank != 1 : return 1
			else : return 0
		if other.rank == 1:
			if self.rank != 1 : return -1
			else : return 0
		
		#suits are the same, so check the rank
		if self.rank > other.rank : return 1
		if self.rank < other.rank : return -1
		
		#suits and ranks must be the same
		return 0

#test
#card = Card(1, 11)
#print card


class Deck:
	def __init__(self):
		self.cards = []
		for suit in range(4):
			for rank in range(1, 14):
				self.cards.append(Card(suit, rank))
	
	def printDeck(self):
		for card in self.cards:
			print card

	def __str__(self):
		s = ""
		length = len(self.cards)
		for i in range(length):
			s += " "*i + str(self.cards[i]) + "\n"
		return s

	def shuffle(self):
		import random
		cardCount = len(self.cards)
		for i in range(cardCount):
			j = random.randrange(i, cardCount)
			self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
	
	def removeCard(self, card):
		if card in self.cards: #'in' uses '__cmp__' method written in the Card class
			self.cards.remove(card)
			return True
		#else
		return False

	#removes a card from the END of the deck
	def popCard(self): 
		return self.cards.pop()
	
	def isEmpty(self):
		return (len(self.cards) == 0)

	def deal(self, hands, cardCount=999):
		handCount = len(hands)
		for i in range(cardCount):
			if self.isEmpty() : break	#break if out of cards
			card = self.popCard()		#remove the top card
			hand = hands[i % handCount]	#whose turn is it next?
			hand.addCard(card)		#add the card to the hand
				
#test
#deck = Deck()
#card = Card(1, 13)
#print "About to remove " + str(card)
#deck.shuffle()
#deck.removeCard(card)
#print deck

#this statement indicates that the new Hand class INHERITS methods and data members from the existing Deck class
class Hand(Deck):
	def __init__(self, name=" "):
		self.cards = []
		self.name = name
	
	def addCard(self, card):
		self.cards.append(card)

	def __str__(self):
		s = "Hand " + self.name
		if self.isEmpty():
			s += " is empty\n"
		else:
			s += " contains\n" + Deck.__str__(self) 

		return s

#test
#deck = Deck()
#deck.shuffle()
#hand = Hand("Josh")
#deck.deal([hand], 5)
#print hand




class CardGame:
	def __init__(self):
		self.deck = Deck()
		self.deck.shuffle()

#since there's no __init__ method, it's inherited from the Hand class	
class OldMaidHand(Hand):
	def removeMatches(self):
		count = 0
		copy = self.cards[:]
		for card in copy:
			match = Card(3 - card.suit, card.rank)
			if match in self.cards:
				self.cards.remove(card)
				self.cards.remove(match)
				print "Hand %s: %s matches %s" % (self.name, card, match)
				count += 1
		return count

#test
#game = CardGame()
#hand = OldMaidHand("Josh")
#game.deck.deal([hand], 7)
#print hand
#hand.removeMatches()
#print hand


class OldMaidGame(CardGame):
	def play(self, names):
		#remove the Queen of Clubs
		self.deck.removeCard(Card(0, 12))
	
		#make a hand for each player
		self.hands = []
		for name in names:
			self.hands.append(OldMaidHand(name))

		#deal out the cards
		self.deck.deal(self.hands)
		print "---------- Cards have been dealt"
		self.printHands()		

		#remove initial matches
		matches = self.removeAllMatches()
		print "---------- Matches discarded, play begins"
		self.printHands()
		
		#play until all 50 cards are matched
		turn = 0
		handCount = len(self.hands)
		while matches < 25:
			matches += self.playOneTurn(turn)
			turn = (turn + 1) % handCount

		print "---------------- Game is Over"
		self.printHands()


	def removeAllMatches(self):
		count = 0
		for hand in self.hands:
			count += hand.removeMatches()
		return count


	def printHands(self):
		for hand in self.hands:
			print str(hand)
	
	
	def playOneTurn(self, turn):
		#if the player's hand is empty, then they are out of the game (not the loser)
		if self.hands[turn].isEmpty(): 
			return 0
		
		#find the next player on the left that has cards 
		neighbor = self.findNeighbor(turn)

		#take a card from the neighbor and add it to your hand
		pickedCard = self.hands[neighbor].popCard()
		self.hands[turn].addCard(pickedCard)
		
		print "Hand", self.hands[turn].name, "picked", pickedCard
		
		#remove any new matches, then re-shuffle the hand
		count = self.hands[turn].removeMatches()
		self.hands[turn].shuffle()
		return count


	def findNeighbor(self, turn):
		handCount = len(self.hands)
		
		for nextPlayer in range(1, handCount):
			neighbor = (turn + nextPlayer) % handCount

			if not self.hands[neighbor].isEmpty():
				return neighbor	
