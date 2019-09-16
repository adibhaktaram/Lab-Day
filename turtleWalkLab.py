import random
import turtle
def randomWalk(turtle, n):
    for i in range(n):
        x = random.uniform(0,1)
        if(x <= 0.25):
            turtle.lt(90)
            turtle.fd(25)
            turtle.rt(90)
        elif(x <= 0.5):
            turtle.rt(90)
            turtle.fd(25)
            turtle.lt(90)
        elif(x <= 0.75):
            turtle.fd(25)
        elif(x <= 1):
            turtle.lt(180)
            turtle.fd(25)
            turtle.rt(180)

bob = turtle.Turtle()
randomWalk(bob, 200)

turtle.mainloop()
