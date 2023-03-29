from main import *

def hitOrStand(playerValue, dealerValue):
    ### Hit = True
    ### Stand = False

    if playerValue < 18:
        return True
    elif playerValue == 18 and dealerValue != 4 and dealerValue != 7 and dealerValue != 8:
        return True
    return False

def winOrLose(playerValue, dealerValue):
    ### Win = True
    ### Lose = False
    if playerValue < 22 and playerValue >= dealerValue:
        return True
    return False

wins = 0
losses = 0
nrOfRounds = 1_000_00

bot = PLAYER()
dealer = DEALER()
players.append(bot)
players.append(dealer)

giveCards()

for rounds in range(1,nrOfRounds+1):
    reset()
    giveCards()

    while True:
        if hitOrStand(bot.calculateHand(), dealer.calculateHand(hand=[dealer.cards[0]])):
            bot.drawCard()
        else:
            break;

    dealer.drawFinalHand(bot.calculateHand())

    if winOrLose(bot.calculateHand(), dealer.calculateHand()):
        wins += 1
    else:
        losses += 1

    if rounds % 1000 == 0:
        print(rounds , wins/(wins+losses))
