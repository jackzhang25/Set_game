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
    
def getStartingCards(sdeck):
    r_deck = []
    for i in range(0, 12):
        r_deck.append(sdeck[i])
    return r_deck


def checkSame(l1,l2,l3):
    for i in range(3):
        if l1[i] == l2[i] and l2[i] == l3[i] or l1[i] != l2[i] and l2[i] != l3[i]:
            continue
        else:
            return False
    return True

def playerCards(input):
    rval = []
    cardNum = ""
    if input[0] == "1":
        rval.append("1")
    else:
        rval.append("2")
    for i in range(2, len(input)):
        if input[i] == " ":
            rval.append(cardNum)
            cardNum = ""
        else:
            cardNum += input[i]
    rval.append(cardNum)
    return rval 

def removeCards(li, x, y, z):
    li.remove(x)
    li.remove(y)
    li.remove(z)
def printCards(li):
   for i in range(12):
        print("card " + str((i + 1)) + ": " + str(li[i]) )







if __name__ == '__main__':
    game = setGame()
    game.shuffle()
    startingCards = getStartingCards(game.deck)
    player1 = 0
    player2 = 0
    guess = input("Press enter when ready ")
    printCards(startingCards)
    while len(startingCards) >= 3:
        guess = input("Enter player number then the three cards you want to guess(with spaces): ")
        if guess == "stop":
            break
        cards = playerCards(guess)
        print(cards)
        if checkSame(startingCards[int(cards[1]) - 1], startingCards[int(cards[2]) - 1], startingCards[int(cards[3]) - 1]):
            if int(cards[0]) == 1:
                player1 += 1
            else:
                player2 += 1
            print("Player1 score: " + str(player1))
            print("Player2 score: " + str(player2))
            removeCards(game.deck, startingCards[int(cards[1]) - 1], startingCards[int(cards[2]) - 1], startingCards[int(cards[3]) - 1])
            startingCards = getStartingCards(game.deck)
            printCards(startingCards)
        else:
            print("That was not a set. Try again")
        
        



