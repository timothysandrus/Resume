import random
with open('wordlist_kevin_atkinson.txt') as f:
        mylist = f.read().splitlines()
alph = "abcdefghijklmnopqrstuvwxyz"
global mylist2
mylist2= mylist
global playerones
global playertwos
playertwos = 3
playerones = 3
global Lost
Lost = 0
global word
word =""
global duck
duck = 1
def strike(a):
    global Lost
    if(a%2 == 0):
        global playerones
        playerones = playerones - 1
        if(playerones == 0):
            Lost = -1
    else:
        global playertwos
        playertwos = playertwos - 1
        if(playertwos == 0):
            Lost = -1
def ghost(a):
    global Lost
    global word
    global duck
    global mylist2
    if(a%2 == 0):
        w = str(input('Enter a Letter player 1\n'))
        w = w.lower()
        if(len(w)>1 or len(w)<1):
            print ("only one")
            return ghost(a)
        elif(w in alph):
            for test in mylist2:
                if(word + w == test[:duck]):
                    jank = []
                    for t2 in mylist2:
                        if(word+w == t2[:duck]):
                            jank.append(t2)
                    mylist2 = jank
                    duck += 1
                    return w
            strike(a)
            if(Lost == -1):
                return "null"
            else:
                print ("player 1 has %i more strikes" %playerones)
                return ghost(a)
        else:
            return ghost(a)
        
    else:
        w = str(input('Enter a Letter player 2\n'))
        w = w.lower()
        if(len(w)>1 or len(w)<1):
            print ("only one")
            return ghost(a)
        elif(w in alph):
            for test in mylist2:
                if(word + w == test[:duck]):
                    jank = []
                    for t2 in mylist2:
                        if(word+w == t2[:duck]):
                            jank.append(t2)
                    mylist2 = jank
                    duck += 1   
                    return w
            strike(a)
            if(Lost == -1):
                return "null"
            else:
                print ("player 2 has %i more strikes" %playertwos)
                return ghost(a)
                
        else:
            return ghost(a)
            
            
            
i = random.randint(0, 1)
while i > -1 or Lost > -1:
    g = ghost(i)
    if(g != "null"):
        word += g
    print (word)
    i += 1
    if(word in mylist and len(word) > 3):
        loser = (i-1)
        i = -1
        break
    if(Lost == -1):
        loser = (i-1)
        i = -1
if(loser%2 == 0):
    if(Lost == -1):
        print ("player 1 has no more strikes so Player 2 wins")
    else:
        print ('player 1 finished the word %s' %word)
else:
    if(Lost == -1):
        print ("player 2 has no more strikes so Player 1 wins")
    else:
        print ('player 2 finished the word %s' %word)
