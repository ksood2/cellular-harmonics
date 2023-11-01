from PIL import Image
import turtle
from turtle import Screen, Turtle
import os

def draw_kochs(turtle, length, n):
    if n == 0:
        turtle.forward(length)
    else:
        n -= 1
        length /= 3
        draw_kochs(turtle, length, n)
        turtle.right(60)
        draw_kochs(turtle, length, n)
        turtle.left(120)
        draw_kochs(turtle, length, n)
        turtle.right(60)
        draw_kochs(turtle, length, n)


def koch_snowflake(order):
    adjust = 2 / order
    WIDTH, HEIGHT = 1500, 1500
    screen = Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.setworldcoordinates(0,0, WIDTH/adjust, HEIGHT/adjust)
    screen.tracer(False)

    turtle = Turtle()
    turtle.hideturtle()
    for _ in range(3):
        draw_kochs(turtle, 600 * order, order)
        turtle.left(120)
    screen.update()
    #screen.mainloop()

    canvas = screen.getcanvas()
    canvas.postscript(file="./test.ps", width=WIDTH, height=HEIGHT)
    im = Image.open("./test.ps")
    filename = "./koch_" + str(order) + ".png"
    im.save(filename)
    im.close()
    os.remove("./test.ps")
    turtle.clear()

def turtle_star(n, size = 250):
    extent = 360 / n
    WIDTH = 1000
    HEIGHT = 1000
    adjust = 2
    screen = Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.setworldcoordinates(-WIDTH/adjust, -HEIGHT/adjust, WIDTH/adjust, HEIGHT/adjust)  # initial null change
    turtle.hideturtle()
    screen.tracer(False)
    if n % 2 == 0:
        coords = []
        for a in range(0, n):
            turtle.penup()
            if a==0:
                turtle.goto(0, 0)
            coords.append(turtle.pos())
            turtle.circle(size, extent)
        for b in range(0, len(coords)):
            if b % 2 == 0:
                turtle.pendown()
                turtle.goto(coords[b][0], coords[b][1])
            else:
                continue
        turtle.goto(coords[0][0], coords[0][1])
        turtle.penup()
        for c in range(0, (len(coords) + 1)):
            if c % 2 != 0:
                turtle.goto(coords[c][0], coords[c][1])
                turtle.pendown()
            else:
                continue
        turtle.goto(coords[1][0], coords[1][1])
    else:
        angle = 180 - (180 / n)
        for a in range(n):
            turtle.forward(size)
            turtle.right(angle)
    screen.update()
    canvas = screen.getcanvas()
    canvas.postscript(file="./test.ps", width=WIDTH, height=HEIGHT)
    im = Image.open("./test.ps")
    filename = "./star_" + str(n) + ".png"
    im.save(filename)
    im.close()
    os.remove("./test.ps")

if __name__ == "__main__":
    """for k in [5, 6, 7, 8, 9]:
        koch_snowflake(k)"""
    for k in [5, 6, 7, 8, 9]:
        turtle_star(k)
        turtle.clear()
        turtle.reset()
