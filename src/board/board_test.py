from src.board.board import Board
from src.movement.movement import Movement
from src.point.point import Point
from src.square.square import Square


def test_init():
    width = 10
    height = 22
    b = Board(width, height)
    assert b.width == width
    assert b.height == height
    assert len(b.board_tetrominos_matrix) == width
    for column in b.board_tetrominos_matrix:
        assert len(column) == height
        for value in column:
            assert value == 0
    assert len(b.current_tetromino_matrix) == width
    for column in b.current_tetromino_matrix:
        assert len(column) == height
        for value in column:
            assert value == 0
    assert b.random_list is not None
    assert b.current_tetromino.name in ["O", "I", "J", "L", "S", "Z", "T"]
    assert len(b.board_tetrominos) == 0


def test_switch_current_tetromino():
    b = Board(10, 22)
    for i in range(100):
        last_tetromino_name = b.current_tetromino.name
        b.switch_current_tetromino()
        if not i + 1 % 7:
            assert b.current_tetromino.name != last_tetromino_name


def test_fill_unfill_matrix():
    b = Board(10, 22)
    for i in range(10):
        for j in range(22):
            b.fill_matrix(b.board_tetrominos_matrix, Square(Point((i, j))))
            assert b.board_tetrominos_matrix[i][j] == 1
    for i in range(10):
        for j in range(22):
            b.unfill_matrix(b.board_tetrominos_matrix, Square(Point((i, j))))
            assert b.board_tetrominos_matrix[i][j] == 0


def test_clear_matrix():
    b = Board(10, 22)
    for i in range(10):
        for j in range(22):
            b.fill_matrix(b.board_tetrominos_matrix, Square(Point((i, j))))
    b.clear_matrix(b.board_tetrominos_matrix)
    for i in range(10):
        for j in range(22):
            assert b.board_tetrominos_matrix[i][j] == 0


def test_hold_current_tetromino():
    b = Board(10, 22)
    m = Movement(b)
    assert b.held_tetromino == None
    last_tetromino_name = b.current_tetromino.name
    # should hold current tetromino
    b.hold_current_tetromino()
    assert b.held_tetromino.name == last_tetromino_name
    # not dropped yet, so held tetromino should be unchanged
    b.hold_current_tetromino()
    assert b.held_tetromino.name == last_tetromino_name
    # drop piece then hold, held piece should replace current
    m.hard_drop()
    b.hold_current_tetromino()
    assert b.held_tetromino.name != last_tetromino_name
    assert b.current_tetromino.name == last_tetromino_name
