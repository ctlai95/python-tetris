import pyglet
import random

UNIT = 40
PIECES = {
    'O_PIECE': [(4, 20), (5, 20), (4, 21), (5, 21)],
    'I_PIECE': [(3, 20), (4, 20), (5, 20), (6, 20)],
    'J_PIECE': [(3, 21), (3, 20), (4, 20), (5, 20)],
    'L_PIECE': [(3, 20), (4, 20), (5, 20), (5, 21)],
    'S_PIECE': [(3, 20), (4, 20), (4, 21), (5, 21)],
    'Z_PIECE': [(3, 21), (4, 21), (4, 20), (5, 20)],
    'T_PIECE': [(3, 20), (4, 20), (5, 20), (4, 21)]
}

PIECE_ORIGINS = {
    'O_PIECE': (5, 21),
    'I_PIECE': (5, 20),
    'J_PIECE': (4.5, 20.5),
    'L_PIECE': (4.5, 20.5),
    'S_PIECE': (4.5, 20.5),
    'Z_PIECE': (4.5, 20.5),
    'T_PIECE': (4.5, 20.5)
}


class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.map = Map(int(self.width/UNIT),
                       int(self.height/UNIT))

    def on_draw(self):
        self.clear()
        self.map.render()

    def on_text_motion(self, motion):
        self.map.move(motion)

    def on_key_press(self, symbol, modifier):
        if symbol == pyglet.window.key.SPACE:
            self.map.hard_drop()
        elif symbol == pyglet.window.key.MOTION_UP:
            self.map.rotate_cw()
        elif symbol == pyglet.window.key.Z:
            self.map.rotate_ccw()


class Piece:
    def __init__(self, coords, origin):
        self.coords = []
        for c in coords:
            self.coords.append(tuple(x for x in c))
        self.origin = origin

    def opengl_coords(self, x, y):
        x *= UNIT
        y *= UNIT
        return (x, y, x + UNIT, y,
                x + UNIT, y + UNIT,
                x, y + UNIT)

    def move_left(self):
        for i in range(len(self.coords)):
            self.coords[i] = (self.coords[i][0] - 1,
                              self.coords[i][1])
        self.origin = (self.origin[0] - 1, self.origin[1])

    def move_right(self):
        for i in range(len(self.coords)):
            self.coords[i] = (self.coords[i][0] + 1,
                              self.coords[i][1])
        self.origin = (self.origin[0] + 1, self.origin[1])

    def move_down(self, distance):
        for i in range(len(self.coords)):
            self.coords[i] = (self.coords[i][0],
                              self.coords[i][1] - distance)
        self.origin = (self.origin[0], self.origin[1] - distance)

    def clockwise_rotation(self):
        for i in range(len(self.coords)):
            normalized_point = tuple(x - y for x, y in zip(self.coords[i],
                                                           self.origin))
            btm_right = tuple(sum(t) for t in zip(normalized_point, (1, 0)))
            new_point = tuple(sum(t) for t in zip(self.origin,
                              (btm_right[1], -btm_right[0])))
            self.coords[i] = (int(new_point[0]), int(new_point[1]))

    def counter_clockwise_rotation(self):
        for i in range(len(self.coords)):
            normalized_point = tuple(x - y for x, y in zip(self.coords[i],
                                                           self.origin))
            top_left = tuple(sum(t) for t in zip(normalized_point, (0, 1)))
            new_point = tuple(sum(t) for t in zip(self.origin,
                              (-top_left[1], top_left[0])))
            self.coords[i] = (int(new_point[0]), int(new_point[1]))


class Map:
    def __init__(self, width, height):
        random_key = random.choice(list(PIECES.keys()))
        self.piece = Piece(PIECES[random_key], PIECE_ORIGINS[random_key])
        self.matrix = [[0 for y in range(height)] for x in range(width)]

    def fillPiece(self):
        for x, y in self.piece.coords:
            self.matrix[x][y] = 1

    def unfillPiece(self):
        for x, y in self.piece.coords:
            self.matrix[x][y] = 0

    def render(self):
        self.fillPiece()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 1:
                    #  print(self.piece.opengl_coords(i, j))
                    pyglet.graphics.draw_indexed(
                        4, pyglet.gl.GL_TRIANGLES,
                        [0, 1, 2, 0, 2, 3],
                        ('v2i', self.piece.opengl_coords(i, j)))

    def rotate_cw(self):
        self.unfillPiece()
        self.piece.clockwise_rotation()
        # TODO: Kicks and boundaries

    def rotate_ccw(self):
        self.unfillPiece()
        self.piece.counter_clockwise_rotation()
        # TODO: Kicks and boundaries

    def move(self, direction):
        if direction == pyglet.window.key.MOTION_LEFT:
            self.unfillPiece()
            moveable = True

            for x, y in self.piece.coords:
                if (x <= 0 or self.matrix[x - 1][y] == 1):
                    moveable = False

            if moveable:
                self.piece.move_left()

        elif direction == pyglet.window.key.MOTION_RIGHT:
            self.unfillPiece()
            moveable = True

            for x, y in self.piece.coords:
                if (x >= len(self.matrix) - 1 or
                        self.matrix[x + 1][y] == 1):
                    moveable = False
                    break

            if moveable:
                self.piece.move_right()

        elif direction == pyglet.window.key.MOTION_DOWN:
            self.unfillPiece()
            moveable = True

            for x, y in self.piece.coords:
                if (y <= 0 or self.matrix[x][y - 1] == 1):
                    moveable = False
                    break

            if moveable:
                self.piece.move_down(1)
            else:
                self.switch_piece()

    def switch_piece(self):
        self.fillPiece()
        random_key = random.choice(list(PIECES.keys()))
        self.piece = Piece(PIECES[random_key], PIECE_ORIGINS[random_key])

    def hard_drop(self):
        self.unfillPiece()
        height = len(self.matrix[0])

        # Find the lowest point of the piece
        for c in self.piece.coords:
            if c[1] < height:
                height = c[1]

        # Get columns that are the lowest point
        columns = []
        for x, y in self.piece.coords:
            if height == y:
                columns.append(x)

        # Get the highest point on the map based on those columns
        map_height = 0
        for x in columns:
            for y in reversed(range(len(self.matrix[x]))):
                if self.matrix[x][y] == 1:
                    if y > map_height:
                        map_height = y

        if map_height != 0:
            if map_height < height:
                height = height - map_height - 1

        self.piece.move_down(height)
        self.switch_piece()

    # Used for debugging purposes
    def print_map(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 1:
                    print("1: ", i, j)


if __name__ == '__main__':
    window = Window(400, 880,
                    "Python Tetris", resizable=True)
    pyglet.app.run()
