# fruit = 'Banana'
# fruit[0] = 'b'
# print(fruit)

# import pyfiglet
# import random 
# import time
# import os

# def clear_screen():
#     # Function to clear the screen in cmd
#     os.system('cls' if os.name == 'nt' else 'clear')

# def happy_birthday():
#     colors = ['red', 'green', 'blue', 'yellow', 'magenta','rose', 'cyan', 'white']
#     ascii_art = pyfiglet.figlet_format("Happy Birthday, my love", font="slant")
#     while True:
#         for color in colors:
#             # Print the text in different colors to create blinking effect
#             clear_screen()
#             print(pyfiglet.figlet_format("Happy Birthday, Rayhan", font="slant", justify="right"))
#             print("\033[{}m".format(random.randint(31, 37)), end='')
#             time.sleep(0.5)
#             clear_screen()
#             time.sleep(0.5)

# happy_birthday()

#A python code for wishing "Happy Birthday"

# import turtle
# import random

# bg = turtle.Screen()
# bg.bgcolor("black")

# turtle.penup()
# turtle.goto(-170,-180)
# turtle.color("white")
# turtle.pendown()
# turtle.forward(330)

# turtle.penup()
# turtle.goto(-160,-150)
# turtle.color("white")
# turtle.pendown()
# turtle.forward(305)

# turtle.penup()
# turtle.goto(-150,-120)
# turtle.color("white")
# turtle.pendown()
# turtle.forward(280)

# turtle.penup()
# turtle.goto(-100,-100)
# turtle.color("pink")
# turtle.begin_fill()
# turtle.pendown()
# turtle.forward(140)
# turtle.left(90)
# turtle.forward(95)
# turtle.left(90)
# turtle.forward(140)
# turtle.left(90)
# turtle.forward(95)
# turtle.end_fill()

# turtle.penup()
# turtle.goto(-90,0)
# turtle.color("red")
# turtle.left(180)
# turtle.pendown()
# turtle.forward(20)

# turtle.penup()
# turtle.goto(-60,0)
# turtle.color("blue")
# turtle.pendown()
# turtle.forward(20)

# turtle.penup()
# turtle.goto(-30,0)
# turtle.color("yellow")
# turtle.pendown()
# turtle.forward(20)

# turtle.penup()
# turtle.goto(0,0)
# turtle.color("green")
# turtle.pendown()
# turtle.forward(20)

# turtle.penup()
# turtle.goto(30,0)
# turtle.color("orange")
# turtle.pendown()
# turtle.forward(20)

# colors = ["red", "orange", "brown", "green", "blue", "purple", "grey"]
# turtle.penup()
# turtle.goto(-40,-50)
# turtle.pendown()

# for each_color in colors:
#     angle = 360 / len(colors)
#     turtle.color(each_color)
#     turtle.circle(10)
#     turtle.right(angle)
#     turtle.forward(10)

# turtle.penup()
# turtle.goto(-170, 50)
# turtle.color("cyan")
# turtle.pendown()
# turtle.write("Happy Birthday To You!", font=("Verdana", 25, "normal"))
# turtle.color("black")

# import time
# from random import randint

# for i in range(1,85):
#     print('')
 
# space = ''
# for i in range(1,1000):
#     count = randint(1, 100)
#     while(count > 0):
#         space += ' '
#         count -= 1
#     if(i%10==0):
#         print(space + '🎂Happy Birthday!')
#     elif(i%9 == 0):
#         print(space + "🎂")
#     elif(i%5==0):
#         print(space +"💛")
#     elif(i%8==0):
#         print(space + "🎉")
#     elif(i%7==0):
#         print(space + "🍫")
#     elif(i%6==0):
#         print(space + "Happy Birthday!Rayhan")
#     else:
#         print(space + "")
#     space = ''
#     time.sleep(0.2)


#!/usr/bin/python

# import curses
# import random

# stdscr = curses.initscr()
# curses.noecho()
# curses.cbreak()
# stdscr.keypad(1)
# curses.halfdelay(1)


# bg_frame = 'QlpoOTFBWSZTWbQ7eg8AAMr7gH/doChY84AQAATAAAAFMAF5QmDQEaEj00I0AyETaJqA9RoAGgCQkRoQjJoYEycRcmNn8JgkdWl1b9yeX1arHCrZQdpdJIGxJB6aEgzYB7ruc8VmVYsQ9WxWrvWPhlxxEqvBsyvw4iTxZwwNiD5QrmDIxRGKLWGUbmaaXxlps9c8t402JqzLay7FleFPkDSzMQg1thxMocVSOoYGvY3DYqWlms3MrxqgwBwjcJ0rQdy4RfmROTTYlz1Y8fJQ07dGkQ4F/F5dtrSQRxtXR3e4t3o338YtLd9vNYnGs754BlgKMk+bGH9JuYnrtylI7gS0NTGA0IyZmt+u6oiSqmdA1mEhp5IqGAYExHK0HIQaAsXtcyUig5VsziVGAHrbKalM/riEKj+SlgWsVJAy5oYEzxjJDNHH4u5IpwoSFodvQeA='.decode('base64').decode('bz2')
# main_dec = []
# minor_decs = []
# for y, bg_line in enumerate(bg_frame.split('\n')):
#   for x, bg_char in enumerate(bg_line):
#     if bg_char in '~*':
#       minor_decs.append((y, x, bg_char))
#     if y > 7: continue
#     if bg_char in '()':
#       if bg_char is '(' and bg_line[x+2] is not ')':
#         main_dec.append((y, x, bg_char))
#       if bg_char is ')' and bg_line[x-2] is not '(':
#         main_dec.append((y, x, bg_char))

# stdscr.addstr(0, 0, bg_frame)
# stdscr.refresh()
# denominator = 3
# finalized = False
# keyin = stdscr.getch()
# while keyin is -1 or not finalized:
#   if keyin is not -1:
#     finalized = True
#   random.shuffle(main_dec)
#   random.shuffle(minor_decs)
#   for index, dec in enumerate(main_dec[:len(main_dec)/denominator]):
#     if not finalized:
#       main_dec[index] = (dec[0], dec[1], '()'.strip(dec[2]))
#     else:
#       main_dec[index] = (dec[0], dec[1], ',')
#     stdscr.addstr(dec[0], dec[1], main_dec[index][2])
#   for index, minor_dec in enumerate(minor_decs[:len(minor_decs)/denominator]):
#     minor_decs[index] = (minor_dec[0], minor_dec[1], '*~'.strip(minor_dec[2]))
#     stdscr.addstr(minor_dec[0], minor_dec[1], minor_decs[index][2])
#   stdscr.move(0, 0)
#   stdscr.refresh()
#   keyin = stdscr.getch()


# curses.nocbreak()
# stdscr.keypad(0)
# curses.echo()
# curses.endwin()

import turtle

# Creating our turtle cursor to draw
my_turtle_cursor = turtle.Turtle()

# Creating a separate Canvas to draw "Happy Birthday"
my_turtle_screen = turtle.Screen()

# initializing a variable for co-ordinating
y_coordinate = -125


# Creating a function to draw a circle on top of stick
def draw_circle_on_top_of_stick(fill_color, border_color, x, y, radius):
    my_turtle_cursor.penup()
    my_turtle_cursor.pensize(3)
    # Changing color of our cursor
    my_turtle_cursor.color(fill_color)
    # Changing fill color of the cursor
    my_turtle_cursor.fillcolor(border_color)

    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.pendown()
    my_turtle_cursor.begin_fill()

    my_turtle_cursor.circle(radius)

    my_turtle_cursor.end_fill()

    my_turtle_cursor.getscreen().update()

def draw_candle_for_cake(fill_color, border_color, x, y):
    my_turtle_cursor.penup()

    # Changing color of our cursor
    my_turtle_cursor.color(border_color)
    # Changing fill color of the cursor
    my_turtle_cursor.fillcolor(fill_color)

    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.pendown()
    my_turtle_cursor.begin_fill()

    # Drawing the first side of our Candle
    my_turtle_cursor.forward(25)
    my_turtle_cursor.left(90)

    # Drawing the second side of our Candle
    my_turtle_cursor.forward(60)
    my_turtle_cursor.left(90)

    # Drawing the third side of our Candle
    my_turtle_cursor.forward(25)
    my_turtle_cursor.left(90)

    # Drawing the fourth side of our Candle
    my_turtle_cursor.forward(60)
    my_turtle_cursor.left(90)

    my_turtle_cursor.end_fill()

    my_turtle_cursor.getscreen().update()

# Creating a Function to draw stick on the candle
def draw_stick_on_candle(fill_color, x, y, cursor_size):
    my_turtle_cursor.penup()

    # Changing color of our cursor
    my_turtle_cursor.color(fill_color)

    # Changing fill color of the cursor
    my_turtle_cursor.fillcolor(fill_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.pensize(cursor_size)
    my_turtle_cursor.begin_fill()
    my_turtle_cursor.pendown()
    my_turtle_cursor.right(90)
    my_turtle_cursor.forward(12)
    my_turtle_cursor.end_fill()
    my_turtle_cursor.getscreen().update()

def write_happy_inside_circle(text_color, x, y):
    my_turtle_cursor.penup()
    # Changing color of our cursor
    my_turtle_cursor.color(text_color)

    # Changing fill color of the cursor
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.begin_fill()
    my_turtle_cursor.pendown()

    my_turtle_cursor.write("HBD", font=("sans-serif", 26, "bold"))

    my_turtle_cursor.getscreen().update()

def write_birthday_inside_circle(text_color, x, y):
    my_turtle_cursor.penup()
    # Changing color of our cursor
    my_turtle_cursor.color(text_color)

    # Changing fill color of the cursor
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.begin_fill()
    my_turtle_cursor.pendown()

    my_turtle_cursor.write("Rayhan", font=("sans-serif", 26, "bold"))

    my_turtle_cursor.getscreen().update()

def draw_stick(fill_color, border_color, x, y):
    my_turtle_cursor.penup()
    my_turtle_cursor.pensize(3)

    # Changing color of our cursor
    my_turtle_cursor.color(border_color)

    # Changing fill color of the cursor
    my_turtle_cursor.fillcolor(fill_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.begin_fill()
    my_turtle_cursor.pendown()
    my_turtle_cursor.left(180)
    my_turtle_cursor.forward(200)
    my_turtle_cursor.end_fill()
    my_turtle_cursor.getscreen().update()

# Function to draw topping of our cake
def draw_toppings_on_cake(fill_color, border_color, x, y, radius):
    my_turtle_cursor.penup()

    # Changing color of our cursor
    my_turtle_cursor.color(border_color)

    # Changing fill color of the cursor
    my_turtle_cursor.fillcolor(fill_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.pendown()
    my_turtle_cursor.begin_fill()

    # Drawing a circle using circle function
    my_turtle_cursor.forward(10)
    my_turtle_cursor.left(90)
    my_turtle_cursor.circle(radius, extent = 180)
    my_turtle_cursor.left(90)
    my_turtle_cursor.forward(10)
    my_turtle_cursor.end_fill()
    my_turtle_cursor.getscreen().update()

# Creating a Function to draw different layers of a cake
def draw_layer_of_the_cake(fill_color, border_color, cursor_size, x, y, width, height):
    my_turtle_cursor.hideturtle()
    my_turtle_cursor.penup()

    my_turtle_cursor.pensize(cursor_size)
    # Changing color of our cursor
    my_turtle_cursor.color(border_color)
    # Changing fill color of the cursor
    my_turtle_cursor.fillcolor(fill_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.pendown()

    # Starting the cursor to fill color
    my_turtle_cursor.begin_fill()

    for i in range(2):
        my_turtle_cursor.forward(width)
        my_turtle_cursor.left(90)
        my_turtle_cursor.forward(height)
        my_turtle_cursor.left(90)

    my_turtle_cursor.end_fill()
    my_turtle_cursor.setheading(0)
    my_turtle_cursor.getscreen().update()

# Changing the background color of our canvas
my_turtle_screen.bgcolor("#000")

# # Creating an empty list of different parts of our cake
parts_of_cake = []
parts_of_cake.append(["#A020F0", "#fff", 3, 30])
parts_of_cake.append(["#55FF55", "#fff", 3, 20])
parts_of_cake.append(["#B87333", "#fff", 3, 60])

# drawing an plate for our cake using draw_layer_of_the_cake() function
draw_layer_of_the_cake("#FFC0CB", "#fff", 3, -220, y_coordinate - 70, 400, 10)

# Drawing different parts of our cake
for parts in parts_of_cake:
    draw_layer_of_the_cake(parts[0], parts[1], parts[2], -135, y_coordinate - 60, 240, parts[3])
    y_coordinate += parts[3]


# drawing top topping of our cake
draw_toppings_on_cake("#C20067", "#fff", -120, y_coordinate - 60, 10)
draw_toppings_on_cake("#FFFF00", "#fff", -80, y_coordinate - 60, 10)
draw_toppings_on_cake("#FF0000", "#fff", 25, y_coordinate - 60, 10)
draw_toppings_on_cake("#0000FF", "#fff", 59, y_coordinate - 60, 10)

# drawing middle topping of our cakes
draw_toppings_on_cake("#FFA500", "#fff", -135, y_coordinate - 80, 10)
draw_toppings_on_cake("#E4E6EB", "#fff", -135, y_coordinate - 100, 10)
draw_toppings_on_cake("#FFA500", "#fff", -135, y_coordinate - 120, 10)
draw_toppings_on_cake("#181A18", "#fff", -80, y_coordinate - 80, 10)
draw_toppings_on_cake("#0000FF", "#fff", -65, y_coordinate - 110, 10)
draw_toppings_on_cake("#FFD700", "#fff", -95, y_coordinate - 140, 10)
draw_toppings_on_cake("#181A18", "#fff", 10, y_coordinate - 80, 10)
draw_toppings_on_cake("#E4E6EB", "#fff", -20, y_coordinate - 110, 10)
draw_toppings_on_cake("#181418", "#fff", 35, y_coordinate - 140, 10)
draw_toppings_on_cake("#FFA500", "#fff", 75, y_coordinate - 80, 10)
draw_toppings_on_cake("#E4E6EB", "#fff", 75, y_coordinate - 110, 10)
draw_toppings_on_cake("#FFD700", "#fff", 75, y_coordinate - 140, 10)

# Drawing candle on of our cake using draw_candle_for_cake() function
draw_candle_for_cake("#FFF44F", "#fff", -40, y_coordinate - 60)

# Drawing stick on top og uou candle
draw_stick_on_candle("#181A18", -26, y_coordinate + 15, 7)

# Drawing a stick for writing Happy Birthday
draw_stick("#fff", "#fff", 0, y_coordinate - 60)

# Drawing a circle on top of stick
draw_circle_on_top_of_stick("#fff", "#000", 100, y_coordinate + 235, 100)

# Writing "Happy" inside of our circle
write_happy_inside_circle("#fff", -70, y_coordinate + 240)

# Writing "Birthday" inside of our circle
write_birthday_inside_circle("#fff", -80, y_coordinate + 190)

# Calling done function at the end
turtle.done()

