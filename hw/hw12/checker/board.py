from piece import Piece

ROWS, COLS = 8,8
WIDTH, HEIGHT = 600, 600
CELL_SIZE = WIDTH//COLS
BROWN = color(139, 69, 19)
WHITE = color(255, 255, 255)
BLACK = color(0, 0, 0)

class Board:
    def __init__(self):
        self.board = []
        self.white_left = self.black_left = 12
        self.white_kings = self.black_kings = 0
        self.init_pieces()

    def draw_cubes(self):
        """draw the brown background of cubes on the board"""
        for i in range(ROWS):
            #select squares spaced one apart are filled in brown
            for j in range(i % 2, ROWS, 2):
                 fill(BROWN)
                 rect(i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE)

    def move(self, piece, row, col):
        #swap the position between two pieces
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        #promote piece to king if it reaches the end of the board
        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.black_kings += 1

    def get_pos(self, row, col):
        """get the specific position of piece from row and col"""
        return self.board[row][col]

    def init_pieces(self):
         """initialize the positions of AI, player, and no piece"""
         for i in range(ROWS):
            self.board.append([])
            for j in range(COLS):
                if j % 2 == ((i + 1) % 2):
                    if i < 3:
                        self.board[i].append(Piece(i, j, BLACK))
                    elif i > 4:
                        self.board[i].append(Piece(i, j, WHITE))
                    else:
                        self.board[i].append(0)
                else:
                    self.board[i].append(0)

    def draw(self):
        """draw the whole board (pieces and squares)"""
        self.draw_cubes()
        for i in range (ROWS):
            for j in range(COLS):
                piece = self.board[i][j]
                if piece !=0:
                    piece.draw()  

    def remove(self, pieces):
        """remove the piece"""
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == WHITE:
                    self.white_left -= 1
                else:
                    self.black_left -= 1  
    
    def get_valid_moves(self, piece):
        """get the valid moves"""
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        directions = []
        #determine which directions the piece can move in
        if piece.color == WHITE or piece.king:
           directions.append((-1, -1))
           directions.append((-1, 1))
        if piece.color == BLACK or piece.king:
           directions.append((1, -1))
           directions.append((1, 1))

        for direction in directions:
        #traverse in each direction to find valid moves
           temp_moves = self._traverse_diagonal(row + direction[0], row + 3 * direction[0], direction[0], piece.color, piece.col + direction[1], direction[1])
           moves.update(temp_moves)

        return moves

    def _traverse_diagonal(self, start, stop, step, color, col, direction, skipped=[]):
        """Find the position that can be reached diagonally."""
        moves = {}
        eat_piece = []
        for i in range(start, stop, step):
            #if piece over the border, cannot move -> break
            if col < 0 or col >= COLS or i < 0 or i >= ROWS:
                break

            cur_pos = self.board[i][col]
            if cur_pos == 0:
                #if there is no piece to eat and skipped, cannot move -> break
                if skipped and not eat_piece:
                    break
                #if there is a piece to eat, update the moves
                elif skipped:
                    moves[(i, col)] = eat_piece + skipped
                else:
                    moves[(i, col)] = eat_piece
                
                #if there is a piece to eat, continue looking for more moves
                if eat_piece:
                    if step == -1:
                        row = max(i-3, 0)
                    else:
                        row = min(i+3, ROWS)
                    moves.update(self._traverse_diagonal(i+step, row, step, color, col-1, direction, skipped=eat_piece))
                    moves.update(self._traverse_diagonal(i+step, row, step, color, col+1, -direction, skipped=eat_piece))
                break
            #if the piece is the same color, cannot move -> break
            elif cur_pos.color == color:
                break
            else:
                eat_piece = [cur_pos]

            col += direction

        return moves
    
    def has_valid_moves(self, color):
        for i in range(ROWS):
            for j in range(COLS):
                piece = self.board[i][j]
                if piece != 0 and piece.color == color:
                    valid_moves = self.get_valid_moves(piece)
                    if valid_moves:
                        return True
        return False
    
