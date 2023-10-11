from checker import Checker
class Board():
    def __init__(self, BOX_SIZE, BOX_NUM):
        
        self.BOX_NUM = BOX_NUM
        self.BOX_SIZE = BOX_SIZE
        self.game_object = []
        self.game_object.append(Checker(0, BOX_NUM - 1, BOX_SIZE, BOX_NUM, False))
        self.game_object.append(Checker(2, BOX_NUM - 1, BOX_SIZE, BOX_NUM, False))
        self.game_object.append(Checker(2, 2, BOX_SIZE, BOX_NUM, True))

        self.tempChecker = Checker(-1, -1, BOX_SIZE, BOX_NUM, False)
        self.tempChecker.invise = True
        self.tempChecker.isHighlight = True
    def getClickedChecker(self, x, y):
        for checker in self.game_object:
            if checker.x == x and checker.y == y:
                if not checker.isAI:
                    return checker
        return None

    def update(self):
         for checker in self.game_object:
            checker.update(self.game_object)
            
    def render(self, img):
        for checker in self.game_object:
            checker.render(img)
        self.tempChecker.render(img)
                        
