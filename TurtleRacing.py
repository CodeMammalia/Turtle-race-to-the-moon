import tkinter as tk
import turtle
import time
import random

WIDTH, HEIGHT = 700, 700
COLORS = ['red', 'green', 'blue', 'orange', 'maroon', 'black', 'purple', 'pink', 'brown', 'cyan']
drawer = turtle.Turtle()

def printInput():
	frame = tk.Tk()
	frame.title("TextBox Input")
	frame.geometry('400x200')

	inp = inputtxt.get(1.0, "end-1c")
	lbl.config(text = "Provided Input: "+inp)
	
	# TextBox Creation
	inputtxt = tk.Text(frame, height = 5, width = 20)
  
	inputtxt.pack()
	
	# Button Creation
	printButton = tk.Button(frame, text = "Enter", command = printInput)
	printButton.pack()
	
	# Label Creation
	lbl = tk.Label(frame, text = "")
	lbl.pack()
	frame.mainloop()

#How many racers will there be

def get_number_of_racers():
	racers = 0
	while True:
		racers = input('Enter the number of racers (2 - 10): ')
		if racers.isdigit():
			racers = int(racers)
		else:
			print('Input is not numeric... Try Again!')
			continue

		if 2 <= racers <= 10:
			return racers
		else:
			print('Number not in range 2-10. Try Again!')
	
#the race to be

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
		racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
		racer.pendown()
		turtles.append(racer)

	return turtles


#Setting up the window/Screen

def init_turtle():
	screen = turtle.Screen()
	screen.setup(WIDTH, HEIGHT)
	screen.title('Turtle Racing!')

#Here the Drawing turtle will create the finish line

def Finish_drawer():

	drawer.hideturtle()
	drawer.penup()
	
	#go to left side end of screen
	drawer.goto(-WIDTH, ((HEIGHT  // 2) - 100))
	drawer.pendown()
	
	#go to middle of screen
	drawer.goto(0, ((HEIGHT  // 2) - 100))

	#write Finish Line
	drawer.write("Finish Line!", align=tk.CENTER)
	
	#go to end of the screen on the right
	drawer.goto(WIDTH,  ((HEIGHT  // 2) - 100))
	drawer.penup()

def Write_Winner():

	drawer.goto(0, ((HEIGHT  // 2) - 100) + 25)
	drawer.pendown
	drawer.write(winner + "won!", align=tk.CENTER)
	drawer.penup

#printInput()

racers = get_number_of_racers()

#shuffle the color order to be different once
random.shuffle(COLORS)

for i in range(3):

	init_turtle()
	print(racers)

	colors = COLORS[:racers]

	Finish_drawer()

	winner = race(colors)

	Write_Winner

	time.sleep(3)

	turtle.clearscreen()

	Finish_drawer()

else:

	turtle.done()
