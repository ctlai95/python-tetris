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

    def rotate_cw(self):
        """Rotates a tetromino clockwise, corrected to the boundaries and other pieces"""
        clone = tetromino.Tetromino(
            self.map.current_tetromino.name, self.map.current_tetromino.loc)
        clone.rotate_cw()
        for s in clone.sqrs:
            print(s.x, s.y)
        # self.map.current_tetromino.rotate_cw()
        # for s in self.map.current_tetromino.sqrs:
        #     if s.x < 0:
        #         self.map.current_tetromino.move_right()
        #     elif s.x >= self.map.width:
        #         self.map.current_tetromino.move_left()
        #     elif s.y < 0:
        #         self.map.current_tetromino.move_up()

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
