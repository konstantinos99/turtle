from turtle import *

def myfunc(length=5):
    speed(0)
    shape('turtle')
    for i in range(0, 100):
        for x in range(0, 4):
            forward(length)
            right(90)
        right(5)
        length += 5
    
myfunc()