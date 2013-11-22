import random
import cards

class ThreeCardPoker:

    UNQUALIFIED = 0
    HIGH_CARD = 1
    PAIR = 2
    FLUSH = 3
    STRAIGHT = 4
    TRIPS = 5
    STRAIGHT_FLUSH = 6

    def __init__(self):
        self.deck = cards.Deck()
        self.players = []
        self.money = 0
        self.hand = []
        self.handScore = self.UNQUALIFIED

    def shuffleDeck(self):
        shuffleCount = random.randint(2, 10)
        for num in range(shuffleCount):
            self.deck.shuffle()

    def addPlayer(self, name="default", money=100):
        player = Player(game=self, name=name, money=money)
        self.players.append(player)

    def dealHand(self):
        self.shuffleDeck()
        for player in self.players:
            player.handScore = self.HIGH_CARD
            player.hand = self.deck.drawCards(3)
        self.handScore = self.UNQUALIFIED
        self.hand = self.deck.drawCards(3)

    def showHands(self):
        print "SHOWDOWN\n-----------------"
        self.handScore = self.evaluateHand(self.hand)
        print "Dealer's hand: "
        self.displayHand(self.hand, self.handScore)

        for player in self.players:
            player.handScore = self.evaluateHand(player.hand)
            print "---------------------"
            print "%s's hand: " % player.name
            self.displayHand(player.hand, player.handScore)

    def displayHand(self, hand, score):
        for card in hand:
            print card

        if score == self.HIGH_CARD:
            print "***High card***"
        elif score == self.PAIR:
            print "***Pair***"
        elif score == self.FLUSH:
            print "***Flush***"
        elif score == self.STRAIGHT:
            print "***Straight***"
        elif score == self.TRIPS:
            print "***Three of a Kind***"
        elif score == self.STRAIGHT_FLUSH:
            print "***Straight Flush***"
        else:
            print "Hand does not qualify"

    def evaluateHand(self, hand):
        """ Evaluate the hand based on the Three Card Poker rules. In order
        to give credit for the best possible hand, the hand will be evaluated
        in order of best to worst."""

        hand.sort()
        firstCard, secondCard, thirdCard = hand[0], hand[1], hand[2]

        #Check for Three of a Kind and pair
        if firstCard.rank == secondCard.rank:
            #Hand contains at least a pair - Check for three of a kind
            if firstCard.rank == thirdCard.rank:
                #All three cards match in rank - Trips!!
                return self.TRIPS
            else:
                #With two and only two matching cards, a pair is the best hand
                return self.PAIR

        # Check for two other pair options
        if firstCard.rank == thirdCard.rank or secondCard.rank == thirdCard.rank:
            return self.PAIR

        #Now Check for next best hand - a straight
        if (firstCard.rank + 1 == secondCard.rank) and (
           firstCard.rank + 2 == thirdCard.rank):
            #We have a straight - check for straight flush!!
            if firstCard.suit == secondCard.suit and firstCard.suit == thirdCard.suit:
                return self.STRAIGHT_FLUSH
            else:
                return self.STRAIGHT

        #Check one edge case - Ace high straight, since deck represents Ace as 1
        if firstCard.rank == 1 and secondCard.rank == 12 and thirdCard.rank == 13:
            #We have a straight - check for straight flush!!
            if firstCard.suit == secondCard.suit and firstCard.suit == thirdCard.suit:
                return self.STRAIGHT_FLUSH
            else:
                return self.STRAIGHT

        #Finally, check for a flush
        if firstCard.suit == secondCard.suit and firstCard.suit == thirdCard.suit:
            #We have a flush!
            return self.FLUSH

        #With no made hands, check for a high card to qualify
        for card in hand:
            if card.rank >= 12 or card.rank == 1:
                return self.HIGH_CARD

        #GOT NOTHING!!
        return self.UNQUALIFIED


class Player:

    def __init__(self, game, name, money):
        self.game = game
        self.name = name
        self.money = money
        self.hand = []
        self.handScore = game.HIGH_CARD
