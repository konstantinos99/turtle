from turtle import *

def myfunc(length):
    speed(0)
    shape('turtle')
    for i in range(0, 60):
        for x in range(0, 4):
            forward(length)
            right(90)
        right(5)
    
myfunc(150)