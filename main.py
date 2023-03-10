#HigherorLower game OOP

import random

# Card Constants
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King',)

NCards = 8

#Pass a deck and this fucntion will get a random card from the deck
def getCard(deckOfCards):
    thisCard = deckOfCards.pop() # pop one off the top of the deck and return
    return thisCard