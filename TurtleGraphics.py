#TurtleGraphics.py
#Name: Luke Knofczynski
#Date: 2/12/25
#Assignment:

hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(myTurtle, sides):
    for s in range(sides):
        myTurtle.forward(75)
        myTurtle.right(360/sides)

def fillCorner(myTurtle, corner):
    drawSquare(myTurtle, 200)
   
    if corner == 1:
        myTurtle.begin_fill()
        drawSquare(myTurtle, 100)
        myTurtle.end_fill()
    elif corner == 2:
        myTurtle.forward(100)
        myTurtle.begin_fill()
        drawSquare(myTurtle, 100)
        myTurtle.end_fill()
    elif corner == 3:
        myTurtle.right(90)
        myTurtle.forward(100)
        myTurtle.left(90)
        myTurtle.begin_fill()
        drawSquare(myTurtle, 100)
        myTurtle.end_fill()
    elif corner == 4:
        myTurtle.right(90)
        myTurtle.forward(100)
        myTurtle.left(90)
        myTurtle.penup()
        myTurtle.forward(100)
        myTurtle.pendown()
        myTurtle.begin_fill()
        drawSquare(myTurtle, 100)
        myTurtle.end_fill()

def squaresInSquares(myTurtle, num):
    for q in range(num):
     drawSquare(myTurtle, (q+1)*30)
     myTurtle.penup()
     myTurtle.left(90)
     myTurtle.forward(15)
     myTurtle.left(90)
     myTurtle.forward(15)
     myTurtle.right(180)
     myTurtle.pendown()

def main():
    myTurtle = turtle.Turtle()    
   
    #drawSquare(myTurtle, 100)
    #drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon

    #fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    #fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    #squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    #squaresInSquares(myTurtle, 3) #draws 3 concentric squares
