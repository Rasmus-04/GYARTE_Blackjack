from config import *
amountOfPlayers = 1#input("Enter amount of players(Max 4): ")

for i in range(int(amountOfPlayers)):
    players.append(PLAYER())
players.append(PLAYER(dealer=True))
dealer = players[-1]

def giveCards():
    for i in range(2):
        for j in players:
            j.drawCard()

def showCards(showDealerHand=False):
    print()
    for index, i in enumerate(players[:-1]):
        print(f"P{index+1} cards: {i.cards}")

    if showDealerHand:
        print(f"Dealers cards: {players[-1].cards}")
    else:
        print(f"Dealers cards: [{players[-1].cards[0]}, #]")
    print()

def showMoney():
    for index, player in enumerate(players[:-1], start=1):
        print(f"\nSpelare {index} har: {player.money} kr\n")

def resetPlayersBet():
    for player in players:
        player.cards = []
        player.activeBet = 0
        player.stand = False

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

def giveWinnings():
    for player in players:
        handValue = player.calculateHand()
        dealerHandValue = dealer.calculateHand()
        if handValue > 21:
            return
        elif handValue > dealerHandValue:
            player.money += player.activeBet*2
        elif handValue == dealerHandValue:
            player.money += player.activeBet


while run:
    round += 1
    print(f"Runda {round}")
    # Fråga spelarna hur mycket dom vill beta
    showMoney()
    for index, player in enumerate(players[:-1]):
        player.bet(int(input("Hur mycket vill spelare " + str(index+1) + " betta? ")))

    giveCards()

    if len(dealer.cards) == 2 and dealer.calculateHand() == 21:
        showCards(showDealerHand=True)
        print("Dealer vinner")

    else:
        showCards()
        for index, player in enumerate(players[:-1]):
            while not player.stand and player.calculateHand() < 20:
                print(f"p{index+1}: ", end="")
                player.showPlayOptions()
                inp = input().strip()[0]
                if inp == "1":
                    player.drawCard()
                    print(f"p{index+1}: {player.cards}")
                elif inp == "2":
                    player.stand = True
                elif inp == "3" and player.canDoubleDown():
                    player.bet(player.activeBet)
                    player.drawCard()
                    player.stand = True
                elif inp == "4":
                    player.money += player.activeBet/2
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