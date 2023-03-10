import random

class DECK:
    # Skapar kortleken med så många kortlekar vi vill ha
    def __init__(self, decks=1):
        self.decks = decks
        self.cards = ([2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]*4)*self.decks

    # Blandar korten
    def shuffleCards(self):
        random.shuffle(self.cards)

    # Tar det senaste kortet och lägger det längs bak i kortleken och returnar det kortert
    def drawCard(self):
        self.cards.insert(0, self.cards[-1])
        self.cards.pop(-1)
        return self.cards[0]
deck = DECK()


class PLAYER:
    def __init__(self, money=1000):
        self.money = money
        self.activeBet = 0
        self.cards = []
        self.splitCards = []
        self.stand = False
        self.isSplit = False
        self.splitStand = False


    # Drar ett kort
    def drawCard(self):
        self.cards.append(deck.drawCard())

    # Bettar
    def bet(self, amount):
        if self.money >= amount and amount > 0:
            self.money -= amount
            self.activeBet += amount
            return True
        return False

    # Skriver ut vad spelarens alternativ är
    def showPlayOptions(self):
        if len(self.cards) == 2 and self.canSplit():
            print("Do you wanna 1(hit), 2(stand), 3(double down), 4(fold), 5(split), 0(Avbryt)? ")
        elif(len(self.cards) == 2):
            print("Do you wanna 1(hit), 2(stand), 3(double down), 4(fold), 0(Avbryt)? ")
        else:
            print("Do you wanna 1(hit), 2(stand), 0(Avbryt)? ")

    # Kollar om spelaren kan splita korten
    def canSplit(self):
        if len(self.cards) != 2 or self.isSplit:
            return False

        temp = self.cards.copy()
        change = ["J", "Q", "K"]
        for index, i in enumerate(temp):
            if i in change:
                temp[index] = 10

        if temp[0] == temp[1] and self.money >= self.activeBet:
            return True
        return False

    # Räknar ut värdet på sina kort
    def calculateHand(self, splitHand=False):
        if splitHand:
            temp = self.splitCards.copy()
        else:
            temp = self.cards.copy()

        change = ["J", "Q", "K"]
        for index, i in enumerate(temp):
            if i in change:
                temp[index] = 10

        tempCount = 0
        for i in range(temp.count("A")):
            temp.remove("A")
            temp.append("A")

        for i in temp:
            if i == "A":
                if tempCount + 11 < 22:
                    tempCount += 11
                else:
                    tempCount += 1
            else:
                tempCount += i
        return tempCount

    # Kollar om spelaren kan double down
    def canDoubleDown(self):
        if len(self.cards) == 2 and self.money >= self.activeBet:
            return True
        return False

    # Resetar för en ny runda
    def reset(self):
        self.activeBet = 0
        self.cards = []
        self.splitCards = []
        self.stand = False
        self.isSplit = False
        self.splitStand = False

    def play(self, playerNr):
        while not self.stand and self.calculateHand() < 21:
            print(f"p{playerNr}: ", end="")
            self.showPlayOptions()
            inp = input().strip()[0]
            if inp == "1":
                self.drawCard()
                print(f"p{playerNr}: {self.cards} ({self.calculateHand()})")
            elif inp == "2":
                self.stand = True
            elif inp == "3" and self.canDoubleDown():
                self.bet(self.activeBet)
                self.drawCard()
                self.stand = True
            elif inp == "4":
                self.money += int(self.activeBet / 2)
                self.activeBet = 0
                self.stand = True
            elif inp == "5":
                if self.canSplit():
                    self.isSplit = True
            elif inp == "0":
                return True

    def addWinnings(self, dealerHandValue):
        handValue = self.calculateHand()

        if handValue > 21:
            return
        elif handValue > dealerHandValue:
            self.money += self.activeBet*2
        elif handValue == dealerHandValue:
            self.money += self.activeBet

class DEALER(PLAYER):
    def drawFinalHand(self, heigestHand):
        while True:
            if self.calculateHand() >= heigestHand:
                return
            elif self.calculateHand() > 16:
                return
            self.drawCard()
