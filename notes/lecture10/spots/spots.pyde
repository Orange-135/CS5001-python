from spot import Spot
from stack import Stack
to_draw = Stack()


def setup():
    size(500, 400)


def draw():
    background(180)
    for spot in to_draw.contents:
        spot.display()


def mousePressed():
    to_draw.push(Spot(mouseX, mouseY))


def keyPressed():
    if key == "x" or key == "X":
        to_draw.pop()
        print("Undo the last added spot.")
