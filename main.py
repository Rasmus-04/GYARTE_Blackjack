import random
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]*4
random.shuffle(deck)
players = []
money = []
activeBet = []
run = True
round = 0
amountOfPlayers = 2#input("Enter amount of players(Max 4): ")

for i in range(int(amountOfPlayers)):
    players.append([])
    money.append(1000)
    activeBet.append(0)
players.append([])

def giveCards():
    for j in range(len(players)):
        players[j].append(deck[-1])
        deck.insert(0, deck[-1])
        deck.pop(-1)

while run:
    round += 1
    print(f"Runda {round}")
    # Fråga spelarna hur mycket dom vill beta
    for i in range(len(players)):
        input("Hur mycket vill spelare "+ str(i+1) +" betta? ")
    break



print(players, money, activeBet)