
class Checker():
    def __init__(self, x, y,  BOX_SIZE, BOX_NUM, isAI):
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.x = x
        self.y = y
        self.new_x = x
        self.new_y = y
        self.BOX_SIZE = BOX_SIZE
        self.BOX_NUM = BOX_NUM
        self.invise = False
        self.isAI = isAI
        self.isKing = False
        self.isHighlight = False

    def update(self, game_object):
        if self.isMoveable(game_object):
            self.x = self.new_x
            self.y = self.new_y
            if self.y == 0 and not self.isAI:
                self.isKing = True
            elif self.y == self.BOX_NUM - 1 and self.isAI:
                self.isKing = True        
        else:
            self.new_x = self.x
            self.new_y = self.y
                
    def die(self):
        self.x = -1
        self.y = -1
        self.invise = True
        
    def isMoveable(self, game_object):
        for item in game_object:
            if(item.x == self.new_x and item.y == self.new_y):
                return False
            if abs(self.new_y - self.y) == 2 and abs(self.new_x - self.x) == 2 and \
                (self.isKing or (not self.isAI and self.new_y < self.y) or (self.isAI and self.new_y > self.y)):
                meanY = (self.new_y + self.y) // 2
                meanX = (self.new_x + self.x) // 2
                if item.x == meanX and item.y == meanY and self.isAI != item.isAI:
                    item.die()
                    return True
        if not self.isAI and (self.new_x == self.x - 1 or self.new_x == self.x + 1) and self.new_y == self.y - 1:
                return True
        if self.isAI and (self.new_x == self.x - 1 or self.new_x == self.x + 1) and self.new_y == self.y + 1:
                return True
        if self.isKing and (self.new_x == self.x - 1 or self.new_x == self.x + 1) and (self.new_y == self.y - 1 or self.new_y == self.y + 1):
                return True
        return False
    
    def render(self, img):
        if self.invise:
            return 
        
            
        if not self.isAI:
            fill(*self.BLACK)

        if self.isAI:
            fill(*self.RED)
        if self.isHighlight:
            
            ellipse(self.x * self.BOX_SIZE + self.BOX_SIZE / 2, self.y  * self.BOX_SIZE + self.BOX_SIZE / 2, self.BOX_SIZE + 2, self.BOX_SIZE + 2)
        ellipse(self.x * self.BOX_SIZE + self.BOX_SIZE / 2, self.y  * self.BOX_SIZE + self.BOX_SIZE / 2, self.BOX_SIZE, self.BOX_SIZE)
        if self.isKing:
            fill(0, 0, 0)
            image(img, self.x * self.BOX_SIZE, self.y  * self.BOX_SIZE, self.BOX_SIZE, self.BOX_SIZE)    
    
        
