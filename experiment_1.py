from classPokies import *
from funcPokie import *
from valsPokie import *

d1 = Deck()

listCards = d1.listCards

dictCntFlushes = {}

for val in listCards:
    dictCntFlushes[val] = 0

intMe = 0

def runFlush():
    deck = Deck()
    deck.shuffle()
    print(deck._listDeck)
    
    table = Table(deck) 
    table.dealFirstTwoCards()
    table.dealTwoTable()
    table.deal3rdCard()
    table.deal4thCard()
    table.deal5thCard()
    table.updateHands()
    
    listHandResults = [0,0,0,0,0,0]
    
    for pl in table.listPlayers:
        res = pl.checkFlush() 
        print(res)
    
runFlush()

print("Stop")



