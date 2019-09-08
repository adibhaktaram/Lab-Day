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

def circle(t, r,):
    circumference = 2 * math.pi *r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(bob, length, n)

bob = turtle.Turtle()
bob.ht()

def polygonTwo(t, length, n):
        for _ in range(n * angle):
            angle = angle/360
            t.fd(length)
            t.lt(360 / n)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n

    for _ in range(n):
        t.fd(step_length)
        t.lt(step_angle)

bob = turtle.Turtle()
bob.ht()

arc(bob, 100, 180)

turtle.mainloop()
