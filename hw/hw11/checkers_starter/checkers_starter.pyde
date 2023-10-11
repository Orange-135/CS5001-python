'''
Group Member: Yilu Xu, Yulin Chen
'''

from board import Board 
# from checker import Checker
BOX_NUM = 2
BOX_SIZE = 60

BOARD = Board(BOX_SIZE, BOX_NUM)
holdingChecker = None

def setup():
    global img
    size(BOX_NUM * BOX_SIZE, BOX_NUM * BOX_SIZE)
    img = loadImage("crown.png")

    
def render(img):
    #draw background
    for x in range(BOX_NUM):
        for y in range(BOX_NUM):
            if((x - y) % 2 == 1):
                fill(*(234, 221, 202))
            else:
                fill(*(255, 255, 0))
            rect(x * BOX_SIZE, y * BOX_SIZE, BOX_SIZE, BOX_SIZE)
    
    BOARD.render(img)
    
def mousePressed():
    global holdingChecker
    global BOARD
    x = mouseX // BOX_SIZE
    y = mouseY // BOX_SIZE

    if holdingChecker == None:
        holdingChecker = BOARD.getClickedChecker(x, y)
    if (holdingChecker != None):
        holdingChecker.invise = True
        BOARD.tempChecker.invise = False
        BOARD.tempChecker.isAI = holdingChecker.isAI
        BOARD.tempChecker.isKing = holdingChecker.isKing
        
    
        
def mouseReleased():
    global holdingChecker
    global BOARD
    BOARD.tempChecker.invise = True
    if holdingChecker != None:
        holdingChecker.invise = False
        holdingChecker.new_x = mouseX // BOX_SIZE
        holdingChecker.new_y = mouseY // BOX_SIZE
        
    holdingChecker = None

def input():
    global BOARD
    x = mouseX // BOX_SIZE
    y = mouseY // BOX_SIZE
    BOARD.tempChecker.x = x
    BOARD.tempChecker.y = y
    
def update():
    global BOARD
    BOARD.update()
    

    
#called every 14ms    
def draw():
    input()
    update()
    render(img)
    # if holdingChecker != None:
    #     square((holdingChecker.x + 1) * BOX_SIZE, (holdingChecker.y - 1) * BOX_SIZE, BOX_SIZE)
    #     square((holdingChecker.x - 1) * BOX_SIZE, (holdingChecker.y - 1) * BOX_SIZE, BOX_SIZE)

 
 
