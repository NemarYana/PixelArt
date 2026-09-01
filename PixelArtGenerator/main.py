import turtle
import random

turtle.tracer(0)
turtle.screensize(2000, 1500)
myPen = turtle.Turtle()
myPen.speed(0)

def box(intDim, color):
    myPen.color(color)    
    myPen.begin_fill()
    for _ in range(4):
        myPen.forward(intDim)
        myPen.left(90)
    myPen.end_fill()
    myPen.setheading(0)
    
boxSize = 10
colors = ['orange', '#FFDAB9', '#A0522D', '#FFF8DC', '#C0C0C0', '#F4A460']
colors2 = ['blue', 'red', 'yellow', 'green', 'purple', 'black', 'pink', 'brown']


def load_characters(file):
    characters = []
    current_character = []

    with open(file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    lines.append('')
            
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            if current_character:
                characters.append(current_character)
                current_character = []
            continue

        row = []
        for char in line:
            if char.isdigit():
                    row.append(int(char))
            
        current_character.append(row)
    
    return characters

def draw_picture(start_x, start_y):
    myPen.penup()
    myPen.goto(start_x, start_y)
    myPen.setheading(0)
    myPen.pendown()
    character = random.choice(characters)
    color = random.choice(colors)
    color2 = random.choice(colors2)
    for i in range(len(character)):
        for j in range(len(character[i])):
            if character[i][j] == 1:
                box(boxSize, 'black')
            elif character[i][j] == 2:
                box(boxSize, color)
            elif character[i][j] == 3:
                box(boxSize, color2)
            myPen.penup()
            myPen.forward(boxSize)
            myPen.pendown()
        myPen.penup()
        myPen.goto(start_x, myPen.ycor() - boxSize)
        myPen.pendown()

characters = load_characters('Pixel-art.txt')

rows = 3
cols = 3
spacing_x = 250 
spacing_y = 250 

for row in range(rows):
    for col in range(cols):
        start_x = -250 + col * spacing_x
        start_y = 200 - row * spacing_y
        draw_picture(start_x, start_y)

myPen.getscreen().update()
turtle.done()
