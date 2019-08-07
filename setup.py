import random 
colors = ["r","g","b"]
shading = ["full", "shaded", "empty"]
shape = ["diamond", "oval", "rectangle"]
number = [1,2,3]
startingDeck = []
class setGame:
    def __init__(self):
        self.deck = None
        self.generateDeck()
        self.shuffle()
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        repr_str = ''
        for card in self.deck:
            repr_str += '\n' + card.__str__()
        return repr_str
    def generateDeck(self):
        deck = []
        for nums in number:
            num = nums
            for col in colors:
                color = col
                for shade in shading:
                    shaded = shade
                    for shapes in shape:
                        deck.append([num, color, shaded, shapes])
        self.deck = deck
    def shuffle(self):
        random.shuffle(self.deck)
if __name__ == '__main__':
    deck = setGame()
    deck.shuffle()
    
def getStartingCards(set_deck):
    r_deck = []
    for i in range(0, 12):
        r_deck.append(set_deck[i])
    return r_deck
def checkSame(l1,l2,l3):
    for i in range(0, 4):
        if l1[i] == l2[i] == l3[i]:
            return True
        return False
def checkDifferent(li1,li2,li3):
    for i in range(0, 4):
        rval = 0
        if li1[i] != li2[i] != li3[i]:
            rval += 1
            continue
    if rval < 3:
        return False
    return True

startingDeck = getStartingCards(deck)

for i in range(0, 12):
    for j in range(1, 12):
        for k in range(2,12):
            if checkSame(deck[i],deck[j],deck[k]) or checkDifferent(deck[i],deck[j],deck[k]) and deck[i] != deck[j] != deck[k]:
                print(deck[i],deck[j],deck[k])


