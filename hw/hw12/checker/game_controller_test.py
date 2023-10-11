import pytest
from game_controller import GameController, WHITE, BLACK

def test_game_controller_init():
    gc = GameController()
    assert gc.turn == WHITE
    assert gc.selected is None
    assert gc.vaild_moves == {}

def test_game_controller_reset():
    gc = GameController()
    gc.select(0, 0)
    gc.reset()
    assert gc.turn == WHITE
    assert gc.selected is None
    assert gc.vaild_moves == {}

def test_select_invalid_piece():
    gc = GameController()
    gc.select(1, 0)
    assert gc.select(2, 0) == False

def test_move_invalid_piece():
    gc = GameController()
    assert gc._move(1, 0) == False

