from src import config
from src.point.point import Point
from src.square.square import Square
from src.tetromino.tetromino import Tetromino
from src.utils.tuples import tuples


def test_init():
    names = ["O", "I", "J", "L", "S", "Z", "T"]
    for name in names:
        for i in range(10):
            for j in range(22):
                t = Tetromino(name, Point((i, j)), config.COLORS[name])
                assert t.name == name
                assert t.loc._xy() == (i, j)
                assert t.state == 0
                assert t.color == config.COLORS[name]


def test_populate_sqrs():
    expected_layouts = {
        "O": [(0, 0), (1, 0), (1, 1), (0, 1)],
        "I": [(0, 0), (1, 0), (2, 0), (3, 0)],
        "J": [(0, 0), (0, 1), (1, 0), (2, 0)],
        "L": [(0, 0), (1, 0), (2, 0), (2, 1)],
        "S": [(0, 0), (1, 0), (1, 1), (2, 1)],
        "Z": [(0, 1), (1, 1), (1, 0), (2, 0)],
        "T": [(0, 0), (1, 0), (2, 0), (1, 1)]
    }
    for name, layout in expected_layouts.items():
        for i in range(10):
            for j in range(22):
                t = Tetromino(name, Point((i, j)), config.COLORS[name])
                squares_tuples = get_list_tuples(t.sqrs)
                layout_offset = []
                for l in layout:
                    layout_offset.append(tuples.add(l, (i, j)))
                assert sorted(squares_tuples) == sorted(layout_offset)


def test_offset():
    offsets = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]
    names = ["O", "I", "J", "L", "S", "Z", "T"]
    for name in names:
        for offset in offsets:
            for i in range(10):
                for j in range(22):
                    t = Tetromino(name, Point((i, j)), config.COLORS[name])
                    t.offset(offset[0], offset[1])
                    assert t.loc._xy() == tuples.add(
                        (i, j), (offset[0], offset[1]))


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
    for name, layouts in expected_new_layouts.items():
        for i in range(10):
            for j in range(22):
                t = Tetromino(name, Point((i, j)), config.COLORS[name])
                old_position = t.loc
                for layout in layouts:
                    assert t.loc._xy() == old_position._xy()
                    squares_tuples = get_list_tuples(t.sqrs)
                    layout_offset = []
                    for l in layout:
                        layout_offset.append(tuples.add(l, (i, j)))
                    assert sorted(squares_tuples) == sorted(layout_offset)
                    t.rotate_cw()


def test_rotate_ccw():
    for name, layouts in expected_new_layouts.items():
        for i in range(10):
            for j in range(22):
                t = Tetromino(name, Point((i, j)), config.COLORS[name])
                old_position = t.loc
                for layout in reversed(layouts):
                    assert t.loc._xy() == old_position._xy()
                    squares_tuples = get_list_tuples(t.sqrs)
                    layout_offset = []
                    for l in layout:
                        layout_offset.append(tuples.add(l, (i, j)))
                    assert sorted(squares_tuples) == sorted(layout_offset)
                    t.rotate_ccw()


def get_list_tuples(tetromino_squares):
    result = []
    for s in tetromino_squares:
        result.append(s.tuple())
    return result
