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
giveCards()

def showCards(showDealerHand=False):
    print()
    for index, i in enumerate(players[:-1]):
        print(f"P{index+1} cards: {i.cards}")

    if showDealerHand:
        print(f"Dealers cards: {players[-1].cards}")
    else:
        print(f"Dealers cards: [{players[-1].cards[0]}, #]")
    print()


while run:
    round += 1
    print(f"Runda {round}")
    # Fråga spelarna hur mycket dom vill beta
    for index, i in enumerate(players[:-1]):
        i.bet(int(input("Hur mycket vill spelare " + str(index+1) + " betta? ")))

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
                elif inp == "3":
                    player.bet(player.activeBet)
                    player.drawCard()
                    player.stand = True

    break