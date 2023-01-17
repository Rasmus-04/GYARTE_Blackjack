from config import *
amountOfPlayers = 2#input("Enter amount of players(Max 4): ")

for i in range(int(amountOfPlayers)):
    players.append(PLAYER())
players.append(PLAYER(dealer=True))

def giveCards():
    for i in range(2):
        for j in players:
            j.drawCard()

giveCards()
for i in players:
    if i.dealer:
        print(i.cards, "Dealer")
        continue
    print(i.cards)

while run:
    round += 1
    print(f"Runda {round}")
    # Fråga spelarna hur mycket dom vill beta
    for i in range(len(players)-1):
        input("Hur mycket vill spelare " + str(i+1) + " betta? ")
    break



