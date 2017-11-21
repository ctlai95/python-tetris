UNIT = 40  # Length of a square in pixels
GRAVITY_INTERVAL = 1

# Each tetromino's square's position relative to the bottomleft piece
LAYOUTS = {
    'O': [[0, 0], [1, 0], [1, 1], [0, 1]],
    'I': [[0, 0], [1, 0], [2, 0], [3, 0]],
    'J': [[0, 0], [1, 0], [2, 0], [0, 1]],
    'L': [[0, 0], [1, 0], [2, 0], [2, 1]],
    'S': [[0, 0], [1, 0], [1, 1], [2, 1]],
    'Z': [[1, 0], [1, 1], [0, 1], [2, 0]],
    'T': [[0, 0], [1, 0], [1, 1], [2, 0]]
}

# Each tetromino's spawn location on the map
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

ROTATIONAL_KICKS = {

}

# Color values in RGB
COLORS = {
    'O': [244, 197, 36],
    'T': [227, 72, 182],
    'S': [124, 227, 22],
    'I': [70, 194, 255],
    'J': [54, 99, 246],
    'Z': [245, 61, 102],
    'L': [237, 130, 33],

    'GHOST': [100, 100, 100],

    'BG_DARK': [40, 40, 40],
    'BG_LIGHT': [50, 50, 50]
}
