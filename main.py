import turtle as t
import random
from colours import color_list

tim = t.Turtle()
t.colormode(255)
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.forward(500)

for _ in range(10):
    tim.penup()
    tim.backward(500)
    tim.left(90)
    tim.forward(50)
    tim.right(90)
    for _ in range(10):
        tim.pensize(10)
        tim.pendown()
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)



screen = t.Screen()
screen.exitonclick()