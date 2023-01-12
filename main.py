import random
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]*4
random.shuffle(deck)
players = []
print(deck)

amountOfPlayers = input("Enter amount of players(Max 4): ")

for i in range(int(amountOfPlayers)):
    players.append([])
players.append([])

for i in range(2):
    for j in range(len(players)):
        players[j].append(deck[-1])
        deck.insert(0, deck[-1])
        deck.pop(-1)

print(players)