import pyglet
import random
import config
import piece
from pyglet.gl import *


class Map:
    def __init__(self, width, height):
        random_key = random.choice(list(config.PIECES.keys()))
        self.piece = piece.Piece(config.PIECES[random_key],
                                 config.PIECE_ORIGINS[random_key],
                                 config.PIECE_COLOR[random_key])
        self.matrix = [[0 for y in range(height)] for x in range(width)]

    def opengl_coords(self, x, y):
        x *= config.UNIT
        y *= config.UNIT
        return (x, y,
                x + config.UNIT, y,
                x + config.UNIT, y + config.UNIT,
                x, y + config.UNIT)

    def fillPiece(self):
        for x, y in self.piece.coords:
            self.matrix[x][y] = self.piece.color

    def unfillPiece(self):
        for x, y in self.piece.coords:
            self.matrix[x][y] = 0

    def render(self):
        self.render_grid()
        self.fillPiece()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] != 0:
                    vertex_list = pyglet.graphics.vertex_list(4, 'v2i', 'c3B')
                    vertex_list.vertices = self.opengl_coords(i, j)

                    vertex_list.colors = [self.matrix[i][j][0],
                                          self.matrix[i][j][1],
                                          self.matrix[i][j][2]]*4
                    vertex_list.draw(GL_TRIANGLE_FAN)
                    shade = [int(c * 0.8) for c in self.matrix[i][j]]
                    vertex_list.colors = [shade[0], shade[1], shade[2]]*4
                    pyglet.gl.glLineWidth(2)
                    vertex_list.draw(GL_LINE_LOOP)

    def render_grid(self):
        vertex_list = pyglet.graphics.vertex_list(4, 'v2i', 'c3B')
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                vertex_list.vertices = self.opengl_coords(i, j)

                if (i % 2 is 0 and j % 2 is 0) or \
                   ((i+1) % 2 is 0 and (j+1) % 2 is 0):
                    vertex_list.colors = [40, 40, 40,
                                          40, 40, 40,
                                          40, 40, 40,
                                          40, 40, 40]
                else:
                    vertex_list.colors = [50, 50, 50,
                                          50, 50, 50,
                                          50, 50, 50,
                                          50, 50, 50]
                vertex_list.draw(pyglet.gl.GL_TRIANGLE_FAN)

    def rotate_cw(self):
        self.unfillPiece()
        self.piece.clockwise_rotation()

        for x, y in self.piece.coords:
            if (y <= 0 or self.matrix[x][y - 1] != 0):
                self.piece.move_up()
            elif (x >= len(self.matrix) - 1 or self.matrix[x + 1][y] != 0):
                self.piece.move_left()
            elif (x < 0 or self.matrix[x - 1][y] != 0):
                self.piece.move_right()

    def rotate_ccw(self):
        self.unfillPiece()
        self.piece.counter_clockwise_rotation()

        for x, y in self.piece.coords:
            if (y <= 0 or self.matrix[x][y - 1] != 0):
                self.piece.move_up()
            elif (x >= len(self.matrix) - 1 or self.matrix[x + 1][y] != 0):
                self.piece.move_left()
            elif (x < 0 or self.matrix[x - 1][y] != 0):
                self.piece.move_right()

    def move(self, direction):
        if direction == pyglet.window.key.MOTION_LEFT:
            self.unfillPiece()
            moveable = True

            for x, y in self.piece.coords:
                if (x <= 0 or self.matrix[x - 1][y] != 0):
                    moveable = False

            if moveable:
                self.piece.move_left()

        elif direction == pyglet.window.key.MOTION_RIGHT:
            self.unfillPiece()
            moveable = True

            for x, y in self.piece.coords:
                if (x >= len(self.matrix) - 1 or
                        self.matrix[x + 1][y] != 0):
                    moveable = False
                    break

            if moveable:
                self.piece.move_right()

        elif direction == pyglet.window.key.MOTION_DOWN:
            self.unfillPiece()
            moveable = True

            for x, y in self.piece.coords:
                if (y <= 0 or self.matrix[x][y - 1] != 0):
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
                                 config.PIECE_ORIGINS[random_key],
                                 config.PIECE_COLOR[random_key])

    def hard_drop(self):
        self.unfillPiece()

        piece_heights = []
        for x, y in self.piece.coords:
            piece_heights.append(y)

        map_heights = []
        for x, _ in self.piece.coords:
            for y in reversed(range(len(self.matrix[x]) - 1)):
                if self.matrix[x][y] != 0:
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
        for i in reversed(range(len(self.matrix[0]))):
            for j in range(len(self.matrix)):
                if self.matrix[j][i] == 1:
                    print(1, end=" ")
                else:
                    print(0, end=" ")
            print()
        print()
