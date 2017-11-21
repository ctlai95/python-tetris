import config
import point
import tetromino


class Map:
    """Map contains all the tetrominos in the current game"""

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map_matrix = [[0 for y in range(height)] for x in range(width)]
        self.piece_matrix = [[0 for y in range(height)] for x in range(width)]
        name = "I"
        self.current_tetromino = tetromino.Tetromino(
            name, point.Point(config.SPAWN[name]))
        self.other_tetrominos = []

    def render_map(self):
        """Renders the map to the screen"""
        self.clear_matrix(self.piece_matrix)
        self.clear_matrix(self.map_matrix)

        # Render current playable piece
        self.current_tetromino.render_tetromino()
        for s in self.current_tetromino.sqrs:
            self.fill_matrix(self.piece_matrix, s)

        # Render the rest of the map
        for t in self.other_tetrominos:
            t.render_tetromino()
            for s in t.sqrs:
                self.fill_matrix(self.map_matrix, s)

    def switch_piece(self):
        self.current_tetromino = tetromino.Tetromino(
            "I", point.Point(config.SPAWN["I"]))

    def fill_matrix(self, matrix, square):
        """Fills the matrix at the given indices with a 1"""
        if square.x >= self.width or square.y >= self.height:
            print(
                "Warning: position exceeds boundaries: [{:d}][{:d}]".format(square.x, square.y))
            return
        matrix[square.x][square.y] = 1

    def unfill_matrix(self, matrix, square):
        """Fills the matrix at the given indices with a 0"""
        if square.x >= self.width or square.y >= self.height:
            print(
                "Warning: position exceeds boundaries: [{:d}][{:d}]".format(square.x, square.y))
            return
        matrix[square.x][square.y] = 0

    def clear_matrix(self, matrix):
        """Clears the current matrix"""
        for i in range(self.width):
            for j in range(self.height):
                matrix[i][j] = 0

    def lowest_difference(self):
        """Returns the number of units a tetromino can drop before touching something"""
        tetromino_lowest = self.height
        for s in self.current_tetromino.sqrs:
            if s.y < tetromino_lowest:
                tetromino_lowest = s.y
        lowest_difference = self.height
        for s in self.current_tetromino.sqrs:
            y = tetromino_lowest
            count = 0
            while y > 0:
                y -= 1
                if self.map_matrix[s.x][y] != 0:
                    break
                count += 1
            if count < lowest_difference:
                lowest_difference = count
        return lowest_difference

    def print_matrix(self):
        """Prints the current matrix for debugging purposes"""
        for i in reversed(range(self.height)):
            for j in range(self.width):
                if self.map_matrix[j][i] != 0:
                    print(1, end=" ")
                else:
                    print(0, end=" ")
            print()
        print()
