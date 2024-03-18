import turtle
t = turtle.Turtle()

def drawStar (myTurtle, sideLength, starPoints):
    sides = starPoints*2
    Angle = 360/sides
    for i in range (starPoints):
         if starPoints % 2 == 0:
             print ("Can't print Star")
             return
         else:
             myTurtle.left(180 - Angle)
             myTurtle.forward (sideLength)

drawStar (t,100,5)
drawStar (t,100,4)
