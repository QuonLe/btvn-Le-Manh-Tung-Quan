from turtle import *

speed(-1)

for x in range(3,7):
    if x==3:
        pencolor("blue")
    elif x==5:
        pencolor("blue")
    else:
        pencolor("red")

    for i in range(x):
        forward(100)
        left(360/x)
