from src.board.board import Board
from src.point.point import Point
from src.square.square import Square


def test_init():
    width = 10
    height = 22
    b = Board(width, height)
    assert b.width == width
    assert b.height == height
    assert len(b.board_matrix) == width
    for column in b.board_matrix:
        assert len(column) == height
        for value in column:
            assert value == 0
    assert len(b.piece_matrix) == width
    for column in b.piece_matrix:
        assert len(column) == height
        for value in column:
            assert value == 0
    assert b.random_list is not None
    assert b.current_tetromino.name in ["O", "I", "J", "L", "S", "Z", "T"]
    assert len(b.other_tetrominos) == 0


def test_switch_piece():
    b = Board(10, 22)
    for i in range(100):
        last_tetromino_name = b.current_tetromino.name
        b.switch_piece()
        assert len(b.other_tetrominos) == i + 1
        assert b.other_tetrominos[i].name == last_tetromino_name
        if not i + 1 % 7:
            assert b.current_tetromino.name != last_tetromino_name


def test_fill_unfill_board():
    b = Board(10, 22)
    for i in range(10):
        for j in range(22):
            b.fill_matrix(b.board_matrix, Square(Point((i, j))))
            assert b.board_matrix[i][j] == 1
    for i in range(10):
        for j in range(22):
            b.unfill_square(b.board_matrix, Square(Point((i, j))))
            assert b.board_matrix[i][j] == 0


def test_clear_matrix():
    b = Board(10, 22)
    for i in range(10):
        for j in range(22):
            b.fill_square(b.board_matrix, Square(Point((i, j))))
    b.clear_matrix(b.board_matrix)
    for i in range(10):
        for j in range(22):
            assert b.board_matrix[i][j] == 0
