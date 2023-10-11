class Spot:
    """A spot object with a x and y position
    that draws itself to the screen"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        noStroke()
        fill(255)
        circle(self.x, self.y, 95)
        fill(0)
        circle(self.x, self.y, 80)
        fill(255)
        circle(self.x, self.y, 65)
        fill(255, 0, 0)
        circle(self.x, self.y, 50)
        fill(255)
        circle(self.x, self.y, 25)
        fill(0)
        circle(self.x, self.y, 10)