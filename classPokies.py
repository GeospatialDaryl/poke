import random
from funcPokie import *

charTab ="	"

class Deck:
    import random
    
    def __init__(self):
        self.listCards = ['A','2','3','4','5','6','7','8','9','J','Q','K']
        self.listSuits = ['c','s','w','p']
        self.charTab ="	"
        self.deck = []
        
        self._listDeck = []
        for i in self.listCards:
            for j in self.listSuits:
                self._listDeck.append(i+j)
        print(self._listDeck)
        self.shuffle()
        
    
    def shuffle(self):
        print(random.shuffle(self._listDeck))
        (random.shuffle(self._listDeck))
        self.deck = self._listDeck
    
    def __str__(self):
        print(self.deck)
        

class Hand:
    def __init__(self):
        self.slot1 = ""
        self.slot2 = ""
        self.hand = []
        self.hazMults = []
        self.hazFlush = []
    def checkMults(self):
        pass
    def checkFlush(self):
        
        def findHighCard(inListHand, suitMatch = False):
            pntVal = 0
            high = [0,"2"]
            for cd in inListHand:
                if checkPointValue(cd[0]) > pntVal:
                    if not suitMatch:
                        pntVal = checkPointValue(cd[0])
                        high = [ cd[0], cd[1] ]
                    else:
                        if cd[1] == suitMatch:
                            pntVal = checkPointValue(cd[0])
                            high = [ cd[0], cd[1] ]
            return high
        
        dictSuits = {}
        dictSuits["c"] = 0
        dictSuits["p"] = 0
        dictSuits["w"] = 0
        dictSuits["s"] = 0
        for c in self.hand:
            if c[1] == "c" : dictSuits["c"] = dictSuits["c"] + 1
            if c[1] == "p" : dictSuits["p"] = dictSuits["p"] + 1
            if c[1] == "w" : dictSuits["w"] = dictSuits["w"] + 1
            if c[1] == "s" : dictSuits["s"] = dictSuits["s"] + 1
        if dictSuits["c"] > 4:
            highCard = findHighCard(self.hand, "c")
            self.hazFlush = [True, highCard, "c"]
        if dictSuits["p"] > 4:
            highCard = findHighCard(self.hand, "p")
            self.hazFlush = [True, highCard, "p"]
        if dictSuits["w"] > 4: 
            highCard = findHighCard(self.hand)
            self.hazFlush = [True, highCard, "w"]
        if dictSuits["s"] > 4: 
            highCard = findHighCard(self.hand)
            self.hazFlush = [True, highCard, "s"]
            
        return self.hazFlush

    def __str__(self):
        self.uSpade = u'\u2660'
        self.uHeart = u'\u2661'
        self.uDiamond = u'\u2662'
        self.uClub = u'\u2663'
        
        strOut = "  "
        
        for cd in self.hand:
            if cd[1] == "c":
                strOut = strOut + cd[0] + self.uHeart + "  "
            elif cd[1] == "p":
                strOut = strOut + cd[0] + self.uDiamond + "  "
            elif cd[1] == "w":
                strOut = strOut + cd[0] + self.uClub + "  "    
            else:
                strOut = strOut + cd[0] + self.uSpade + "  "
        
        return strOut

        
class Card:
    def __init__(self, inTuple):
        self.uSpade = u'\u2660'
        self.uHeart = u'\u2661'
        self.uDiamond = u'\u2662'
        self.uClub = u'\u2663'
        self.pip=inTuple[0]
        self.suit=inTuple[1]
        if self.suit == "w": self.uSuit= self.uClub
        if self.suit == "c": self.uSuit= self.uDiamond
        if self.suit == "p": self.uSuit= self.uHeart
        if self.suit == "s": self.uSuit= self.uSword
        
    def __str__(self):
        return self.pip+self.uSuit



class Table:
    def __init__(self, inDeck, intPlayers=6, VERBOSE = True):

        self.verbose=VERBOSE

        # create table and players with empty hands
        self.deck = inDeck
        self.intPlayers = intPlayers
        
        #  k is the relative counter
        self.listPlayers = []
                
        #  i is the instance-wide counter for 
        #  where we are in the shuffled deck.
        self.i = 0
        
        # populate the listPlayers with a objHand each
        k = 0
        while k < intPlayers:
            # each entry is listPlayers is their objHand
            self.listPlayers.append(Hand())
            k = k + 1

    def dealFirstTwoCards(self):
        k = 0
        while k < self.intPlayers:
            thisUn = self.deck.deck[self.i]
            if self.verbose: print(thisUn) 
            self.listPlayers[k].slot1=thisUn
            
            self.i = self.i + 1
            k = k + 1
        
        k = 0
        while k < self.intPlayers:
            thisUn = self.deck.deck[self.i]
            if self.verbose: print(thisUn) 
            self.listPlayers[k].slot2=thisUn
            
            self.i = self.i + 1
            k = k + 1

    def dealTwoTable(self):
        self.tableCards = ["",""]
        self.tableCards[0] = self.deck.deck[self.i]
        self.i = self.i + 1
        self.tableCards[1] = self.deck.deck[self.i]
        self.i = self.i + 1

        if self.verbose: print(self.tableCards)

    def deal3rdCard(self):
        k = 0
        while k < 1:
            thisUn = self.deck.deck[self.i]
            if self.verbose: print(thisUn) 
            self.tableCards.append(thisUn)
            self.i = self.i + 1
            k = k + 1

        if self.verbose: print(self.tableCards)

    def deal4thCard(self):
        k = 0
        while k < 1:
            thisUn = self.deck.deck[self.i]
            if self.verbose: print(thisUn) 
            self.tableCards.append(thisUn)
            self.i = self.i + 1
            k = k + 1

        if self.verbose: print(self.tableCards)

    def deal5thCard(self):
        k = 0
        while k < 1:
            thisUn = self.deck.deck[self.i]
            if self.verbose: print(thisUn) 
            self.tableCards.append(thisUn)
            self.i = self.i + 1
            k = k + 1

        if self.verbose: print(self.tableCards)

    def makeFinalHands(self):
        self.finals = []
        self.j = 0
        while self.j < intPlayers:
            self.finals[j] = self.listPlayers[j].slot1+self.tableCards[j]
            self.j = self.j + 1

    def updateHands(self):
        for players in self.listPlayers:
            players.hand = self.tableCards + [players.slot1] + [players.slot2]

    def printHand(self, intPlayer):
        if intPlayer >= self.intPlayers:
            print("<<<No Player>>")
        elif intPlayer < 0:
            print("<<<No Player>>")
        else:
            print(self.listPlayers[intPlayer].hand)

    def checkHand(self, intPlayer):
        thisPlayer = self.listPlayers[intPlayer]
        listHand = thisPlayer.hand
        listCards = []
        for card in listHand:
            listCards.append( (card[0], card[1] ) )

        #print(listHand, listCards)
        return listCards

    def whoWins(self):
        for p in self.listPlayers:
            print(p.hand)

        return (intPlayer, score)
    

    def evaluateHand(self, intPlayer):
        # check for multiples
        self.listPlayers[intPlayer].hazMults = ()
        
        