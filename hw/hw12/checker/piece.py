ROWS, COLS = 8,8
WIDTH, HEIGHT = 600, 600
CELL_SIZE = WIDTH//COLS
WHITE = color(255, 255, 255)
GREY = color(128, 128, 128)

class Piece:
    """draw each piece on the board"""
    PEDDING = 10
    OUTLINE = 2
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.piece_pos()
        
        self.CROWN_SIZE = (45, 25)

    def piece_pos(self):
        """determine the position of each piece"""
        self.x = CELL_SIZE * self.col + CELL_SIZE // 2
        self.y = CELL_SIZE * self.row + CELL_SIZE // 2

    def make_king(self):
        self.king = True

    def draw(self):
        """draw the color of pieces"""
        radius = CELL_SIZE//2 - self.PEDDING
        #draw the outline of pieces
        strokeWeight(self.OUTLINE * 2)
        stroke(GREY)
        noFill()
        ellipse(self.x, self.y, (radius + self.OUTLINE) * 2, (radius + self.OUTLINE) * 2)

        #darw the inner of pieces
        noStroke()
        fill(self.color)
        ellipse(self.x, self.y, radius * 2, radius * 2)
        
        #draw king png upper the piece
        if self.king:
            CROWN = loadImage("king.png")
            imageMode(CENTER)
            image(CROWN, self.x, self.y - self.CROWN_SIZE[1] // 4, *self.CROWN_SIZE)
    
    def move(self, row, col):
        """update the position of piece""" 
        self.row = row
        self.col = col
        self.piece_pos()
        
    def update_position(self, x, y):
        """update the position for temp"""
        self.x = x
        self.y = y
    
    def __repr__(self):
        return str(self.color)
