import turtle

RADIUS = 264
DIMENSION = 3 * RADIUS
POSITION = 0
HEADING_ANGLE = 72
PENTAGON = 5
STAR_PIXEL = 500
STAR_ANGLE = 144


def setup(dimension, starting, radius):
    turtle.setup(width=dimension, height=dimension)
    turtle.penup()
    turtle.setposition(starting, radius)
    turtle.pendown()


def draw_circle(outline, fill, radius):
    turtle.color(outline, fill)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def draw_star(outline, fill, set_head, shape_factor, length, shape_angle):
    turtle.color(outline, fill)
    turtle.begin_fill()
    turtle.setheading(set_head)
    for _ in range(shape_factor):
        turtle.forward(length)
        turtle.right(shape_angle)
    turtle.end_fill()


def main():

    setup(DIMENSION, POSITION, RADIUS)
    draw_circle('blue', 'cyan', -RADIUS)
    draw_star('red', 'yellow', -HEADING_ANGLE, PENTAGON, STAR_PIXEL, STAR_ANGLE)

    turtle.exitonclick()
    turtle.done()


main()