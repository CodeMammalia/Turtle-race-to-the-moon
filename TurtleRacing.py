import tkinter as tk
import turtle
import time
import random

WIDTH, HEIGHT = 700, 600
COLORS = ['red', 'green', 'blue', 'orange', 'maroon', 'black', 'purple', 'pink', 'brown', 'cyan']
drawer = turtle.Turtle()
cash = 200


# How many racers will there be
def get_number_of_racers():
    racers = int(0)
    while True:
        racers = input('Enter the number of racers (2 - 10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Give me a number you loser')
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print('A number between 2 and 10. Can you read?')


# the race to be
def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 100:
                return colors[turtles.index(racer)]


# Here we will define how to create the turtle racers
def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles


# Setting up the window/Screen
def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing!')


# Here the Drawing turtle will create the finish line
def finishline_drawn():

    drawer.hideturtle()
    # drawer.hideturtle()
    drawer.penup()

    # go to left side end of screen
    drawer.goto(-WIDTH, ((HEIGHT // 2) - 100))
    drawer.pendown()

    # go to middle of screen
    drawer.goto(0, ((HEIGHT // 2) - 100))

    # write Finish Line
    drawer.write("Finish Line!", align=tk.CENTER)

    # go to end of the screen on the right
    drawer.goto(WIDTH, ((HEIGHT // 2) - 100))
    drawer.pendown()


def write_winner(winner):
    drawer.penup()
    drawer.goto(0, ((HEIGHT // 2) - 100) - 50)
    drawer.pendown()
    drawer.write(winner + " won!", align=tk.CENTER)


# racers = get_number_of_racers()

racers = 2

# shuffle the color order to be different once
random.shuffle(COLORS)

# Creates window
init_turtle()

finishline_drawn()

print("Let's get ready to rumble. The contestants are as follows")

for x in range(racers):
    print(str(COLORS[x]))

bet = input("Who will win?")

print("how much are you betting?")

bettingCash = input()

if bettingCash.isdigit():
    bettingCash = int(bettingCash)
else:
    print("A number you loser")

if bettingCash >= cash:
    # do something
else:
    print("Bitch you and what money")

colors = COLORS[:racers]

# starts the race
winner = race(colors)

write_winner(winner)

time.sleep(3)
