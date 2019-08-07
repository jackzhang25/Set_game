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
    game = setGame()
    game.shuffle()
    
def getStartingCards(sdeck):
    r_deck = []
    for i in range(0, 12):
        r_deck.append(sdeck[i])
    return r_deck


def checkSame(l1,l2,l3):
    for i in range(0, 4):
        if not (l1[i] == l2[i] and l2[i] == l3[i]) and not (l1[i] != l2[i] and l2[i] != l3[i] and l1[i] != l3[i]):
            return False
        
    return True





if __name__ == '__main__':
    game = setGame()
    game.shuffle()
    startingDeck = [["3","g","empty","rectangle"],["1","r","shaded","rectangle"],["3","r","empty","diamond"],["1","g","full","oval"],["3","g","full","diamond"],["3","g","empty","oval"],["3","g","shaded","diamond"],["3","g","full","rectangle"],["3","r","shaded","oval"],["3","g","shaded","oval"], ["1","g","full","rectangle"], ["3","g","empty","diamond"]]            #getStartingCards(game.deck)
    for i in range(0,12):
        print("card: " + str(startingDeck[i]))

    for i in range(0, 12):
        for j in range(i+1, 12):
            for k in range(j+1,12):
                if checkSame(startingDeck[i],startingDeck[j],startingDeck[k]):
                    print(startingDeck[i],startingDeck[j],startingDeck[k])


