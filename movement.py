import config

import map
import tetromino


class Movement:
    def __init__(self, map):
        self.map = map

    def move_left(self):
        """If the current tetromino is moveable, move 1 unit left"""
        moveable = True
        for s in self.map.current_tetromino.sqrs:
            if s.x <= 0 or self.map.map_matrix[s.x - 1][s.y] != 0:
                moveable = False
                break
        if moveable:
            self.map.current_tetromino.offset(-1, 0)

    def move_right(self):
        """If the current tetromino is moveable, move 1 unit right"""
        moveable = True
        for s in self.map.current_tetromino.sqrs:
            if s.x + 1 >= self.map.width or self.map.map_matrix[s.x + 1][s.y] != 0:
                moveable = False
                break
        if moveable:
            self.map.current_tetromino.offset(1, 0)

    def move_down(self):
        """If the current tetromino is moveable, move 1 unit down"""
        moveable = True
        for s in self.map.current_tetromino.sqrs:
            if s.y <= 0 or self.map.map_matrix[s.x][s.y - 1] != 0:
                moveable = False
                break
        if moveable:
            self.map.current_tetromino.offset(0, -1)

    def move_up(self):
        moveable = True
        for s in self.map.current_tetromino.sqrs:
            if s.y < self.map.height or self.map.matrix[s.x][s.y + 1] != 0:
                moveable = False
                break
        if moveable:
            self.map.current_tetromino.offset(0, 1)

    def rotate_cw(self):
        """Rotates a tetromino clockwise, corrected to the boundaries and other pieces"""
        if self.map.current_tetromino.name == "O":
            return

        if self.map.current_tetromino.name in ("J", "L", "S", "T", "Z"):
            wall_kick = config.JLSTZ_WALL_KICK
        elif self.map.current_tetromino.name == "I":
            wall_kick = config.I_WALL_KICK

        if self.map.current_tetromino.state == 0:
            rotation = "0R"
        elif self.map.current_tetromino.state == 1:
            rotation = "R2"
        elif self.map.current_tetromino.state == 2:
            rotation = "2L"
        elif self.map.current_tetromino.state == 3:
            rotation = "L0"

        self.map.current_tetromino.rotate_cw()
        for p in wall_kick[rotation]:
            ok = self.wall_kick_test(p[0], p[1])
            if ok:
                return

        # if it reaches here that means all tests have failed, so rotate back
        self.map.current_tetromino.rotate_ccw()

    def rotate_ccw(self):
        """Rotates a tetromino counter-clockwise, corrected to the boundaries and other pieces"""
        if self.map.current_tetromino.name == "O":
            return

        if self.map.current_tetromino.name in ("J", "L", "S", "T", "Z"):
            wall_kick = config.JLSTZ_WALL_KICK
        elif self.map.current_tetromino.name == "I":
            wall_kick = config.I_WALL_KICK

        if self.map.current_tetromino.state == 0:
            rotation = "0L"
        elif self.map.current_tetromino.state == 1:
            rotation = "R0"
        elif self.map.current_tetromino.state == 2:
            rotation = "2R"
        elif self.map.current_tetromino.state == 3:
            rotation = "L2"

        self.map.current_tetromino.rotate_ccw()
        for p in wall_kick[rotation]:
            ok = self.wall_kick_test(p[0], p[1])
            if ok:
                return

        # if it reaches here that means all tests have failed, so rotate back
        self.map.current_tetromino.rotate_cw()

    def wall_kick_test(self, x, y):
        self.map.current_tetromino.offset(x, y)
        for s in self.map.current_tetromino.sqrs:
            if s.x < 0 or s.x >= self.map.width or \
                s.y < 0 or s.y >= self.map.height or \
                    self.map.map_matrix[s.x][s.y] == 1:
                self.map.current_tetromino.offset(-x, -y)
                return False
        return True

    def hard_drop(self):
        """Moves a tetromino down by the lowest difference"""
        for i in range(self.map.height):
            self.map.current_tetromino.offset(0, -1)
            for s in self.map.current_tetromino.sqrs:
                if s.y < 0 or self.map.map_matrix[s.x][s.y] == 1:
                    self.map.current_tetromino.offset(0, 1)
                    break
        self.map.other_tetrominos.append(self.map.current_tetromino)
        self.map.switch_piece()
        self.map.holdable = True
