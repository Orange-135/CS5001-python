import random
import os
from board import Board

ROWS, COLS = 8, 8 
WIDTH, HEIGHT = 600, 600
CELL_SIZE = WIDTH//COLS
WHITE = color(255, 255, 255)
BLACK = color(0, 0, 0)

class GameController:
    def __init__(self, player_name):
        self.player_name = player_name
        self._init()  

    def update(self):
        """update the position of pieces from board"""
        self.board.draw()

    def _init(self):
        """make it more clear to reset the piece"""
        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.vaild_moves = {}

    def reset(self):
        """reset the piece"""
        self._init()

    def select(self, row, col):
        """define the rule of selected pieces"""
        if self.selected:
            result = self._move(row, col)
            #if the selected piece can not be moved, the selected piece should be returned
            if not result:
                self.selected = None
                return self.select(row, col)
        
          #check all the pieces that can be moved and store them.
          #if no piece can be moved, return false.
        piece = self.board.get_pos(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.vaild_moves = self.board.get_valid_moves(piece)
            return True
     
        return False
    
    def mouse_drag(self, x, y):
        """when mouse drags, selected should always be updated"""
        if self.selected:
            self.selected.update_position(x, y)

    def drop_piece(self, x, y):
        """make the rule when player drop the piece"""
        if self.selected:
            row = int(y // CELL_SIZE)
            col = int(x // CELL_SIZE)
            if (row, col) in self.vaild_moves:
                self.board.move(self.selected, row, col)
                skipped = self.vaild_moves[(row, col)]
                if skipped:
                    self.board.remove(skipped)
                self.swap_turn()
            else:
                self.selected.piece_pos()
            self.selected = None
            self.vaild_moves = {}
        
    def _move(self, row, col):
        """move the selected piece which can be moved"""
        piece = self.board.get_pos(row,col)
        if self.selected and piece == 0 and (row, col) in self.vaild_moves:
            self.board.move(self.selected, row, col)
            skipped = self.vaild_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.swap_turn()
            return True
        else:
            return False

#I tried to design the ai move, which firstly protects own pieces from be eaten
#then find the opportunity to eat opponent's piece
#if nither of above two circumtances exists, randomly selects the piece that can be moved
#unfortunely. I failed to run with this design.
#so I adopted easilier one, which firstly considers to eat opponent's piece
#if AI can not eat the other's piece, randomly selects the piece that can be moved. 
    def ai_move(self):
        """Automatically move the AI"""
        all_valid_moves = {}
        all_pieces = []
    
        # create a list of all AI pieces' positions
        for i in range(ROWS):
            for j in range(COLS):
                if self.board.get_pos(i, j) != 0 and self.board.get_pos(i, j).color == self.turn:
                    all_pieces.append((i, j))
        # iterate through all_pieces to find valid moves for each piece
        for i, j in all_pieces:
            piece = self.board.get_pos(i, j)
            moves = self.board.get_valid_moves(piece)
            if moves:
                all_valid_moves[(i, j)] = moves
    
        capture_moves = {}
        # Find all moves that result in capturing opponent's pieces
        for start_pos, end_positions in all_valid_moves.items():
            for end_pos, skipped in end_positions.items():
                if skipped:
                    if start_pos not in capture_moves:
                        capture_moves[start_pos] = {}
                    capture_moves[start_pos][end_pos] = skipped
    
        if capture_moves:
            # randomly choose one capturing move from capture_moves
            start_pos, end_positions = random.choice(list(capture_moves.items()))
        elif all_valid_moves:
            # randomly choose one piece's position from all_valid_moves
            start_pos, end_positions = random.choice(list(all_valid_moves.items()))
        else:
            return
    
        end_pos = random.choice(list(end_positions.keys()))
        piece = self.board.get_pos(*start_pos)
        self.board.move(piece, *end_pos)
        # check if any pieces were skipped and remove them if necessary
        skipped = end_positions[end_pos]
        if skipped:
            self.board.remove(skipped)
    
        self.swap_turn()

    def game_over(self):
        """determine the rule of becoming the winner"""
        white_lost = (self.board.white_left == 0) or (not self.board.has_valid_moves(WHITE))
        black_lost = (self.board.black_left == 0) or (not self.board.has_valid_moves(BLACK))
        
        if white_lost or black_lost:
            print("Game over!") 
            if white_lost:
               winner = "AI"
            else:
               winner = str(self.player_name)
            self.update_scores(winner)
            self.reset()
            #aviod the condition updating game_over() too many times
            self.game_ended = True
            return True
        return False

    def update_scores(self, winner):
        """update the score into the file"""
        scores = {}
        
        #create the empty file named scores.txt 
        if not os.path.exists("scores.txt"):
            open("scores.txt", "w").close()
        #read the context of scores.txt
        with open("scores.txt", "r") as file:
            for line in file.readlines():
                name, score = line.strip().split()
                scores[name] = int(score)
        #update scores
        scores[winner] = scores.get(winner, 0) + 1
        #write score into the scores.txt
        with open("scores.txt", "w") as file:
            for name, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
                line = "{name} {score}\n".format(name=name, score=score)
                file.write(line)

    def swap_turn(self):
        """change the turn"""
        self.vaild_moves = {}
        if self.turn == WHITE:
            self.turn = BLACK
            self.ai_move()
        else:
            self.turn = WHITE

        self.game_over()
