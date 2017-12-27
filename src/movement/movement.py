from src import config
from src.tetromino.tetromino import State


class Movement:
    def __init__(self, board):
        self.board = board

    def move_left(self):
        """If the current tetromino is moveable, move 1 unit left"""
        moveable = True
        for s in self.board.current_tetromino.sqrs:
            if s.x <= 0 or self.board.board_matrix[s.x - 1][s.y] != 0:
                moveable = False
                break
        if moveable:
            self.board.current_tetromino.offset(-1, 0)

    def move_right(self):
        """If the current tetromino is moveable, move 1 unit right"""
        moveable = True

        for s in self.board.current_tetromino.sqrs:
            if s.x + 1 >= self.board.width or \
                    self.board.board_matrix[s.x + 1][s.y] != 0:
                moveable = False
                break
        if moveable:
            self.board.current_tetromino.offset(1, 0)

    def move_down(self):
        """If the current tetromino is moveable, move 1 unit down"""
        moveable = True
        for s in self.board.current_tetromino.sqrs:
            if s.y <= 0 or self.board.board_matrix[s.x][s.y - 1] != 0:
                moveable = False
                break
        if moveable:
            self.board.current_tetromino.offset(0, -1)

    def move_up(self):
        moveable = True
        for s in self.board.current_tetromino.sqrs:
            if s.y < self.board.height or self.board.matrix[s.x][s.y + 1] != 0:
                moveable = False
                break
        if moveable:
            self.board.current_tetromino.offset(0, 1)

    def rotate_cw(self):
        """
        Rotates a tetromino clockwise, corrected to boundaries and other pieces
        """
        if self.board.current_tetromino.name == "O":
            return

        if self.board.current_tetromino.name in ("J", "L", "S", "T", "Z"):
            wall_kick = config.JLSTZ_WALL_KICK
        elif self.board.current_tetromino.name == "I":
            wall_kick = config.I_WALL_KICK

        if self.board.current_tetromino.state == State.ZERO:
            rotation = "0->1"
        elif self.board.current_tetromino.state == State.ONE:
            rotation = "1->2"
        elif self.board.current_tetromino.state == State.TWO:
            rotation = "2->3"
        elif self.board.current_tetromino.state == State.THREE:
            rotation = "3->0"

        self.board.current_tetromino.rotate_cw()
        for p in wall_kick[rotation]:
            ok = self.wall_kick_test(p[0], p[1])
            if ok:
                return

        # if it reaches here that means all tests have failed, so rotate back
        self.board.current_tetromino.rotate_ccw()

    def rotate_ccw(self):
        """
        Rotates a tetromino counter-clockwise, corrected to boundaries and
        other pieces
        """
        if self.board.current_tetromino.name == "O":
            return

        if self.board.current_tetromino.name in ("J", "L", "S", "T", "Z"):
            wall_kick = config.JLSTZ_WALL_KICK
        elif self.board.current_tetromino.name == "I":
            wall_kick = config.I_WALL_KICK

        if self.board.current_tetromino.state == State.ZERO:
            rotation = "0->3"
        elif self.board.current_tetromino.state == State.ONE:
            rotation = "1->0"
        elif self.board.current_tetromino.state == State.TWO:
            rotation = "2->1"
        elif self.board.current_tetromino.state == State.THREE:
            rotation = "3->2"

        self.board.current_tetromino.rotate_ccw()
        for p in wall_kick[rotation]:
            ok = self.wall_kick_test(p[0], p[1])
            if ok:
                return

        # if it reaches here that means all tests have failed, so rotate back
        self.board.current_tetromino.rotate_cw()

    def wall_kick_test(self, x, y):
        self.board.current_tetromino.offset(x, y)
        for s in self.board.current_tetromino.sqrs:
            if s.x < 0 or s.x >= self.board.width or \
                s.y < 0 or s.y >= self.board.height or \
                    self.board.board_matrix[s.x][s.y] == 1:
                self.board.current_tetromino.offset(-x, -y)
                return False
        return True

    def hard_drop(self):
        """Moves a tetromino down by the lowest difference"""
        for i in range(self.board.height):
            self.board.current_tetromino.offset(0, -1)
            for s in self.board.current_tetromino.sqrs:
                if s.y < 0 or self.board.board_matrix[s.x][s.y] == 1:
                    self.board.current_tetromino.offset(0, 1)
                    break
        self.board.switch_piece()
