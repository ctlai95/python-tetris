"""Tetromino movement handler."""
import logging

from src.tetromino.constants import WALL_KICKS
from src.tetromino.state import State

log = logging.getLogger(__name__)


class Movement:
    """Movement handles all the tetromino movements in the game."""

    def __init__(self, board):
        """
        Initialize a Movement handler.

        Args:
            board (Board): The game's board object.
        """
        self.board = board

    def move_left(self):
        """Move the current tetromino one unit left if it is moveable."""
        moveable = True
        for square in self.board.current_tetromino.squares:
            if square.x <= 0 or self.board.board_tetrominos_matrix[square.x - 1][square.y] != 0:
                moveable = False
                break
        if moveable:
            log.debug("Moving current tetromino left")
            self.board.current_tetromino.offset(-1, 0)
            self.board.ghost_tetromino = self.board.get_ghost_tetromino()

    def move_right(self):
        """Move the current tetromino one unit right if it is moveable."""
        moveable = True

        for square in self.board.current_tetromino.squares:
            if square.x + 1 >= self.board.width or \
                    self.board.board_tetrominos_matrix[square.x + 1][square.y] != 0:
                moveable = False
                break
        if moveable:
            log.debug("Moving current tetromino right")
            self.board.current_tetromino.offset(1, 0)
            self.board.ghost_tetromino = self.board.get_ghost_tetromino()

    def move_down(self):
        """Move the current tetromino one unit down if it is moveable."""
        moveable = True
        for square in self.board.current_tetromino.squares:
            if square.y <= 0 or self.board.board_tetrominos_matrix[square.x][square.y - 1] != 0:
                moveable = False
                break
        if moveable:
            log.debug("Moving current tetromino down")
            self.board.current_tetromino.offset(0, -1)
            self.board.ghost_tetromino = self.board.get_ghost_tetromino()

    def move_up(self):
        """Move the current tetromino one unit up if it is moveable."""
        moveable = True
        for square in self.board.current_tetromino.squares:
            if square.y < self.board.height or self.board.matrix[square.x][square.y + 1] != 0:
                moveable = False
                break
        if moveable:
            log.debug("Moving current tetromino up")
            self.board.current_tetromino.offset(0, 1)
            self.board.ghost_tetromino = self.board.get_ghost_tetromino()

    def rotate_cw(self):
        """Rotate a tetromino clockwise, corrected to boundaries and other tetrominos."""
        if self.board.current_tetromino.id == "O":
            log.debug("Tetromino \"O\" detected, skipping")
            return

        if self.board.current_tetromino.id in ("J", "L", "S", "T", "Z"):
            wall_kick = WALL_KICKS["JLSTZ"]
        elif self.board.current_tetromino.id == "I":
            wall_kick = WALL_KICKS["I"]

        if self.board.current_tetromino.state == State.ZERO:
            rotation = "0->1"
        elif self.board.current_tetromino.state == State.ONE:
            rotation = "1->2"
        elif self.board.current_tetromino.state == State.TWO:
            rotation = "2->3"
        elif self.board.current_tetromino.state == State.THREE:
            rotation = "3->0"

        self.board.current_tetromino.rotate_cw()
        for i, p in enumerate(wall_kick[rotation]):
            if self.wall_kick_test_pass(p[0], p[1]):
                log.debug("Clockwise rotation wall kick passed Test #{} with offset ({}, {})".format(
                    i + 1, p[0], p[1]))
                self.board.ghost_tetromino = self.board.get_ghost_tetromino()
                return

        # if it reaches here that means all tests have failed, so rotate back
        self.board.current_tetromino.rotate_ccw()
        log.debug("All clockwise rotation wall kicks failed, not rotating")

    def rotate_ccw(self):
        """Rotate a tetromino counterclockwise, corrected to boundaries and other tetrominos."""
        if self.board.current_tetromino.id == "O":
            log.debug("Tetromino \"O\" detected, skipping")
            return

        if self.board.current_tetromino.id in ("J", "L", "S", "T", "Z"):
            wall_kick = WALL_KICKS["JLSTZ"]
        elif self.board.current_tetromino.id == "I":
            wall_kick = WALL_KICKS["I"]

        if self.board.current_tetromino.state == State.ZERO:
            rotation = "0->3"
        elif self.board.current_tetromino.state == State.ONE:
            rotation = "1->0"
        elif self.board.current_tetromino.state == State.TWO:
            rotation = "2->1"
        elif self.board.current_tetromino.state == State.THREE:
            rotation = "3->2"

        self.board.current_tetromino.rotate_ccw()
        for i, p in enumerate(wall_kick[rotation]):
            if self.wall_kick_test_pass(p[0], p[1]):
                log.debug("Counterclockwise rotation wall kick passed Test #{} with offset ({}, {})".format(
                    i + 1, p[0], p[1]))
                self.board.ghost_tetromino = self.board.get_ghost_tetromino()
                return

        # if it reaches here that means all tests have failed, so rotate back
        self.board.current_tetromino.rotate_cw()
        log.debug("All clockwise rotation wall kicks failed, not rotating")

    def wall_kick_test_pass(self, x, y):
        """
        Perform a wall kick test to determine the resulting position after a rotation.

        Args:
            x (int): The x coordinate of the position being tested.
            y (int): The y coordinate of the position being tested.

        Returns:
            bool: Whether or not the wall kick test passed.

        """
        self.board.current_tetromino.offset(x, y)
        for square in self.board.current_tetromino.squares:
            if square.x < 0 or square.x >= self.board.width or \
                square.y < 0 or square.y >= self.board.height or \
                    self.board.board_tetrominos_matrix[square.x][square.y] == 1:
                self.board.current_tetromino.offset(-x, -y)
                return False
        return True

    def hard_drop(self):
        """Move a tetromino down by the lowest difference."""
        log.info("Hard dropping current tetromino")
        for i in range(self.board.height):
            self.board.current_tetromino.offset(0, -1)
            for square in self.board.current_tetromino.squares:
                if square.y < 0 or self.board.board_tetrominos_matrix[square.x][square.y] == 1:
                    self.board.current_tetromino.offset(0, 1)
                    break

        for square in self.board.current_tetromino.squares:
            self.board.board_tetrominos_squares.append(square)

        self.board.switch_current_tetromino()
        self.board.holdable = True
        filled_indices = self.board.get_filled_indices()
        self.board.clear_lines(filled_indices)
        self.board.drop_lines(filled_indices)
