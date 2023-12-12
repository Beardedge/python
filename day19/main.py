import turtle as t
import random

def move_forward(turtle_name):
    turtle_name.forward(random.randint(0, 5))

red = t.Turtle()
red.shape("turtle")
red.color("red")
red.penup()
red.shapesize(2)

orange = t.Turtle()
orange.shape("turtle")
orange.color("orange")
orange.penup()
orange.shapesize(2)

yellow = t.Turtle()
yellow.shape("turtle")
yellow.color("yellow")
yellow.penup()
yellow.shapesize(2)

green = t.Turtle()
green.shape("turtle")
green.color("green")
green.penup()
green.shapesize(2)

blue = t.Turtle()
blue.shape("turtle")
blue.color("blue")
blue.penup()
blue.shapesize(2)

purple = t.Turtle()
purple.shape("turtle")
purple.color("purple")
purple.penup()
purple.shapesize(2)

list_of_racers = [red, orange, yellow, green, blue, purple]

screen = t.Screen()
wager = screen.textinput("Wagers", "Choose color to bet on:")

for racer in list_of_racers:
    racer.speed(5)

red.goto(-900, 150)
orange.goto(-900, 100)
yellow.goto(-900, 50)
green.goto(-900, 0)
blue.goto(-900, -50)
purple.goto(-900, -100)

for racer in list_of_racers:
    racer.speed(1)

screen.exitonclick()
