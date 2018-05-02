from src.board.board import Board
from src.movement.movement import Movement
from src.point.point import Point
from src.square.square import Square
from src.colors import colors


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
    assert b.random_tetrominos is not None
    assert b.current_tetromino.id in ["O", "I", "J", "L", "S", "Z", "T"]
    assert len(b.board_tetrominos_squares) == 0


def test_switch_current_tetromino():
    b = Board(10, 22)
    for i in range(100):
        last_tetromino_id = b.current_tetromino.id
        b.switch_current_tetromino()
        if not i + 1 % 7:
            assert b.current_tetromino.id != last_tetromino_id


def test_fill_unfill_matrix():
    b = Board(10, 22)
    for i in range(10):
        for j in range(22):
            b.fill_matrix(b.board_tetrominos_matrix,
                          Square(Point((i, j)), colors.ASH))
            assert b.board_tetrominos_matrix[i][j] == 1
    for i in range(10):
        for j in range(22):
            b.unfill_matrix(b.board_tetrominos_matrix,
                            Square(Point((i, j)), colors.ASH))
            assert b.board_tetrominos_matrix[i][j] == 0


def test_get_filled_indices_should_be_zero():
    b = Board(10, 22)
    assert not b.get_filled_indices()


def test_get_filled_indices_should_be_seven():
    b = Board(10, 22)
    filled_indices = [0, 1, 2, 3, 4, 5, 6]
    for i in range(10):
        for j in range(7):
            b.fill_matrix(b.board_tetrominos_matrix,
                          Square(Point((i, j)), colors.ASH))
    assert b.get_filled_indices() == filled_indices


def test_clear_lines():
    b = Board(10, 22)
    # Set up lines that should be cleared
    for i in range(10):
        b.fill_matrix(b.board_tetrominos_matrix,
                      Square(Point((i, 3)), colors.ASH))
        b.fill_matrix(b.board_tetrominos_matrix,
                      Square(Point((i, 8)), colors.ASH))

    filled_indices = [3, 8]
    b.clear_lines(filled_indices)
    lines_cleared = True
    b.update_matrices()

    for i in range(10):
        if (b.board_tetrominos_matrix[i][3] == 1 or
                b.board_tetrominos_matrix[i][8] == 1):
            lines_cleared = False
    assert lines_cleared


def test_clear_matrix():
    b = Board(10, 22)
    for i in range(10):
        for j in range(22):
            b.fill_matrix(b.board_tetrominos_matrix,
                          Square(Point((i, j)), colors.ASH))
    b.clear_matrix(b.board_tetrominos_matrix)
    for i in range(10):
        for j in range(22):
            assert b.board_tetrominos_matrix[i][j] == 0


def test_hold_current_tetromino():
    b = Board(10, 22)
    m = Movement(b)
    assert b.held_tetromino is None
    last_tetromino_id = b.current_tetromino.id
    # should hold current tetromino
    b.hold_current_tetromino()
    assert b.held_tetromino.id == last_tetromino_id
    # not dropped yet, so held tetromino should be unchanged
    b.hold_current_tetromino()
    assert b.held_tetromino.id == last_tetromino_id
    # drop tetromino then hold, held tetromino should replace current
    m.hard_drop()
    b.hold_current_tetromino()
    assert b.held_tetromino.id != last_tetromino_id
    assert b.current_tetromino.id == last_tetromino_id
