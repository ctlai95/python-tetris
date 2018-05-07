"""Tetromino constants definition."""
from src.colors import colors

# Each tetromino's square's position relative to the bottomleft corner
LAYOUTS = {
    'O': [(0, 0), (1, 0), (1, 1), (0, 1)],
    'I': [(0, 0), (1, 0), (2, 0), (3, 0)],
    'J': [(0, 0), (1, 0), (2, 0), (0, 1)],
    'L': [(0, 0), (1, 0), (2, 0), (2, 1)],
    'S': [(0, 0), (1, 0), (1, 1), (2, 1)],
    'Z': [(1, 0), (1, 1), (0, 1), (2, 0)],
    'T': [(0, 0), (1, 0), (1, 1), (2, 0)]
}

# Each tetromino's spawn location on the board
SPAWN = {
    'O': (4, 20),
    'I': (3, 20),
    'J': (3, 20),
    'L': (3, 20),
    'S': (3, 20),
    'Z': (3, 20),
    'T': (3, 20)
}

# Each tetromino's point of rotation relative to its origin
ROTATION_POINTS = {
    'O': (1, 1),
    'I': (2, 0),
    'J': (1.5, 0.5),
    'L': (1.5, 0.5),
    'S': (1.5, 0.5),
    'Z': (1.5, 0.5),
    'T': (1.5, 0.5)
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
