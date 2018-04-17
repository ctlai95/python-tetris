import copy
import logging

from src import config
from src.colors import colors
from src.point.point import Point
from src.randomizer.randomizer import Randomizer
from src.renderer.renderer import Renderer
from src.tetromino.tetromino import Tetromino

log = logging.getLogger(__name__)


class Board:
    """Board contains all the tetrominos in the current game"""

    def __init__(self, width, height):
        log.info("Initializing board (width={}, height={})".format(width, height))
        self.width = width
        self.height = height
        self.board_tetrominos_matrix = [
            [0 for y in range(height)] for x in range(width)]
        self.current_tetromino_matrix = [
            [0 for y in range(height)] for x in range(width)]
        self.random_list = Randomizer()
        self.next_piece = self.random_list.next()
        self.current_tetromino = Tetromino(
            self.next_piece,
            Point(config.SPAWN[self.next_piece]),
            config.COLORS[self.next_piece]
        )
        self.next_piece = self.random_list.next()
        log.info("Next piece is {}".format(self.next_piece))
        self.board_tetrominos = []
        self.holdable = True
        self.held_tetromino = None

    def render_board(self):
        """Renders the board to the screen and updates matrices"""
        self.clear_matrix(self.current_tetromino_matrix)
        self.clear_matrix(self.board_tetrominos_matrix)

        # Render the background
        self.render_background()

        # Render pieces except current one
        for t in self.board_tetrominos:
            t.render_tetromino()
            for s in t.sqrs:
                self.fill_matrix(self.board_tetrominos_matrix, s)

        # Render the ghost tetromino
        # self.render_ghost()

        # Render current playable tetromino
        self.current_tetromino.render_tetromino()
        for s in self.current_tetromino.sqrs:
            self.fill_matrix(self.current_tetromino_matrix, s)

    def switch_current_tetromino(self):
        """Assigns a new current piece"""
        self.current_tetromino = Tetromino(
            self.next_piece,
            Point(config.SPAWN[self.next_piece]),
            config.COLORS[self.next_piece]
        )
        self.next_piece = self.random_list.next()
        log.info("Next piece is {}".format(self.next_piece))

    def render_ghost(self):
        """Renders the ghost of the current tetromino"""
        ghost = Tetromino(
            self.current_tetromino.name,
            self.current_tetromino.btm_left_pt,
            colors.ASH
        )
        for i in range(self.current_tetromino.state.value):
            ghost.rotate_cw()
        for i in range(self.height):
            ghost.offset(0, -1)
            for s in ghost.sqrs:
                if s.y < 0 or self.board_tetrominos_matrix[s.x][s.y] == 1:
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

    def hold_current_tetromino(self):
        """Holds the current tetromino and switches to another one"""
        if self.holdable is False:
            log.info("Hold slot is already occupied by {}".format(
                self.held_tetromino.name))
            return
        self.holdable = False
        if self.held_tetromino is None:
            log.info("Putting tetromino {} on hold".format(
                self.current_tetromino.name))
            self.held_tetromino = copy.deepcopy(self.current_tetromino)
            self.switch_current_tetromino()
        else:
            log.info("Putting tetromino {} out of hold".format(
                self.held_tetromino.name))
            tmp = self.current_tetromino
            self.current_tetromino = self.held_tetromino
            log.info("Putting tetromino {} on hold".format(tmp.name))
            self.held_tetromino = copy.deepcopy(tmp)

    def get_combined_matrix_string(self):
        """Combines the board and piece matrices as a string for debugging"""
        combined_matrix = "Matrix:\n"
        for j in reversed(range(self.height)):
            for i in range(self.width):
                combined_matrix += str(self.board_tetrominos_matrix[i]
                                       [j] or self.current_tetromino_matrix[i][j]) + " "
            combined_matrix += "\n"
        return combined_matrix
