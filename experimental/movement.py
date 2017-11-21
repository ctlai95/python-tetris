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
            self.map.current_tetromino.move_left()

    def move_right(self):
        """If the current tetromino is moveable, move 1 unit right"""
        moveable = True
        for s in self.map.current_tetromino.sqrs:
            if s.x + 1 >= self.map.width or self.map.map_matrix[s.x + 1][s.y] != 0:
                moveable = False
                break
        if moveable:
            self.map.current_tetromino.move_right()

    def move_down(self):
        """If the current tetromino is moveable, move 1 unit down"""
        moveable = True
        for s in self.map.current_tetromino.sqrs:
            if s.y <= 0 or self.map.map_matrix[s.x][s.y - 1] != 0:
                moveable = False
                break
        if moveable:
            self.map.current_tetromino.move_down()

    def move_up(self):
        moveable = True
        for s in self.map.current_tetromino.sqrs:
            if s.y < self.map.height or self.map.matrix[s.x][s.y + 1] != 0:
                moveable = False
                break
        if moveable:
            self.map.current_tetromino.move_up()

    def rotate_cw(self):
        """Rotates a tetromino clockwise, corrected to the boundaries and other pieces"""
        self.map.current_tetromino.rotate_cw()
        for s in self.map.current_tetromino.sqrs:
            if s.x < 0:
                self.map.current_tetromino.move_right()
            elif s.x >= self.map.width:
                self.map.current_tetromino.move_left()
            elif s.y < 0:
                self.map.current_tetromino.move_up()
        # (0, 0)
        ok = True
        for s in self.map.current_tetromino.sqrs:
            if self.map.map_matrix[s.x][s.y] == 1:
                print("(0, 0): Test failed")
                ok = False
                break
        if ok is True:
            print("(0, 0): Test passed")
            return
        # (-1, 0)
        self.move_left()
        ok = True
        for s in self.map.current_tetromino.sqrs:
            if s.x >= self.map.width or s.y <= 0:
                ok = False
                break
            if self.map.map_matrix[s.x][s.y] == 1:
                print("(-2, 0): Test failed")
                ok = False
                break
        if ok is True:
            print("(-2, 0): Test passed")
            return

        self.move_right()
        # (2, 0)
        self.move_right()
        self.move_right()
        ok = True
        for s in self.map.current_tetromino.sqrs:
            if s.x >= self.map.width or s.y <= 0:
                ok = False
                break
            if self.map.map_matrix[s.x][s.y] == 1:
                print("(1, 0): Test failed")
                ok = False
                break
        if ok is True:
            print("(1, 0): Test passed")
            return
        self.move_left()
        self.move_left()
        # (-1, 2)
        self.move_left()
        self.move_up()
        self.move_up()
        ok = True
        for s in self.map.current_tetromino.sqrs:
            if s.x >= self.map.width or s.y <= 0:
                ok = False
                break
            if self.map.map_matrix[s.x][s.y] == 1:
                print("(-2, -1): Test failed")
                ok = False
                break
        if ok is True:
            print("(-2, -1): Test passed")
            return
        self.move_right()
        self.move_down()
        self.move_down()
        # (2, -1)
        self.move_right()
        self.move_right()
        self.move_down()
        ok = True
        for s in self.map.current_tetromino.sqrs:
            if self.map.map_matrix[s.x][s.y] == 1:
                print("(1, 2): Test failed")
                ok = False
                break
        if ok is True:
            print("(1, 2): Test passed")
            return
        self.move_left()
        self.move_left()
        self.move_up()

    def rotate_ccw(self):
        """Rotates a tetromino counter-clockwise, corrected to the boundaries and other pieces"""
        self.map.current_tetromino.rotate_ccw()
        for s in self.map.current_tetromino.sqrs:
            if s.x < 0:
                self.map.current_tetromino.move_right()
            elif s.x >= self.map.width:
                self.map.current_tetromino.move_left()
            elif s.y < 0:
                self.map.current_tetromino.move_up()

    def hard_drop(self):
        """Moves a tetromino down by the lowest difference"""
        for _ in range(self.map.lowest_difference()):
            self.map.current_tetromino.move_down()
        self.map.other_tetrominos.append(self.map.current_tetromino)
        self.map.switch_piece()
