import pyglet
import random
import config
import piece


class Map:
    def __init__(self, width, height):
        random_key = random.choice(list(config.PIECES.keys()))
        self.piece = piece.Piece(config.PIECES[random_key],
                                 config.PIECE_ORIGINS[random_key])
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

        for x, y in self.piece.coords:
            if (y <= 0 or self.matrix[x][y - 1] == 1):
                self.piece.move_up()
            elif (x >= len(self.matrix) - 1 or self.matrix[x + 1][y] == 1):
                self.piece.move_left()
            elif (x < 0 or self.matrix[x - 1][y] == 1):
                self.piece.move_right()

    def rotate_ccw(self):
        self.unfillPiece()
        self.piece.counter_clockwise_rotation()

        for x, y in self.piece.coords:
            if (y <= 0 or self.matrix[x][y - 1] == 1):
                self.piece.move_up()
            elif (x >= len(self.matrix) - 1 or self.matrix[x + 1][y] == 1):
                self.piece.move_left()
            elif (x < 0 or self.matrix[x - 1][y] == 1):
                self.piece.move_right()

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
        random_key = random.choice(list(config.PIECES.keys()))
        self.piece = piece.Piece(config.PIECES[random_key],
                                 config.PIECE_ORIGINS[random_key])

    def hard_drop(self):
        self.unfillPiece()

        piece_heights = []
        for x, y in self.piece.coords:
            piece_heights.append(y)

        map_heights = []
        for x, _ in self.piece.coords:
            for y in reversed(range(len(self.matrix[x]) - 1)):
                if self.matrix[x][y] == 1:
                    map_heights.append(y + 1)
                    break
                if y == 0:
                    map_heights.append(0)

        differences = [y1 - y2 for y1, y2 in zip(piece_heights, map_heights)]

        lowest_difference = len(self.matrix[0]) - 1
        for diff in differences:
            if diff < lowest_difference:
                lowest_difference = diff

        self.piece.move_down(lowest_difference)
        self.switch_piece()

    def gravity(self):
        self.unfillPiece()
        self.move(pyglet.window.key.MOTION_DOWN)

    # Used for debugging purposes
    def print_map(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 1:
                    print("1: ", i, j)
