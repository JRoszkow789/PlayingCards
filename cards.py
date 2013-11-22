import random
from itertools import product

cardLetters = {
    1  : 'A',
    10 : 'T',
    11 : 'J',
    12 : 'Q',
    13 : 'K',
}

cardSuits = {
    'c' : 'clubs',
    'h' : 'hearts',
    'd' : 'diamonds',
    's' : 'spades',
}

class Card:
    """Represents a playing card."""

    def __init__(self, rank, suit):
        self.rank = int(rank)
        self.suit = suit[0].lower()

    def __gt__(self, otherCard):
        return self.rank > otherCard.rank

    def __lt__(self, otherCard):
        return self.rank < otherCard.rank

    def __repr__(self):
        return "<%d%s>" % (self.rank, self.suit)

    def __str__(self):
        cardLetter = cardLetters.get(self.rank, str(self.rank))
        cardSuit = cardSuits[self.suit]
        return "%s of %s" % (cardLetter, cardSuit)


class Deck:
    """Represents an entire deck of playing cards."""

    ranks = range(1, 14)
    suits = cardSuits.keys()
    newDeck = [Card(combo[0], combo[1]) for combo in product(ranks, suits)]
    usedDeck = []

    def __init__(self):
        self.activeDeck = Deck.newDeck
        random.shuffle(self.activeDeck)

    def shuffle(self):
        """Simulates shuffling a new deck of cards. Also makes the newly
           shuffled deck become the active deck for this Deck object.
        """

        shuffleDeck = self.activeDeck + self.usedDeck
        random.shuffle(shuffleDeck)
        self.activeDeck = shuffleDeck
        self.usedDeck = []

    def drawCard(self):
        """Returns the top card of the active deck, simulating drawing a card."""

        try:
            card =  self.activeDeck.pop()
        except IndexError:
            print "No more drawing cards. The deck is empty!"
            return None

        self.usedDeck.append(card)
        return card

    def drawCards(self, count=1):
        """Returns cards from the top of the deck, simulating drawing cards.
        The cards are returned in a list and the number returned is the number
        specified in the count parameter.
        """

        cards = []
        while len(cards) < count:
            try:
                card = self.activeDeck.pop()
            except IndexError:
                print "Not enough cards! Deck is empty"
                return None
            self.usedDeck.append(card)
            cards.append(card)
        return cards

    def __len__(self):
        return len(self.activeDeck)


class Player:

    def __init__(self, name, money=1000):
        self.name = name
        self.money = money
        self.hand = None

    def setHand(self, firstCard, secondCard):
        self.hand = (firstCard, secondCard)

    def showHand(self):
        if len(self.hand) == 2:
            print "<%s, %s>" % (self.hand[0], self.hand[1])
        else:
            for card in self.hand:
                print card

    def __repr__(self):
        return "<%s(%d)>" % (self.name, self.money)

    def __str__(self):
        if not self.hand:
            hand = ("None", "None")
        else:
            hand = self.hand
        return "Player Name: %s\nChips: %d\nCards: %s, %s" % (self.name, self.money, hand[0], hand[1])
