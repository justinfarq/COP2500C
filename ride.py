#Justin Farquharson
#09/07/2021
#COP 2500C
#Knighto's Vehicles

import turtle
turtle.speed(20)

#Starting point for the bumpers
turtle.penup()
turtle.backward(200)
turtle.right(90)
turtle.forward(100)
turtle.pendown()
turtle.left(90)

#Bumper Tire
number = 0
while (number != 55):
    turtle.circle(30)
    turtle.forward(7)
    number = number + 1

#Bumper Base
turtle.left(90)
turtle.penup()
turtle.forward(60)
turtle.left(90)
turtle.forward(30)
turtle.right(90)
turtle.pendown()
turtle.circle(60,90)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.circle(10)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(210)
turtle.circle(60,90)

#BumperShield
turtle.penup()
turtle.left(90)
turtle.forward(60)
turtle.left(90)
turtle.forward(60)
turtle.pendown()
turtle.forward(55)
turtle.right(30)
turtle.forward(50)

#BumperBackRest
turtle.penup()
turtle.right(60)
turtle.forward(170)
turtle.pendown()
turtle.forward(15)
turtle.right(180)
turtle.forward(15)
turtle.left(90)
turtle.forward(99)

#Clearing Turtle from Bumper Car
turtle.penup()
turtle.forward(150)
