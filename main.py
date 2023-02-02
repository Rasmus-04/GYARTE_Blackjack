from config import *

# Antal spelare
amountOfPlayers = 1#input("Enter amount of players(Max 4): ")

# Skapar en lista med alla spelare
for i in range(int(amountOfPlayers)):
    players.append(PLAYER())

# Skapar dealern och sätter den sist i spelar listan
players.append(PLAYER(dealer=True))
dealer = players[-1]

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
        player.cards = []
        player.activeBet = 0
        player.stand = False

# Ränknar ut hur många kort dealern borde plocka upp
def calculateDealerHand():
    heigestHand = 0
    for player in players[:-1]:
        hand = player.calculateHand()
        if hand < 22 and hand > heigestHand:
            heigestHand = hand

    while True:
        if dealer.calculateHand() >= heigestHand:
            return
        elif dealer.calculateHand() > 16:
            return
        dealer.drawCard()

# Delar ut alla winnings till spelarna
def giveWinnings():
    for player in players:
        handValue = player.calculateHand()
        dealerHandValue = dealer.calculateHand()

        if dealerHandValue > 21:
            dealerHandValue = 0

        if handValue > 21:
            return
        elif handValue > dealerHandValue:
            player.money += player.activeBet*2
        elif handValue == dealerHandValue:
            player.money += player.activeBet


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
        for index, player in enumerate(players[:-1]):
            while not player.stand and player.calculateHand() < 21:
                print(f"p{index+1}: ", end="")
                player.showPlayOptions()
                inp = input().strip()[0]
                if inp == "1":
                    player.drawCard()
                    print(f"p{index+1}: {player.cards} ({player.calculateHand()})")
                elif inp == "2":
                    player.stand = True
                elif inp == "3" and player.canDoubleDown():
                    player.bet(player.activeBet)
                    player.drawCard()
                    player.stand = True
                elif inp == "4":
                    player.money += int(player.activeBet/2)
                    player.activeBet = 0
                    player.stand = True
                elif inp == "5":
                    pass
                elif inp == "0":
                    run = False
                    break

        calculateDealerHand()
        giveWinnings()
        showCards(True)

    resetPlayersBet()
