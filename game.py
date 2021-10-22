#Justin Farquharson
#09/13/2021
#COP 2500C
#Knightro’s New Game

import random

number = random.randint(0,100)
print(number)
quest = input("For the UCF Golden Sword, has Knightro picked an odd or even number?\n")

if (quest == "even" and number%2 == 0):
    print("You guessed correct! The Golden Key is yours!")
elif (quest == "odd" and number%2 != 0):
    print("You guessed correct! The Golden Key is yours!")
else:
    print("I am sorry Knightro will look for someone else.")
