SIZE = (600, 600)
STROKE_WEIGHT = 3
SPACESHIP_POINTS = (-16, 10,  0, -30, 16, 10)
THRUST_INCREMENT = 0.5
ROTATION_INCREMENT = 3
SIZE_X = 600
SIZE_Y = 600
CIRCLE_RAD = 75
CIRCLE_INCREMENT = 1
GRAY_COLOR = (0.5, 0.5, 0.5)
WHITE_COLOR = (1.0, 1.0, 1.0)
LIGHT_BLUE_COLOR = (0.8, 0.9, 1.0)

thrust_factor = 0
spaceship_x = 300
spaceship_y = 300
x_vel = 0
y_vel = 0
rotation = 0
circle_x = 300
circle_1_y = 100
circle_2_y = 300
circle_3_y = 500


def setup():
    size(*SIZE)
    colorMode(RGB, 1)
    strokeWeight(STROKE_WEIGHT)


def draw():
    global rotation
    global circle_x
    background(0)
    circle_x = circle_x + CIRCLE_INCREMENT

    if circle_x > SIZE_X + CIRCLE_RAD:
        circle_x = circle_x - SIZE_Y
    elif circle_x > SIZE_X - CIRCLE_RAD:
        draw_circle_1(circle_x - SIZE_X)
        draw_circle_2(circle_x - SIZE_X)
        draw_circle_3(circle_x - SIZE_X)
    draw_circle_2(circle_x)

    draw_spaceship()
    rotate(radians(-rotation))
    translate(-spaceship_x, -spaceship_y)

    draw_circle_1(circle_x)
    draw_circle_3(circle_x)


def keyPressed():
    global rotation
    global thrust_factor
    if (key == CODED):
        if keyCode == UP:
            thrust_factor = THRUST_INCREMENT
        if keyCode == RIGHT:
            rotation += ROTATION_INCREMENT
        if keyCode == LEFT:
            rotation -= ROTATION_INCREMENT


def draw_spaceship():
    global spaceship_x
    global spaceship_y
    global x_vel
    global y_vel
    global thrust_factor
    global circle_1_y
    global circle_2_y
    x_vel = (x_vel + sin(radians(rotation))) * thrust_factor
    y_vel = (y_vel - cos(radians(rotation))) * thrust_factor

    spaceship_x = spaceship_x + x_vel
    spaceship_y = spaceship_y + y_vel

    translate(spaceship_x, spaceship_y)
    rotate(radians(rotation))
    fill(0)
    stroke(1)
    strokeWeight(STROKE_WEIGHT)
    triangle(*SPACESHIP_POINTS)


def draw_circle_1(x):
    fill(*GRAY_COLOR)
    stroke(*WHITE_COLOR)
    ellipse(x, circle_1_y, CIRCLE_RAD*2, CIRCLE_RAD*2)


def draw_circle_2(x):
    fill(*LIGHT_BLUE_COLOR)
    stroke(*WHITE_COLOR)
    ellipse(circle_2_y, x, CIRCLE_RAD*2, CIRCLE_RAD*2)


def draw_circle_3(x):
    fill(*GRAY_COLOR)
    stroke(*WHITE_COLOR)
    ellipse(x, circle_3_y, CIRCLE_RAD*2, CIRCLE_RAD*2)
