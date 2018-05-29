"""Game's playing area."""
import copy
import logging

from src.colors import colors
from src.randomizer.randomizer import Randomizer
from src.renderer.renderer import Renderer

log = logging.getLogger(__name__)


class Board:
    """Board contains all the tetrominos in the current game."""

    def __init__(self, width, height):
        """
        Initialize a Board object.

        Args:
            width (int): The board's width in number of units.
            height (int): The board's height in number of units.
        """
        log.info(
            "Initializing board (width={}, height={})".format(width, height)
        )
        self.width = width
        self.height = height
        self.random_tetrominos = Randomizer()
        self.current_tetromino = self.random_tetrominos.next()
        self.current_tetromino_matrix = [
            [0 for y in range(height)] for x in range(width)]
        self.next_tetromino = self.random_tetrominos.next()
        self.board_tetrominos_squares = []
        self.board_tetrominos_matrix = [
            [0 for y in range(height)] for x in range(width)]
        self.ghost_tetromino = self.get_ghost_tetromino()
        self.holdable = True
        self.held_tetromino = None

    def render_board(self):
        """Render the contents of the board to the screen."""
        self.update_matrices()

        # Render the background
        self.render_background()

        # Render pieces except current one
        for square in self.board_tetrominos_squares:
            square.render_square()

        # Render the ghost tetromino
        self.ghost_tetromino.render_tetromino()

        # Render current playable tetromino
        self.current_tetromino.render_tetromino()

    def get_filled_indices(self):
        """
        Returns the number of lines filled.

        Returns:
            list (int): The indices filled.

        """
        filled_indices = []
        for j in range(self.height):
            filled = True
            for i in range(self.width):
                if self.board_tetrominos_matrix[i][j] == 0:
                    filled = False
            if filled:
                filled_indices.append(j)
        return filled_indices

    def clear_lines(self, indices):
        """
        Takes in a list of indices that are full and removes all the
        squares in the row.

        Args:
            indices (list int): The list of filled indices.
        """

        #  Needs a copy of the list so it doesn't mutate the original list
        board_tetrominos_squares_copy = self.board_tetrominos_squares[:]
        for index in indices:
            for square in self.board_tetrominos_squares:
                if square.y == index:
                    board_tetrominos_squares_copy.remove(square)

        self.board_tetrominos_squares = board_tetrominos_squares_copy

    def drop_lines(self, indices):
        """
        Drops the lines based on the given indices.

        Args:
            indices (list int): The list of filled indices.
        """
        for lines_dropped, index in enumerate(indices):
            for square in self.board_tetrominos_squares:
                if square.y > index - lines_dropped:
                    square.y = square.y - 1

    def update_matrices(self):
        """Update the matrices to match the tetrominos in the board."""
        self.clear_matrix(self.current_tetromino_matrix)
        self.clear_matrix(self.board_tetrominos_matrix)
        for square in self.board_tetrominos_squares:
            self.fill_matrix(self.board_tetrominos_matrix, square.x, square.y)
        for square in self.current_tetromino.squares:
            self.fill_matrix(self.current_tetromino_matrix, square.x, square.y)

    def get_ghost_tetromino(self):
        """
        Return a gray clone of the current tetromino and
        moves it down by the maximum amount.

        Returns:
            Tetromino: The ghost tetromino.

        """
        self.update_matrices()
        ghost = copy.deepcopy(self.current_tetromino)
        for i in range(self.height):
            ghost.offset(0, -1)
            for square in ghost.squares:
                if square.y < 0 or self.board_tetrominos_matrix[square.x][square.y] == 1:
                    ghost.offset(0, 1)
                    break
                square.color = colors.ASH
        return ghost

    def switch_current_tetromino(self):
        """Replace the current tetromino with the next tetromino."""
        self.current_tetromino = self.next_tetromino
        self.ghost_tetromino = self.get_ghost_tetromino()
        self.next_tetromino = self.random_tetrominos.next()

    def fill_matrix(self, matrix, x, y):
        """
        Fill the given matrix at the given x and y position.

        Args:
            matrix ([][]int): The matrix with the index to be filled.
            x (int): The x coordinate of the position to be filled.
            y (int): The y coordinate of the position to be filled.
        """
        if x >= self.width or y >= self.height:
            log.error(
                "Position exceeds boundaries: [{}][{}]".format(x, y))
            return
        matrix[x][y] = 1

    def unfill_matrix(self, matrix, x, y):
        """
        Fill the given matrix at the given square's indices with a 0.

        Args:
            matrix ([][]int): The matrix with the index to be unfilled.
            x (int): The x coordinate of the position to be unfilled.
            y (int): The y coordinate of the position to be unfilled.
        """
        if x >= self.width or y >= self.height:
            log.error(
                "Position exceeds boundaries: [{}][{}]".format(x, y))
            return
        matrix[x][y] = 0

    def clear_matrix(self, matrix):
        """
        Set every element of the given matrix to 0.

        Args:
            matrix ([][]int): The matrix to be cleared.
        """
        for i in range(self.width):
            for j in range(self.height):
                matrix[i][j] = 0

    def render_background(self):
        """Render the background squares."""
        for i in range(self.width):
            for j in range(self.height):
                if (i % 2 is 0 and j % 2 is 0) or \
                        ((i + 1) % 2 is 0 and (j + 1) % 2 is 0):
                    s = Renderer(i, j, colors.CHARCOAL)
                else:
                    s = Renderer(i, j, colors.JET)
                s.draw()

    def hold_current_tetromino(self):
        """Put the current tetromino on hold to be retrieved later."""
        if self.holdable is False:
            log.info("Hold slot is already occupied by {}".format(
                self.held_tetromino.id))
            return
        self.holdable = False
        if self.held_tetromino is None:
            log.info("Putting tetromino {} on hold".format(
                self.current_tetromino.id))
            self.held_tetromino = copy.deepcopy(self.current_tetromino)
            self.held_tetromino.reset_position()
            self.switch_current_tetromino()
        else:
            log.info("Putting tetromino {} out of hold".format(
                self.held_tetromino.id))
            tmp = self.current_tetromino
            self.current_tetromino = self.held_tetromino
            log.info("Putting tetromino {} on hold".format(tmp.id))
            self.held_tetromino = copy.deepcopy(tmp)
            self.held_tetromino.reset_position()
        self.ghost_tetromino = self.get_ghost_tetromino()

    def get_combined_matrix_string(self):
        """
        Combine the board and piece matrices as a string for debugging.

        Returns:
            string: The combined matrix.

        """
        combined_matrix = "Matrix:\n"
        for j in reversed(range(self.height)):
            for i in range(self.width):
                combined_matrix += str(self.board_tetrominos_matrix[i][j] or
                                       self.current_tetromino_matrix[i][j]) + " "
            combined_matrix += "\n"
        return combined_matrix
