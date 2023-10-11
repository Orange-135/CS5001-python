import pytest
from piece import Piece, WHITE

def test_piece_init():
    piece = Piece(4, 5, WHITE)
    assert piece.row == 4
    assert piece.col == 5
    assert piece.color == WHITE
    assert piece.king == False

def test_piece_make_king():
    piece = Piece(2, 3, WHITE)
    piece.make_king()
    assert piece.king == True

def test_piece_move():
    piece = Piece(2, 3, WHITE)
    piece.move(5, 6)
    assert piece.row == 5
    assert piece.col == 6