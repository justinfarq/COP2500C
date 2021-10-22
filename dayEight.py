import turtle

#for count in range(3):

    #for x in range(3):

        #for x2 in range(3):
            #turtle.forward(100)
            #turtle.left(120)

        #turtle.penup()
       # turtle.forward(120)
        #turtle.pendown()
    
    #turtle.penup()
    #turtle.left(180)
    #turtle.forward(360)
    #turtle.left(90)
    #turtle.forward(120)
    #turtle.left(90)

    #turtle.pendown()


def drawTriangle(flowerSize):
    for z in range(3):
        turtle.forward(flowerSize)
        turtle.left(120)


def drawBox(stemLength):
    for z in range(2):
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(stemLength)
        turtle.left(90)
def drawFlower(stemL, flowerS):
    drawBox(stemL)
    turtle.left(90)
    turtle.forward(stemL)
    turtle.left(90)
    turtle.forward(flowerS/2 - 5)
    turtle.left(180)
    drawTriangle(flowerS)

drawFlower(50, 50)
turtle.penup()

turtle.goto(120,0)
turtle.pendown()
drawFlower(200, 100)
turtle.penup()


turtle.goto(240,0)
turtle.pendown()

drawFlower(150, 200)
