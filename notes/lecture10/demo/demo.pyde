# size(500, 300)
# background(225, 60, 0) #background color: red, green, blue
# fill(0, 200, 0) #fill the color of the circle

# stroke(255) #fill the color of the outline
# strokeWeight(5) #determine the width of the outline
# circle(250, 150, 100) #circle: long of the size(start with the radius), wide, diameter
# circle(250, 155, 50)

# fill(200, 0, 100)
# circle(250, 100, 50) #will recover the previous circle

x = 0
# should be global


# can not be changed
def setup():
    size(500, 300)


def draw():
    global x
    x += 1
    background(250, 150, 0)
    # notice the position

    strokeWeight(5)
    stroke(255)
    fill(0, 0, 200)
    circle(x, 150, 100)

    fill(250, 0, 0)
    noStroke()
    circle(mouseX, mouseY, 30)
