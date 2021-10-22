#Justin Farquhharson
#09/16/2021
#COP 2500C

subCost = float(input("How much does the sub cost?\n"))

while(subCost < 3 or subCost > 15):
    print("The sub cost needs to be between 3 and 15 dollars")
    subCost = float(input("How much are you going to pay?\n"))

money = float(input("How much are you going to pay?\n"))

while(money < subCost):
    print("You must pay for your sub with", subCost, "dollars or more")
    money = float(input("How much are you going to pay?\n"))

change = money - subCost

print("Your change is", change)

total = 0

for a in range(5):
    for b in range(2):
        total = total + 1

print(total)

total = 0

while(total < 20):
    for a in range(1,4):
        total = total + a

print(total)


import turtle
import random

def FtoC ( Fa ):
    C = 5/9 * (Fa - 32)

    return C


def drawTriangle(length):
    for a in range(3):
        turtle.forward(length)
        turtle.left(120)
        
for t in range(10):
    drawTriangle(t)
    turtle.penup()
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    turtle.setpos(x,y)
    turtle.pendown()
