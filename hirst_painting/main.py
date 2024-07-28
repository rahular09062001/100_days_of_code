import turtle as t
import random as rd

tim = t.Turtle()
screen = t.Screen()
t.colormode(255)

color = [(228, 227, 226), (246, 237, 243), (243, 244, 246), (234, 166, 59), (45, 112, 157), (113, 150, 203), (212, 123, 164), (16, 128, 96), (172, 44, 88), (1, 177, 143)]

tim.setheading(230)
tim.penup()
tim.forward(350)
tim.setheading(0)
tim.speed(10)
def hirst_painting(x,y,color):
    tim.width(20)
    for j  in range (y):
        for  i  in range (x):
            tim.color(rd.choice(color))
            tim.pendown()
            tim.forward(1)
            tim.penup()
            tim.forward(49)
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(50*x)
        tim.left(180)

hirst_painting(10,10,color)
screen.exitonclick()
