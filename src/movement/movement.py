import logging

from src.tetromino.constants import WALL_KICKS
from src.tetromino.tetromino import State

log = logging.getLogger(__name__)


class Movement:
    def __init__(self, board):
        self.board = board

    def move_left(self):
        """If the current tetromino is moveable, move 1 unit left"""
        moveable = True
        for s in self.board.current_tetromino.sqrs:
            if s.x <= 0 or self.board.board_tetrominos_matrix[s.x - 1][s.y] != 0:
                moveable = False
                break
        if moveable:
            log.debug("Moving current tetromino left")
            self.board.current_tetromino.offset(-1, 0)
            self.board.ghost_tetromino = self.board.get_ghost_tetromino()

    def move_right(self):
        """If the current tetromino is moveable, move 1 unit right"""
        moveable = True

        for s in self.board.current_tetromino.sqrs:
            if s.x + 1 >= self.board.width or \
                    self.board.board_tetrominos_matrix[s.x + 1][s.y] != 0:
                moveable = False
                break
        if moveable:
            log.debug("Moving current tetromino right")
            self.board.current_tetromino.offset(1, 0)
            self.board.ghost_tetromino = self.board.get_ghost_tetromino()

    def move_down(self):
        """If the current tetromino is moveable, move 1 unit down"""
        moveable = True
        for s in self.board.current_tetromino.sqrs:
            if s.y <= 0 or self.board.board_tetrominos_matrix[s.x][s.y - 1] != 0:
                moveable = False
                break
        if moveable:
            log.debug("Moving current tetromino down")
            self.board.current_tetromino.offset(0, -1)
            self.board.ghost_tetromino = self.board.get_ghost_tetromino()

    def move_up(self):
        moveable = True
        for s in self.board.current_tetromino.sqrs:
            if s.y < self.board.height or self.board.matrix[s.x][s.y + 1] != 0:
                moveable = False
                break
        if moveable:
            log.debug("Moving current tetromino up")
            self.board.current_tetromino.offset(0, 1)
            self.board.ghost_tetromino = self.board.get_ghost_tetromino()

    def rotate_cw(self):
        """
        Rotates a tetromino clockwise, corrected to boundaries and other pieces
        """
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
            ok = self.wall_kick_test(p[0], p[1])
            if ok:
                log.debug("Clockwise rotation wall kick passed Test #{} with offset ({}, {})".format(
                    i + 1, p[0], p[1]))
                self.board.ghost_tetromino = self.board.get_ghost_tetromino()
                return

        # if it reaches here that means all tests have failed, so rotate back
        self.board.current_tetromino.rotate_ccw()
        log.debug("All clockwise rotation wall kicks failed, not rotating")

    def rotate_ccw(self):
        """
        Rotates a tetromino counterclockwise, corrected to boundaries and
        other pieces
        """
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
            ok = self.wall_kick_test(p[0], p[1])
            if ok:
                log.debug("Counterclockwise rotation wall kick passed Test #{} with offset ({}, {})".format(
                    i + 1, p[0], p[1]))
                self.board.ghost_tetromino = self.board.get_ghost_tetromino()
                return

        # if it reaches here that means all tests have failed, so rotate back
        self.board.current_tetromino.rotate_cw()
        log.debug("All clockwise rotation wall kicks failed, not rotating")

    def wall_kick_test(self, x, y):
        self.board.current_tetromino.offset(x, y)
        for s in self.board.current_tetromino.sqrs:
            if s.x < 0 or s.x >= self.board.width or \
                s.y < 0 or s.y >= self.board.height or \
                    self.board.board_tetrominos_matrix[s.x][s.y] == 1:
                self.board.current_tetromino.offset(-x, -y)
                return False
        return True

    def hard_drop(self):
        """Moves a tetromino down by the lowest difference"""
        log.info("Hard dropping current tetromino")
        for i in range(self.board.height):
            self.board.current_tetromino.offset(0, -1)
            for s in self.board.current_tetromino.sqrs:
                if s.y < 0 or self.board.board_tetrominos_matrix[s.x][s.y] == 1:
                    self.board.current_tetromino.offset(0, 1)
                    break

        for square in self.board.current_tetromino.sqrs:
            self.board.board_tetrominos_squares.append(square)

        self.board.switch_current_tetromino()
        self.board.holdable = True
        filled_indices = self.board.get_filled_indices()
        self.board.clear_lines(filled_indices)
        self.board.drop_lines(filled_indices)
