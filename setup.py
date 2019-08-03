import random 
colors = ["r","g","b"]
shading = ["full", "shaded", "empty"]
shape = ["diamond", "oval", "rectangle"]
number = [1,2,3]
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
    print(deck)
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
