import pytest
from board import Board, Piece, BLACK

#There ia something wrong about pytest(name 'color' is not defined), I don't know how to deal with it
#I asked ChatGPT about this, it gives me the solution like that:
#  try:
#     from processing import color
#     WHITE = color(255, 255, 255)
#     BLACK = color(0, 0, 0)
# except ImportError:
#     WHITE = (255, 255, 255)
#     BLACK = (0, 0, 0)
#after I revised, the pytest can run, but the checker.pyde could not run.

def test_board_init():
    board = Board()
    assert len(board.board) == 8
    assert board.white_left == board.black_left == 12
    assert board.white_kings == board.black_kings == 0

def test_get_pos():
    board = Board()
    piece = board.get_pos(0, 1)
    assert isinstance(piece, Piece)
    assert piece.color == BLACK

def test_remove():
    board = Board()
    piece = board.get_pos(0, 1)
    board.remove([piece])
    assert board.get_pos(0, 1) == 0
    assert board.black_left == 11
