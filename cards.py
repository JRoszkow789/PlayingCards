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
        """Returns the number of cards left in the deck."""
        return len(self.activeDeck)
