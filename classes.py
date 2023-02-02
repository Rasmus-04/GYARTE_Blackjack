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
    def __init__(self, money=1000, dealer=False):
        self.money = money
        self.dealer = dealer
        self.activeBet = 0
        self.cards = []
        self.stand = False

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
        if len(self.cards) != 2:
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
    def calculateHand(self):
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
