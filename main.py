from config import *

# Ger alla spelare och dealern sina kort av början av en runda
def giveCards():
    for i in range(2):
        for j in players:
            j.drawCard()

# Vissar alla kort
def showCards(showDealerHand=False):
    print()
    for index, i in enumerate(players[:-1]):
        print(f"P{index+1} cards: {i.cards} ({i.calculateHand()})")

    if showDealerHand:
        print(f"Dealers cards: {players[-1].cards} ({dealer.calculateHand()})")
    else:
        print(f"Dealers cards: [{players[-1].cards[0]}, #]")
    print()

# Vissar alla pengar
def showMoney():
    for index, player in enumerate(players[:-1], start=1):
        print(f"\nSpelare {index} har: {player.money} kr\n")

# Resetar spelaren efter varjee runda
def resetPlayersBet():
    for player in players:
        player.reset()

def reset():
    for player in players:
        player.reset()
    deck.shouldShuffle()

# Ränknar ut hur många kort dealern borde plocka upp
def calculateDealerHand():
    heigestHand = 0
    for player in players[:-1]:
        hand = player.calculateHand()
        if hand < 22 and hand > heigestHand:
            heigestHand = hand
    dealer.drawFinalHand(heigestHand)

# Delar ut alla winnings till spelarna
def giveWinnings():
    for player in players:
        dealerHandValue = dealer.calculateHand()
        if dealerHandValue > 21:
            dealerHandValue = 0
        player.addWinnings(dealerHandValue)

def play():
    global round
    while run:
        round += 1
        print(f"Runda {round}")
        showMoney()
        # Fråga spelarna hur mycket dom vill beta
        for index, player in enumerate(players[:-1]):
            while not player.bet(int(input("Hur mycket vill spelare " + str(index+1) + " betta? "))):
                pass
        giveCards()

        # Kollar om dealern vann
        if len(dealer.cards) == 2 and dealer.calculateHand() == 21:
            showCards(showDealerHand=True)
            print("Dealer vinner")

        else:
            # Vissar alla kort
            showCards()
            # Går igenom varje spelare och kollar vad dom vill göra
            for index, player in enumerate(players[:-1], start=1):
                if player.play(index):
                    return
            calculateDealerHand()
            giveWinnings()
            showCards(True)
        resetPlayersBet()


if __name__ == "__main__":
    # Antal spelare
    amountOfPlayers = 1  # input("Enter amount of players(Max 4): ")

    # Skapar en lista med alla spelare
    for i in range(int(amountOfPlayers)):
        players.append(PLAYER())

    # Skapar dealern och sätter den sist i spelar listan
    players.append(DEALER())
    dealer = players[-1]
    play()