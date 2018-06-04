"""Tetromino constants definition."""
from src.colors import colors
from src.point.point import Point

# Each tetromino's square's position relative to the bottomleft corner
LAYOUTS = {
    'O': [Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1)],
    'I': [Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0)],
    'J': [Point(0, 0), Point(1, 0), Point(2, 0), Point(0, 1)],
    'L': [Point(0, 0), Point(1, 0), Point(2, 0), Point(2, 1)],
    'S': [Point(0, 0), Point(1, 0), Point(1, 1), Point(2, 1)],
    'Z': [Point(1, 0), Point(1, 1), Point(0, 1), Point(2, 0)],
    'T': [Point(0, 0), Point(1, 0), Point(1, 1), Point(2, 0)]
}

# Each tetromino's spawn location on the board
SPAWN = {
    'O': Point(4, 20),
    'I': Point(3, 20),
    'J': Point(3, 20),
    'L': Point(3, 20),
    'S': Point(3, 20),
    'Z': Point(3, 20),
    'T': Point(3, 20)
}

# Each tetromino's point of rotation relative to its origin
ROTATION_POINTS = {
    'O': Point(1.0, 1.0),
    'I': Point(2.0, 0.0),
    'J': Point(1.5, 0.5),
    'L': Point(1.5, 0.5),
    'S': Point(1.5, 0.5),
    'Z': Point(1.5, 0.5),
    'T': Point(1.5, 0.5)
}

# Wall kicks are based on the Super Rotation System (SRS)
# http://tetris.wikia.com/wiki/SRS
WALL_KICKS_CW = {
    # index position corresponds to initial rotation state
    ('J', 'L', 'S', 'T', 'Z'): [
        [(0, 0), (-1, 0), (-1, +1), (0, -2), (-1, -2)],
        [(0, 0), (+1, 0), (+1, -1), (0, +2), (+1, +2)],
        [(0, 0), (+1, 0), (+1, +1), (0, -2), (+1, -2)],
        [(0, 0), (-1, 0), (-1, -1), (0, +2), (-1, +2)]
    ],
    ('I'): [
        [(0, 0), (-2, 0), (+1, 0), (-2, -1), (+1, +2)],
        [(0, 0), (-1, 0), (+2, 0), (-1, +2), (+2, -1)],
        [(0, 0), (+2, 0), (-1, 0), (+2, +1), (-1, -2)],
        [(0, 0), (+1, 0), (-2, 0), (+1, -2), (-2, +1)]
    ]
}

WALL_KICKS_CCW = {
    ('J', 'L', 'S', 'T', 'Z'): [
        [(0, 0), (+1, 0), (+1, +1), (0, -2), (+1, -2)],
        [(0, 0), (+1, 0), (+1, -1), (0, +2), (+1, +2)],
        [(0, 0), (-1, 0), (-1, +1), (0, -2), (-1, -2)],
        [(0, 0), (-1, 0), (-1, -1), (0, +2), (-1, +2)]
    ],
    ('I'): [
        [(0, 0), (-1, 0), (+2, 0), (-1, +2), (+2, -1)],
        [(0, 0), (+2, 0), (-1, 0), (+2, +1), (-1, -2)],
        [(0, 0), (+1, 0), (-2, 0), (+1, -2), (-2, +1)],
        [(0, 0), (-2, 0), (+1, 0), (-2, -1), (+1, +2)]
    ]
}

# Color values in RGB
COLORS = {
    'O': colors.YELLOW,
    'I': colors.TEAL,
    'J': colors.BLUE,
    'L': colors.ORANGE,
    'S': colors.GREEN,
    'Z': colors.RED,
    'T': colors.PURPLE,
}
