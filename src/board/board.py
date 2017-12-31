from src import config
from src.colors import colors
from src.point.point import Point
from src.randomizer.randomizer import Randomizer
from src.renderer.renderer import Renderer
from src.tetromino.tetromino import Tetromino


class Board:
    """Board contains all the tetrominos in the current game"""

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board_matrix = [[0 for y in range(height)] for x in range(width)]
        self.piece_matrix = [[0 for y in range(height)] for x in range(width)]
        self.random_list = Randomizer()
        next_piece = self.random_list.next()
        self.current_tetromino = Tetromino(
            next_piece,
            Point(config.SPAWN[next_piece]),
            config.COLORS[next_piece]
        )
        self.other_tetrominos = []
        self.holdable = True
        self.held_tetromino = None

    def render_board(self):
        """Renders the board to the screen and updates matrices"""
        self.clear_matrix(self.piece_matrix)
        self.clear_matrix(self.board_matrix)

        # Render the background
        self.render_background()

        # Render pieces except current one
        for t in self.other_tetrominos:
            t.render_tetromino()
            for s in t.sqrs:
                self.fill_matrix(self.board_matrix, s)

        # Render the ghost tetromino
        self.render_ghost()

        # Render current playable tetromino
        self.current_tetromino.render_tetromino()
        for s in self.current_tetromino.sqrs:
            self.fill_matrix(self.piece_matrix, s)

    def switch_piece(self):
        """Assigns a new current piece"""
        next_piece = self.random_list.next()
        self.current_tetromino = Tetromino(
            next_piece,
            Point(config.SPAWN[next_piece]),
            config.COLORS[next_piece]
        )

    def render_ghost(self):
        """Renders the ghost of the current tetromino"""
        ghost = Tetromino(
            self.current_tetromino.name,
            self.current_tetromino.loc,
            colors.ASH
        )
        for i in range(self.current_tetromino.state.value):
            ghost.rotate_cw()
        for i in range(self.height):
            ghost.offset(0, -1)
            for s in ghost.sqrs:
                if s.y < 0 or self.board_matrix[s.x][s.y] == 1:
                    ghost.offset(0, 1)
                    break
        ghost.render_tetromino()

    def fill_matrix(self, matrix, square):
        """Fills the matrix at the given indices with a 1"""
        if square.x >= self.width or square.y >= self.height:
            print(
                "Warning: position exceeds boundaries: " +
                "[{:d}][{:d}]".format(square.x, square.y))
            return
        matrix[square.x][square.y] = 1

    def unfill_matrix(self, matrix, square):
        """Fills the matrix at the given indices with a 0"""
        if square.x >= self.width or square.y >= self.height:
            print(
                "Warning: position exceeds boundaries: " +
                "[{:d}][{:d}]".format(square.x, square.y))
            return
        matrix[square.x][square.y] = 0

    def clear_matrix(self, matrix):
        """Clears the current matrix"""
        for i in range(self.width):
            for j in range(self.height):
                matrix[i][j] = 0

    def render_background(self):
        """Renders the background squares"""
        for i in range(self.width):
            for j in range(self.height):
                if (i % 2 is 0 and j % 2 is 0) or \
                        ((i + 1) % 2 is 0 and (j + 1) % 2 is 0):
                    s = Renderer(i, j, colors.CHARCOAL)
                else:
                    s = Renderer(i, j, colors.JET)
                s.draw()

    def hold_piece(self):
        """Holds the current tetromino and switches to another one"""
        if self.holdable is False:
            return
        self.holdable = False
        if self.held_tetromino is None:
            self.held_tetromino = Tetromino(
                self.current_tetromino.name,
                Point(config.SPAWN[self.current_tetromino.name]),
                config.COLORS[self.current_tetromino.name]
            )
            self.switch_piece()
        else:
            tmp = self.current_tetromino
            self.current_tetromino = self.held_tetromino
            self.held_tetromino = Tetromino(
                tmp.name,
                Point(config.SPAWN[tmp.name]),
                config.COLORS[tmp.name]
            )

    def print_matrix(self):
        """Prints the current matrix for debugging purposes"""
        for i in reversed(range(self.height)):
            for j in range(self.width):
                print(self.board_matrix[j][i]
                      or self.piece_matrix[j][i], end=" ")
            print()
        print()
