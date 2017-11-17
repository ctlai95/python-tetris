import config
import point
import tetromino


class Map:
    """Map contains all the tetrominos in the current game"""

    def __init__(self, width, height):
        self.matrix = [[0 for y in range(height)] for x in range(width)]
        name = "O"
        self.current_tetromino = tetromino.Tetromino(
            name, point.Point(config.SPAWN[name]))
        self.other_tetrominos = []

    def render_map(self):
        """Renders the map to the screen"""
        self.clear_matrix()

        # Render current playable piece
        self.current_tetromino.render_tetromino()
        for s in self.current_tetromino.sqrs:
            self.fill_matrix(s)

        # Render the rest of the map
        for t in self.other_tetrominos:
            t.render_tetromino()
            for s in t.sqrs:
                self.fill_matrix(s)

    def fill_matrix(self, square):
        """Fills the matrix at the given indices with a 1"""
        self.matrix[square.x][square.y] = 1

    def clear_matrix(self):
        """Clears the current matrix"""
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] = 0

    def print_matrix(self):
        """Prints the current matrix for debugging purposes"""
        for i in reversed(range(len(self.matrix[0]))):
            for j in range(len(self.matrix)):
                if self.matrix[j][i] != 0:
                    print(1, end=" ")
                else:
                    print(0, end=" ")
            print()
        print()
