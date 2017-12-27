from src.map.map import Map
from src.point.point import Point
from src.square.square import Square


def test_init():
    width = 10
    height = 22
    m = Map(width, height)
    assert m.width == width
    assert m.height == height
    assert len(m.map_matrix) == width
    for column in m.map_matrix:
        assert len(column) == height
        for value in column:
            assert value == 0
    assert len(m.piece_matrix) == width
    for column in m.piece_matrix:
        assert len(column) == height
        for value in column:
            assert value == 0
    assert m.random_list is not None
    assert m.current_tetromino.name in ["O", "I", "J", "L", "S", "Z", "T"]
    assert len(m.other_tetrominos) == 0


def test_switch_piece():
    m = Map(10, 22)
    for i in range(100):
        last_tetromino_name = m.current_tetromino.name
        m.switch_piece()
        assert len(m.other_tetrominos) == i + 1
        assert m.other_tetrominos[i].name == last_tetromino_name
        if not i + 1 % 7:
            assert m.current_tetromino.name != last_tetromino_name


def test_fill_unfill_matrix():
    m = Map(10, 22)
    for i in range(10):
        for j in range(22):
            m.fill_matrix(m.map_matrix, Square(Point((i, j))))
            assert m.map_matrix[i][j] == 1
    for i in range(10):
        for j in range(22):
            m.unfill_matrix(m.map_matrix, Square(Point((i, j))))
            assert m.map_matrix[i][j] == 0


def test_clear_matrix():
    m = Map(10, 22)
    for i in range(10):
        for j in range(22):
            m.fill_matrix(m.map_matrix, Square(Point((i, j))))
    m.clear_matrix(m.map_matrix)
    for i in range(10):
        for j in range(22):
            assert m.map_matrix[i][j] == 0
