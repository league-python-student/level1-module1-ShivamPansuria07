"""
Turtle Race
"""
import turtle
from random import randint
from PIL import Image

# ================= Instructions at the bottom of this file ===================


def screen_clicked(x, y):
    print('You pressed: x=' + str(x) + ', y=' + str(y))


def draw_background():
    filename = 'race_track.gif'

    try:
        image = Image.open(filename)
    except(FileNotFoundError, IOError):
        print("ERROR: Unable to find file " + filename)
        return

    window = turtle.Screen()
    window.setup(image.width + 100, image.height + 100, startx=0, starty=0)
    window.bgpic(filename)
    window.onclick(screen_clicked)

# ====================== DO NOT EDIT THE CODE ABOVE ===========================


if __name__ == '__main__':
    draw_background()

    # TODO 1) Create an empty list of turtles
    turtles = []
    # TODO 2) Create a new turtle and set its shape to 'turtle
    num = 195
    flag = False
    for i in range(8):
        if i > 0:
            num -= 55
        if i >=6:
           flag = True
        i = turtle.Turtle()
        i.penup()
        i.shape('turtle')
        i.speed(3)
        i.goto(-415, num)
        turtles.append(i)
    while flag:
        for index in range(len(turtles)):
            xturt = turtles[index].xcor()
            turtles[index].forward(randint(1,5))
            if turtles[index].xcor() == 335:
                print("Turtle Won!")
                flag = False







    # TODO 3) Set the turtle's speed to 3

    # TODO 6) use a loop to repeat the previous instructions and create
    #  8 turtles lined up on the left side of the screen
    #  *HINT* click on the window to print the corresponding x, y location

    # TODO 7) Move each turtle forward a random distance between 1 and 20

    # TODO 8) Create a loop to keep moving each turtle until a turtle
    #  crosses the finish linez`
    #  *HINT* click on the window to print the corresponding x, y location

    # TODO 9) When a turtle crosses the finish line, stop the race and
    #  indicate which turtle won the race.

    # EXTRA: Create different colors for each turtle and code a special
    # dance for the winning turtle!

    turtle.done()
