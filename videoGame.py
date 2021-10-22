#Justin Farquharson
#09/26/2021
#COP 2500C
#Video Game

import random

games = 0
groups = 0

while(games < 20):
    size = random.randint(1,4)
    #print(size)
    groups = groups+1
    print("Visiting Group #", groups)
    #This will determine if there's space for user to play with this group
    if (size < 4 and games < 20):
        print("Played Game")
        games = games+1
        chance = random.randint(1,10)
        #print("c:",chance)
        #This section will determine if they will play again with the same group
        for a in range(chance):
            if (chance <= 5 and games < 20):
            #for a in range(chance):
                print("Played Game")
                games = games+1
