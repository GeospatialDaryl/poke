def checkPointValue(inPip):
    if inPip=="A": return(14)
    elif inPip=="K": return(13)
    elif inPip=="Q": return(12)
    elif inPip=="J": return(11)
    else: return(int(inPip))
    

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


def checkCardFromPoint(inPoint):
    if inPoint==14: return("A")
    elif inPip==13: return("K")
    elif inPip==12: return("Q")
    elif inPip==11: return("J")
    else: return(str(inPoints))
    


def returnListMax(inCntPip):    
    cntPip = inCntPip 
    max = 0
    for key in cntPip.keys():
        if cntPip[key] > max: 
            max = cntPip[key]

    listTops = []
    #print(max)

    for key in cntPip.keys():
        if cntPip[key] == max:
            listTops.append( (key, max) )
            #print(key, max)
    return listTops




# Returns the score for the list of multiples

def scoreFromListMax(inListMax):
    '''
    Returns the score for the list of multiples
    out tuple:   Score, NumCards
    '''
    listMax = inListMax
    score = 0
    for items in listMax:
        if checkPointValue(items[0]) > score:
            score = checkPointValue(items[0])
    return (score, checkPointValue(items[1]))



#  in a list of listCards, out dictCoutPip

def checkHandPairs(inListCards):
    pair = ""
    listPip = []
    listSuit = []
    for cards in inListCards:
        listPip.append(cards[0])
        listSuit.append(cards[1])
    countPip = {}
    countSuit = {}
    for items in listPip:
        if items in countPip.keys(): 
            countPip[items] = countPip[items] + 1
        else:
            countPip[items] = 1
    print(countPip)
    if len(countPip) < len(listPip):
        #we have dupes
        l = 1
        while l < len(listPip):
            l = l + 1
            pass
    return(countPip)