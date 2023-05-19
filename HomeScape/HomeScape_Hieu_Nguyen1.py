# Prolog
# Author:  Hieu Nguyen
# Email:  hnguyen182@student.gsu.edu
# Section: Section 004
# Python: Homework 4 
'''
Purpose:
    Introduce to turtle function, experience with writing loops, experience with recursion, experience with complex objects that have both attributes and methods, experience with using asserts to enforce your preconditions.
Pre-conditions (input):
    You shoud have walls, roof, door, windows(2-4), floower, clouds, and grass. 
Post-conditions (output):
    Print out the homescape with turtle function.
'''
"""
#main function
Apply Function(s) as needed - Turtle
draw_window(x, y): (x, y passing location)
Draw window without inner grid
Draw inner grid of window
Draw top and right side wall of house
Draw bottom and door of house
Draw left wall and roof
Draw_window(x, y) – first location
Draw_window(x, y) – second location
Draw_window(x, y) – third location
"""
import turtle



# Set up the turtle window
turtle.setup(1300, 1200)
turtle.title("My House Landscape")
turtle.bgcolor("white")
turtle.speed(0.0001)
# Draw the grass
turtle.penup()
turtle.goto(-700, -700)
turtle.pendown()
turtle.color("lime")
turtle.begin_fill()
turtle.goto(700, -700)
turtle.goto(700, 5)
turtle.goto(-700, 5)
turtle.goto(-700, -700)
turtle.end_fill()

# Draw the sky
turtle.penup()
turtle.goto(-700, 5)
turtle.pendown()
turtle.color("cyan")
turtle.begin_fill()
turtle.goto(700, 5)
turtle.goto(700, 900)
turtle.goto(-700, 900)
turtle.goto(-700, 5)
turtle.end_fill()

# Draw the sun
turtle.penup()
turtle.goto(-250, 410)
turtle.pendown()
turtle.color("yellow")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()


# Draw the house
turtle.penup()
turtle.goto(-200, -100)
turtle.pendown()
turtle.color("peach puff", "peru")
turtle.begin_fill()
turtle.goto(200, -100)
turtle.goto(200, 50)
turtle.goto(-200, 50)
turtle.goto(-200, -100)
turtle.end_fill()

# Draw the roof
turtle.penup()
turtle.goto(-200, 50)
turtle.pendown()
turtle.color("saddlebrown")
turtle.begin_fill()
turtle.goto(0, 150)
turtle.goto(200, 50)
turtle.goto(-200, 50)
turtle.end_fill()

# Draw the door
turtle.penup()
turtle.goto(-20, -100)
turtle.pendown()
turtle.color("saddlebrown")
turtle.begin_fill()
turtle.goto(20, -100)
turtle.goto(20, -40)
turtle.goto(-20, -40)
turtle.end_fill()

# Draw the doorknob
turtle.penup()
turtle.goto(15, -75)
turtle.pendown()
turtle.color("yellow")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

# Draw the windows
turtle.penup()
turtle.goto(-70, 10)
turtle.pendown()
turtle.color("saddlebrown", "white")
turtle.begin_fill()
for i in range(4):
    turtle.forward(40)
    turtle.right(90)
turtle.end_fill()

turtle.penup()
turtle.goto(-70, -10)
turtle.pendown()
turtle.color("#000000")
for i in range(2):
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)

    
turtle.penup()
turtle.goto(70, -30)
turtle.pendown()
turtle.color("saddlebrown", "#ffffff")
turtle.begin_fill()
for i in range(4):
    turtle.forward(40)
    turtle.right(90)
turtle.end_fill()

turtle.penup()
turtle.goto(70, -10)
turtle.pendown()
turtle.color("#000000")
for i in range(2):
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.pendown()


turtle.penup()
turtle.goto(100, 10)
turtle.pendown()
turtle.color("saddlebrown", "#ffffff")
turtle.begin_fill()
for i in range(4):
    turtle.forward(40)
    turtle.right(90)
turtle.end_fill()

turtle.penup()
turtle.goto(100, -10)
turtle.pendown()
turtle.color("#000000")
for i in range(2):
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.end_fill()

turtle.penup()
turtle.goto(-100, -30)
turtle.pendown()
turtle.color("saddlebrown", "#ffffff")
turtle.begin_fill()
for i in range(4):
    turtle.forward(40)
    turtle.right(90)
turtle.end_fill()

turtle.penup()
turtle.goto(-100, -10)
turtle.pendown()
turtle.color("#000000")
for i in range(2):
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.end_fill() 
# Draw the cloud
def filled_circle(radius, color):
    turtle.color(color,color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def cloud(radius, cloud_color ="white"):
    filled_circle(radius,cloud_color)
    turtle.forward(radius)
    filled_circle(radius,cloud_color)
    turtle.right(90)
    filled_circle(radius,cloud_color)
    turtle.right(90)
    filled_circle(radius,cloud_color)
    turtle.right(90)
    filled_circle(radius,cloud_color)
    turtle.right(90)

turtle.penup()
turtle.goto(100,300)
cloud(20)
turtle.goto(-50,275)
cloud(30)
turtle.goto(45,450)
cloud(50)
turtle.goto(-50,450)
cloud(5)
turtle.goto(-150,275)
cloud(15)
turtle.goto(-150,420)
cloud(10)
turtle.goto(-300,400)
cloud(30)
turtle.goto(150,275)
cloud(15)
turtle.goto(150,420)
cloud(10)
turtle.goto(300,400)
cloud(30)

# Draw the driveway
turtle.penup()
turtle.goto(-50, -100)
turtle.pendown()
turtle.color("grey")
turtle.begin_fill()
turtle.forward(100)
turtle.right(90)
turtle.forward(700)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(700)
turtle.end_fill()


turtle.penup()
turtle.goto(-350, -250)
turtle.pendown()
turtle.color("grey")
turtle.begin_fill()
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.end_fill()

# Draw the leaves
turtle.penup()
turtle.goto(-250, -200)
turtle.pendown()
turtle.color("dark green")
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

turtle.penup()
turtle.goto(-230, -150)
turtle.pendown()
turtle.color("dark green")
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()
turtle.color("dark green")
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()
turtle.pendown()

# Draw the grass
def draw_grass(x, y, size):
    turtle.speed(0.01)
    turtle.penup()
    turtle.goto(x, y)
    turtle.forward(size / 2)
    turtle.fillcolor("dark green")
    turtle.begin_fill()
    
    for i in range(15):
        turtle.left(10)
        turtle.forward(size / 3)
    
    turtle.left(220)
    for i in range(15):
        turtle.left(10)
        turtle.forward(size / 4)
    
    turtle.left(200)
    for i in range(19):
        turtle.left(10)
        turtle.forward(size / 4)
    
    turtle.forward(size/6 )
    turtle.left(90)
    turtle.forward(size / 6)
    turtle.end_fill()
    turtle.penup()
draw_grass(400,-350, 20)
turtle.left(80)
draw_grass(400,-250, 15)
turtle.left(80)
draw_grass(-300,-450, 20)
turtle.left(80)
draw_grass(-100,-400, 20)


#Draw the flower
def draw_flower(x, y, size):
    
    turtle.speed(0.01)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor("red")
    turtle.begin_fill()
    
    for i in range(5):
        turtle.circle(20, 50)
        turtle.circle(5, 180)
        turtle.left(180)
        turtle.circle(5, 180)
        turtle.circle(20, 50)
        turtle.left(170)
    
    turtle.end_fill()
    turtle.penup()
    
    turtle.goto(x - size /2  , y + size /2)
    turtle.pendown()
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    turtle.color("yellow")
    turtle.dot(size)
    turtle.end_fill()
    
    turtle.penup()
    turtle.goto(x - size /2  , y + size /2)
    turtle.pendown()
    turtle.pensize(size / 5)
    turtle.color("dark green")
    turtle.right(185)
    turtle.forward(size * 5)

draw_flower(450,-400, 10)
turtle.left(90)
draw_flower(400,-400, 10)
turtle.left(90)
draw_flower(350,-400, 10)
turtle.left(90)
draw_flower(300,-400, 10)
turtle.left(100)
draw_flower(250,-400, 10)

turtle.left(100)
draw_flower(400,-150, 10)
turtle.left(100)
draw_flower(350,-150, 10)
turtle.left(90)
draw_flower(300,-150, 10)
turtle.left(90)
draw_flower(250,-150, 10)
turtle.left(100)
draw_flower(200,-150, 10)

turtle.left(90)
draw_flower(-550,-350, 10)
turtle.left(90)
draw_flower(-500,-350, 10)
turtle.left(90)
draw_flower(-450,-350, 10)
turtle.left(100)
draw_flower(-400,-350, 10)
turtle.left(100)
draw_flower(-350,-350, 10)

# Draw the mountains
turtle.penup()
turtle.goto(200, 5)
turtle.pendown()
turtle.color("burlywood")
turtle.begin_fill()
turtle.goto(400, 150)
turtle.goto(650, 5)
turtle.end_fill()

turtle.penup()
turtle.goto(300, 5)
turtle.pendown()
turtle.color("peru")
turtle.begin_fill()
turtle.goto(500, 150)
turtle.goto(700, 5)
turtle.end_fill()


turtle.penup()
turtle.goto(-200, 5)
turtle.pendown()
turtle.color("burlywood")
turtle.begin_fill()
turtle.goto(-400, 150)
turtle.goto(-650, 5)
turtle.end_fill()

turtle.penup()
turtle.goto(-300, 5)
turtle.pendown()
turtle.color("peru")
turtle.begin_fill()
turtle.goto(-500, 150)
turtle.goto(-700, 5)
turtle.end_fill()


#draw the fence
def draw_fence(x, y, width, height, num_planks):
    plank_width = width / num_planks
    turtle.fillcolor("tan")
    turtle.penup()
    turtle.goto(x, y + height / 2)
    turtle.pendown()
    turtle.setheading(0)
    for i in range(num_planks):
        turtle.begin_fill()
        for j in range(2):
            turtle.forward(plank_width)
            turtle.right(90)
            turtle.forward(height / 3)
            turtle.right(90)
        turtle.end_fill()
        turtle.forward(plank_width)
draw_fence(50, -575, 650, 200, 20)
draw_fence(-50, -575, -650, 200, 20)


turtle.penup()
turtle.setposition(-40, -350)

# Draw the rectangle
turtle.fillcolor("dark green")
turtle.begin_fill()
turtle.pendown()
turtle.forward(60)
turtle.setheading(90)
turtle.forward(21)
turtle.setheading(180)
turtle.forward(60)
turtle.setheading(-90)
turtle.forward(21)
turtle.end_fill()

# Draw the left tire
turtle.fillcolor("black")
turtle.penup()
turtle.setposition(-35, -350)
turtle.pendown()
turtle.begin_fill()
turtle.forward(3.75)
turtle.setheading(0)
turtle.forward(7.5)
turtle.setheading(90)
turtle.forward(3.75)
turtle.end_fill()

# Draw the right tire
turtle.penup()
turtle.setposition(5, -350)
turtle.fillcolor("black")
turtle.begin_fill()
turtle.pendown()
turtle.setheading(270)
turtle.forward(3.75)
turtle.setheading(0)
turtle.forward(7.5)
turtle.setheading(90)
turtle.forward(3.75)
turtle.end_fill()

# Draw the uppermost line
turtle.penup()
turtle.setposition(-25, -310)
turtle.pendown()
turtle.setheading(0)
turtle.forward(28.12)

# Draw the second uppermost line
turtle.penup()
turtle.setposition(-25, -320)
turtle.pendown()
turtle.setheading(0)
turtle.forward(30)

# Draw the left slanted line
turtle.penup()
turtle.setposition(-25, -310)
turtle.pendown()
turtle.setposition(-35, -330)

# Draw the right slanted line
turtle.penup()
turtle.setposition(5, -310)
turtle.pendown()
turtle.setposition(15, -330)

# Draw the left circle
turtle.penup()
turtle.setposition(-25, -340)
turtle.pendown()
turtle.fillcolor("#ECFFDC")
turtle.begin_fill()
turtle.circle(1.875)
turtle.end_fill()

# Draw the right circle
turtle.penup()
turtle.setposition(5, -340)
turtle.pendown()
turtle.fillcolor("#ECFFDC")
turtle.begin_fill()
turtle.circle(1.875)
turtle.end_fill()

# Draw the horizontal lines
turtle.penup()
turtle.setposition(-15, -335)
turtle.pendown()
turtle.setposition(-15, -340)
turtle.penup()
turtle.setposition(-10, -335)
turtle.pendown()
turtle.setposition(-10, -340)
turtle.penup()
turtle.setposition(-5, -335)
turtle.pendown()
turtle.setposition(-5, -340)


# Hide the turtle
turtle.hideturtle()
# Display the landscape
turtle.done()
