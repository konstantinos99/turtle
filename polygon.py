from turtle import *

def polygon(sides):
    speed(2)
    shape('turtle')
    for x in range(sides):
        forward(100)
        left(360 / sides)

polygon(6)

