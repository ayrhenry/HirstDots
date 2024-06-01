# import colorgram

#code used to get colors from the image using the colorgram library
# list = []
# colors = colorgram.extract('image.jpg', 30)


# for color in colors:
#     rgb = color.rgb
#     color_values = (rgb.r, rgb.g, rgb.b)
#     list.append(color_values)

# print(list)

from turtle import *
from random import *

turtle = Turtle()
random = Random()
screen = Screen()
screen.colormode(255)
turtle.shape("circle")
y_pos = -200
x_pos = -250
turtle.penup()
turtle.setpos(x_pos, y_pos)

dot_colors = [(236, 243, 250), (236, 226, 85), (211, 159, 109), (115, 176, 211), (202, 5, 69), (231, 53, 126), (195, 77, 20), (215, 133, 176), (194, 163, 14), (33, 106, 169),
    (10, 20, 65), (30, 189, 116), (232, 224, 4), (18, 28, 172), (234, 165, 197), (121, 187, 159), (203, 31, 130), (12, 186, 212), (10, 46, 25), 
    (143, 216, 200), (43, 17, 11), (39, 132, 71), (107, 92, 210), (182, 15, 8), (127, 219, 233), (233, 71, 40), (169, 178, 229)]



for x in range(10):
    for y in range(10):
        color_value = random.choice(dot_colors)
        turtle.color(color_value)
        turtle.stamp()
        #turtle.dot(20, color(color_value))
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()
        turtle.penup()
    y_pos += 50
    turtle.setpos(x_pos, y_pos)

turtle.hideturtle()
    
    
    
    










screen.exitonclick()