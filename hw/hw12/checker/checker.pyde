from game_controller import GameController

FPS = 60
ROWS, COLS = 8,8
WIDTH, HEIGHT = 600, 600
WHITE = color(255, 255, 255)
YELLOW = color(255, 255, 200)
BLACK = color(0, 0, 0)
CELL_SIZE = WIDTH//COLS


def setup():
    global gc, answer
    size(WIDTH, HEIGHT)
    frameRate(FPS)

    answer = input('enter your name')
    if answer:
        print('hi ' + answer)
    elif answer == '':
        print('[empty string]')
    else:
        print(answer) # Canceled dialog will print None
        
    gc = GameController(answer)

def input(self, message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)

def draw():
    global gc
    background(YELLOW)
    gc.update()
    gc.game_over()

def mousePressed():
    global gc
    row = int(mouseY // CELL_SIZE)
    col = int(mouseX // CELL_SIZE)
    if gc.select(row, col):
       gc.update()
       
def mouseDragged():
    global gc
    gc.mouse_drag(mouseX, mouseY)

def mouseReleased():
    global gc
    gc.drop_piece(mouseX, mouseY)
    gc.game_over()
