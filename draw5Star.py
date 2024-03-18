import turtle

t = turtle.Turtle()

def draw5Star (myTurtle, sideLength):
    myTurtle.right(36)
    myTurtle.forward(sideLength)#1
    myTurtle.right(108)
    myTurtle.backward(sideLength)#2
    myTurtle.left(36)
    myTurtle.forward(sideLength)#3
    myTurtle.right(108)
    myTurtle.backward(sideLength)#4
    myTurtle.left(36)
    myTurtle.forward(sideLength)#5
    myTurtle.right(108)
    myTurtle.backward(sideLength)#6
    myTurtle.left(36)
    myTurtle.forward(sideLength)#7
    myTurtle.right(108)
    myTurtle.backward(sideLength)#8
    myTurtle.left(36)
    myTurtle.forward(sideLength)#9
    myTurtle.right(108)
    myTurtle.backward(sideLength)#10

draw5Star (t,100)
