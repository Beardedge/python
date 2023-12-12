import turtle as t
from random import choice

color_list = [(5, 13, 37), (38, 21, 16), (130, 89, 57), (201, 140, 118), (234, 210, 85), (187, 138, 162), (213, 86, 69), (79, 8, 20), (38, 137, 63), (194, 80, 100), (145, 85, 104), (31, 87, 29), (74, 107, 139), (220, 177, 212), (25, 203, 173), (126, 160, 180), (152, 138, 63), (13, 71, 25), (10, 61, 136), (115, 186, 157), (123, 12, 31), (86, 133, 174), (21, 208, 218), (230, 175, 166), (240, 208, 6), (133, 223, 206), (103, 41, 33), (183, 189, 205), (75, 84, 32), (132, 217, 221), (6, 246, 217)]

jim = t.Turtle()
jim.speed("fastest")
jim.hideturtle()
t.colormode(255)
jim.penup()
jim.goto(-250,-200)

number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    jim.color(choice(color_list))
    jim.dot(20)
    jim.forward(50)

    if dot_count % 10 == 0 and dot_count < 100:
        jim.setheading(90)
        jim.forward(50)
        jim.setheading(180)
        jim.forward(500)
        jim.setheading(0)

screen = t.Screen()
screen.exitonclick()