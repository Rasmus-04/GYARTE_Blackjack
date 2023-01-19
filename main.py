from config import *
amountOfPlayers = 1#input("Enter amount of players(Max 4): ")

for i in range(int(amountOfPlayers)):
    players.append(PLAYER())
players.append(PLAYER(dealer=True))

def giveCards():
    for i in range(2):
        for j in players:
            j.drawCard()
giveCards()

def showCards():
    print()
    for index, i in enumerate(players[:-1]):
        print(f"P{index+1} cards: {i.cards}")
    print(f"Dealers cards: [{players[-1].cards[0]}, #]")
    print()


while run:
    round += 1
    print(f"Runda {round}")
    # Fråga spelarna hur mycket dom vill beta
    for index, i in enumerate(players[:-1]):
        i.bet(int(input("Hur mycket vill spelare " + str(index+1) + " betta? ")))
    showCards()

    for index, i in enumerate(players[:-1]):
        print(f"p{index+1}: ", end="")
        i.showPlayOptions()
        input()

    break
