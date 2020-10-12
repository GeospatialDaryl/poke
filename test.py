from classPokies import *
from funcPokie import *
from valsPokie import *

deck = Deck()
deck.shuffle()
print(deck._listDeck)
#rint(deck)

listRank = print(listRank[0].split(charTab))

table = Table(deck) 
table.dealFirstTwoCards()
table.dealTwoTable()
table.deal3rdCard()
table.deal4thCard()
table.deal5thCard()
table.updateHands()

listCards = table.checkHand(0)
listCards2 = [('2', 'p'), ('Q', 'w'), ('K', 's'), ('2', 'w'), ('5', 'w'), ('Q', 's'), ('K', 'p')]
listCards3 = [('K', 'p'), ('Q', 'w'), ('K', 's'), ('2', 'w'), ('5', 'w'), ('Q', 's'), ('K', 'p')]

thisScores = scoreFromListMax(returnListMax(checkHandPairs(listCards2)))

outie = checkHandPairs(listCards2)
print(u'\u2660')
#table.listPlayers[0].hand = [('2', 'p'), ('Q', 'w'), ('K', 's'), ('2', 'p'), ('5', 'p'), ('Q', 'p'), ('K', 'p')]
#table.listPlayers[0].checkFlush()
#print(table.listPlayers[0].__str__())


for pl in table.listPlayers:
    print( pl, pl.checkFlush() )
    
print(table.listPlayers[0], table.listPlayers[0].checkFlush())

print("hello")
#checkPointValue("2")
#returnListMax(cntPip)
listMax = returnListMax(cntPip)
print(listMax)

# Returns the score for the list of multiples
