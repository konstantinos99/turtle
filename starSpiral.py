from turtle import *

def starSpiral(length=10):
    speed(0)
    shape('turtle')
    for i in range(0, 60):
        for x in range(0, 5):
            forward(length)
            right(144)
        right(5)
        length += 5
    
starSpiral()
