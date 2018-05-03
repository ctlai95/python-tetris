import operator

from src.colors import colors
from src.point.point import Point
from src.tetromino.constants import COLORS
from src.tetromino.tetromino import State, Tetromino


def test_init():
    ids_colors = {
        "O": colors.YELLOW,
        "I": colors.TEAL,
        "J": colors.BLUE,
        "L": colors.ORANGE,
        "S": colors.GREEN,
        "Z": colors.RED,
        "T": colors.PURPLE,
    }
    for id, color in ids_colors.items():
        for i in range(10):
            for j in range(22):
                t = Tetromino(id, Point(i, j), COLORS[id])
                assert t.id == id
                assert t.origin.x == i
                assert t.origin.y == j
                assert t.state == State.ZERO
                assert t.color == color


def test_populate_squares():
    expected_layouts = {
        "O": [(0, 0), (1, 0), (1, 1), (0, 1)],
        "I": [(0, 0), (1, 0), (2, 0), (3, 0)],
        "J": [(0, 0), (0, 1), (1, 0), (2, 0)],
        "L": [(0, 0), (1, 0), (2, 0), (2, 1)],
        "S": [(0, 0), (1, 0), (1, 1), (2, 1)],
        "Z": [(0, 1), (1, 1), (1, 0), (2, 0)],
        "T": [(0, 0), (1, 0), (2, 0), (1, 1)]
    }
    for id, layout in expected_layouts.items():
        for i in range(10):
            for j in range(22):
                t = Tetromino(id, Point(i, j), COLORS[id])
                squares_tuples = get_list_tuples(t.squares)
                layout_offset = []
                for l in layout:
                    layout_offset.append(tuple(map(operator.add, l, (i, j))))
                assert sorted(squares_tuples) == sorted(layout_offset)


def test_offset():
    offsets = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]
    ids = ["O", "I", "J", "L", "S", "Z", "T"]
    for id in ids:
        for offset in offsets:
            for i in range(10):
                for j in range(22):
                    t = Tetromino(id, Point(i, j), COLORS[id])
                    t.offset(offset[0], offset[1])
                    assert t.origin.x == i + offset[0]
                    assert t.origin.y == j + offset[1]


expected_new_layouts = {
    "O": [[(+0, +0), (+1, +0), (+1, +1), (+0, +1)],   # initial layout
          [(+0, +0), (+1, +0), (+1, +1), (+0, +1)],   # 1 cw rotation
          [(+0, +0), (+1, +0), (+1, +1), (+0, +1)],   # 2 cw rotations
          [(+0, +0), (+1, +0), (+1, +1), (+0, +1)],   # 3 cw rotations
          [(+0, +0), (+1, +0), (+1, +1), (+0, +1)]],  # initial layout
    "I": [[(+0, +0), (+1, +0), (+2, +0), (+3, +0)],
          [(+2, +0), (+2, +1), (+2, -1), (+2, -2)],
          [(+0, -1), (+1, -1), (+2, -1), (+3, -1)],
          [(+1, -2), (+1, -1), (+1, +0), (+1, +1)],
          [(+0, +0), (+1, +0), (+2, +0), (+3, +0)]],
    "J": [[(+0, +0), (+1, +0), (+2, +0), (+0, +1)],
          [(+1, -1), (+1, +0), (+1, +1), (+2, +1)],
          [(+0, +0), (+1, +0), (+2, +0), (+2, -1)],
          [(+0, -1), (+1, -1), (+1, +0), (+1, +1)],
          [(+0, +0), (+1, +0), (+2, +0), (+0, +1)]],
    "L": [[(+0, +0), (+1, +0), (+2, +0), (+2, +1)],
          [(+1, -1), (+1, +0), (+1, +1), (+2, -1)],
          [(+0, +0), (+1, +0), (+2, +0), (+0, -1)],
          [(+0, +1), (+1, -1), (+1, +0), (+1, +1)],
          [(+0, +0), (+1, +0), (+2, +0), (+2, +1)]],
    "S": [[(+0, +0), (+1, +0), (+1, +1), (+2, +1)],
          [(+2, +0), (+1, +0), (+1, +1), (+2, -1)],
          [(+1, -1), (+1, +0), (+2, +0), (+0, -1)],
          [(+0, +1), (+1, -1), (+1, +0), (+0, +0)],
          [(+0, +0), (+1, +0), (+1, +1), (+2, +1)]],
    "Z": [[(+0, +1), (+1, +0), (+1, +1), (+2, +0)],
          [(+2, +0), (+1, -1), (+1, +0), (+2, +1)],
          [(+1, -1), (+1, +0), (+0, +0), (+2, -1)],
          [(+0, -1), (+1, +1), (+1, +0), (+0, +0)],
          [(+0, +1), (+1, +0), (+1, +1), (+2, +0)]],
    "T": [[(+0, +0), (+1, +0), (+2, +0), (+1, +1)],
          [(+1, +1), (+1, -1), (+1, +0), (+2, +0)],
          [(+0, +0), (+1, +0), (+2, +0), (+1, -1)],
          [(+0, +0), (+1, +0), (+1, +1), (+1, -1)],
          [(+0, +0), (+1, +0), (+2, +0), (+1, +1)]],
}


def test_rotate_cw():
    for id, layouts in expected_new_layouts.items():
        for i in range(10):
            for j in range(22):
                t = Tetromino(id, Point(i, j), COLORS[id])
                old_position = t.origin
                for num_rotations, layout in enumerate(layouts):
                    assert t.origin.x == old_position.x
                    assert t.origin.y == old_position.y
                    squares_tuples = get_list_tuples(t.squares)
                    layout_offset = []
                    for l in layout:
                        layout_offset.append(
                            tuple(map(operator.add, l, (i, j))))
                    assert sorted(squares_tuples) == sorted(layout_offset)
                    assert t.state == State(num_rotations % 4)
                    t.rotate_cw()


def test_rotate_ccw():
    for id, layouts in expected_new_layouts.items():
        for i in range(10):
            for j in range(22):
                t = Tetromino(id, Point(i, j), COLORS[id])
                old_position = t.origin
                for num_rotations, layout in enumerate(reversed(layouts)):
                    assert t.origin.x == old_position.x
                    assert t.origin.y == old_position.y
                    squares_tuples = get_list_tuples(t.squares)
                    layout_offset = []
                    for l in layout:
                        layout_offset.append(
                            tuple(map(operator.add, l, (i, j))))
                    assert sorted(squares_tuples) == sorted(layout_offset)
                    assert t.state == State((4 - num_rotations) % 4)
                    t.rotate_ccw()


def get_list_tuples(tetromino_squares):
    result = []
    for square in tetromino_squares:
        result.append((square.x, square.y))
    return result
