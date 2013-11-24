from models.board import *
from models.ball import Ball

import pytest

class TestBoard():
  def setup_method(self, method):
    self.board = Board()

  def test_it_setups(self):
    assert self.board.field(3, 3) == Ball(Ball.RED)
    assert self.board.field(3, 4) == Ball(Ball.YELLOW)
    assert self.board.field(4, 3) == Ball(Ball.BLUE)
    assert self.board.field(4, 4) == Ball(Ball.GREEN)

  def test_it_places_fields_vertically(self):
    assert self.board.field(3, 2) == Ball(Ball.EMPTY)
    with pytest.raises(ForcedMoveError):
      self.board.place(3, 2, Ball.RED)

    self.board.place(3, 2, Ball.YELLOW)
    assert self.board.field(3, 2) == Ball(Ball.YELLOW)
    assert self.board.field(3, 3) == Ball(Ball.YELLOW)

  def test_it_places_fields_horizontally(self):
    assert self.board.field(5, 4) == Ball(Ball.EMPTY)
    with pytest.raises(ForcedMoveError):
      self.board.place(5, 4, Ball.RED)

    self.board.place(5, 4, Ball.YELLOW)
    assert self.board.field(5, 4) == Ball(Ball.YELLOW)
    assert self.board.field(4, 4) == Ball(Ball.YELLOW)
  
  def test_it_places_fields_diagonally_up(self):
    assert self.board.field(5, 2) == Ball(Ball.EMPTY)
    with pytest.raises(ForcedMoveError):
      self.board.place(5, 2, Ball.RED)

    self.board.place(5, 2, Ball.YELLOW)
    assert self.board.field(5, 2) == Ball(Ball.YELLOW)
    assert self.board.field(4, 3) == Ball(Ball.YELLOW)

    with pytest.raises(ForcedMoveError):
      self.board.place(2, 5, Ball.YELLOW)

  def test_it_places_fields_diagonally_down(self):
    assert self.board.field(5, 5) == Ball(Ball.EMPTY)
    with pytest.raises(ForcedMoveError):
      self.board.place(5, 5, Ball.YELLOW)
    
    self.board.place(5, 5, Ball.RED)
    assert self.board.field(5, 5) == Ball(Ball.RED)
    assert self.board.field(4, 4) == Ball(Ball.RED)

    with pytest.raises(ForcedMoveError):
      self.board.place(2, 2, Ball.RED)

  def test_it_takes_no_double_placements(self):
    self.board.place(3, 2, Ball.YELLOW)

    with pytest.raises(AlreadyOccupiedError):
      self.board.place(3, 2, Ball.YELLOW)

  def test_it_only_allows_adjacent_placements(self):
    with pytest.raises(NotAdjacentError):
      self.board.place(6, 2, Ball.GREEN)

    self.board.place(5, 3, Ball.RED)
    self.board.place(6, 2, Ball.GREEN)

    assert self.board.field(6, 2) == Ball(Ball.GREEN)
    assert self.board.field(5, 3) == Ball(Ball.GREEN)

  def test_it_allows_any_move_if_blocking_is_not_forced(self):
    with pytest.raises(ForcedMoveError):
      self.board.place(2, 2, Ball.BLUE)

    self.board.place(5, 3, Ball.RED)
    self.board.place(2, 2, Ball.BLUE)
  
  def test_it_gives_the_right_winning_colors(self):
    assert self.board.winning_colors() == [Ball.RED, Ball.YELLOW, Ball.BLUE, Ball.GREEN]

    self.board.place(5, 5, Ball.RED)
    assert self.board.winning_colors() == [Ball.RED]

    print self.board
    self.board.place(5, 23, Ball.YELLOW)
    assert self.board.winning_colors() == [Ball.RED, Ball.YELLOW]
