import turtle
import math
def square(t, length):
    for _ in range(4):
        t.fd(length)
        t.lt(90)

bob = turtle.Turtle()

def polygon(t, length, n):
    for _ in range(n):
        t.fd(length)
        t.lt(360/n)

bob = turtle.Turtle()

polygon(bob, 1, 360)

def circle(t, r):
    r = (length*n)/(2*math.pi)
    n = (2*math.pi*r)/length

    polygon(t, length, n)





turtle.mainloop()
