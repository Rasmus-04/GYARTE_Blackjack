import random

class DECK:
    def __init__(self, decks=1):
        self.decks = decks
        self.cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]*4*self.decks

    def shuffleCards(self):
        random.shuffle(self.cards)

    def drawCard(self):
        self.cards.insert(0, self.cards[-1])
        self.cards.pop(-1)
        return self.cards[0]
deck = DECK()


class PLAYER:
    def __init__(self, money=1000, dealer=False):
        self.money = money
        self.dealer = dealer
        self.activeBet = 0
        self.cards = []

    def drawCard(self):
        self.cards.append(deck.drawCard())

    def bet(self, amount):
        self.money -= amount
        self.activeBet += amount