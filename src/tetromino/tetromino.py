import logging

from src.point.point import Point
from src.square.square import Square
from src.tetromino.constants import LAYOUTS, ROTATION_POINTS, SPAWN
from src.tetromino.state import State
from src.utils.tuples import tuples

log = logging.getLogger(__name__)


class Tetromino:
    """A tetromino is a piece which consists of exactly four squares."""

    def __init__(self, id, origin, color):
        """
        Initialize a Tetromino object.

        Args:
            id (string): The identifier of the tetromino (O, I, J, L, S, Z, T)
            origin (Point): The position of the bottom left point used as a reference for the "LAYOUTS" values
            color (list): The color of the tetromino in [R, G, B] format
        """
        log.info("Initializing Tetromino (id={}, origin={}, color={})".format(
            id, origin.tuple(), color))
        self.id = id
        self.origin = origin
        self.squares = self.get_squares()
        self.state = State.ZERO
        self.color = color

    def get_squares(self):
        """
        Get the four squares that make up the tetromino.

        Returns:
            sqrs ([]Square): the four squares as a list.

        """
        squares = []
        for i in range(4):
            square_position = tuples.add(
                self.origin.tuple(), LAYOUTS[self.id][i])
            squares.append(
                Square(Point(square_position[0], square_position[1])))
        return squares

    def offset(self, x, y):
        """
        Move the tetromino by the given horizontal and vertical values.

        Args:
            x (int): The number of horizontal units to move (pos = right, neg = left).
            y (int): The number of vertical units to move (pos = up, neg = down).
        """
        new_position = tuples.add(self.origin.tuple(), (x, y))
        self.origin = Point(new_position[0], new_position[1])
        for square in self.squares:
            square.offset(x, y)

    def rotate_cw(self):
        """Rotate the tetromino by 90 degrees, clockwise."""
        # the point of rotation, relative to the board origin
        abs_rotation_pt = tuples.add(
            self.origin.tuple(), ROTATION_POINTS[self.id])
        for i in range(len(self.squares)):
            # the square's position relative to the point of rotation
            current_square = tuples.subtract(
                self.squares[i].tuple(), abs_rotation_pt)
            # the square's bottom right point, which will be the new
            # square origin after the rotation
            btm_right = tuples.add(
                current_square, (1, 0))
            # x -> y and y -> -x for rotation about the origin
            new_point = tuples.add(
                (btm_right[1], -btm_right[0]), abs_rotation_pt)
            # replace the old square with the new square
            self.squares[i] = Square(
                Point(int(new_point[0]), int(new_point[1])))
        self.state = self.state.next()

    def rotate_ccw(self):
        """Rotate the tetromino by 90 degrees, counterclockwise."""
        # the point of rotation, relative to the board origin
        abs_rotation_pt = tuples.add(
            self.origin.tuple(), ROTATION_POINTS[self.id])
        for i in range(len(self.squares)):
            # the square's position relative to the point of rotation
            current_square = tuples.subtract(
                self.squares[i].tuple(), abs_rotation_pt)
            # the square's bottom right point, which will be the new
            # square origin after the rotation
            top_left = tuples.add(
                current_square, (0, 1))
            # x -> y and y -> -x for rotation about the origin
            new_point = tuples.add(
                (-top_left[1], top_left[0]), abs_rotation_pt)

            # replace the old square with the new square
            self.squares[i] = Square(
                Point(int(new_point[0]), int(new_point[1])))
        self.state = self.state.prev()

    def reset_position(self):
        """Reset the tetromino to its original spawn position."""
        self.origin = Point(SPAWN[self.id][0], SPAWN[self.id][1])
        self.squares = self.get_squares()

    def render_tetromino(self):
        """Render the tetromino to the screen."""
        for square in self.squares:
            square.render_square(self.color)
