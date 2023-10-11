SIZE = (600, 600)
spaceship_x = 300
spaceship_y = 300
trust_factor = 0
x_vel = 0
y_vel = 0
rotation = 0


def setup():
    size(*SIZE)
    # represent color channels on 0.0 to 1.0 scale
    colorMode(RGB, 1)


def draw():
    background(0)
    draw_spaceship()


def keyPressed():
    global rotation
    global trust_factor
    if (key == CODED):
        if keyCode == UP:
            trust_factor = 0.5
        if keyCode == RIGHT:
            rotation += 3
        if keyCode == LEFT:
            rotation -= 3


def draw_spaceship():
    global spaceship_x
    global spaceship_y
    global x_vel
    global y_vel
    global trust_factor

    x_vel = (x_vel + cos(radians(rotation))) * trust_factor
    y_vel = (y_vel + sin(radians(rotation))) * trust_factor

    spaceship_x = spaceship_x + x_vel
    spaceship_y = spaceship_y + y_vel

    translate(spaceship_x, spaceship_y)
   # should be put in the front of draw
    rotate(radians(rotation))

    fill(0)
    stroke(1)
    strokeWeight(3)
    # triangle(-16, 10, 0, -30, 16, 10)
    triangle(-10, -16, 30, 0, -10, 16)
