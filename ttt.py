#!/usr/bin/python

# TicTacToe


p1m = []    # player 1 list of moves
p2m = []    # player 2 list of moves 
b = [0,1,2, # the board
     3,4,5,
     6,7,8]

# TODO Replace check() helper method and checkWin() with list.containsAll(win)?
def check(w, p):
    j = 0
    for i in w:
        if i in p:
            j += 1
    if j == 3:
        return True
    else:
        return False
def checkWin(p):
    wins = [[0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]]
    for w in wins:
        if(check(w,p)):
            return True
    return False

def printBoard():
# TODO make this print prettier!
    print b[0:3]
    print b[3:6]
    print b[6:9]

printBoard()

# TODO play against the computer (random or AI, easy or hard)
while(True):
# TODO D.R.Y. 
# basic game play logic
    p1 = int(raw_input("p1: "))
    if type(b[p1]) is type(0):
        b[p1] = "x"
        p1m.append(p1)

    printBoard()
    if(checkWin(p1m)):
        print "\nPLAYER 1 WINS!"
        break
    p2 = int(raw_input("p2: "))
    if type(b[p2]) is type(0):
        b[p2] = "o"
        p2m.append(p2)


    printBoard()
    if(checkWin(p2m)):
        print "\nPLAYER 2 WINS!"
        break

print "THANKS FOR PLAYING\n"
