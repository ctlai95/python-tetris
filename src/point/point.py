"""Position in the game."""
import logging

log = logging.getLogger(__name__)


class Point:
    """A point is a coordinate on the board with an x and y position."""

    def __init__(self, x, y):
        """
        Initialize a Point object.

        Args:
            x (int): The x coordinate.
            y (int): The y coorindate.
        """
        self.x = x
        self.y = y

    def add(self, point):
        """
        Calculate the addition of two points.

        Args:
            point (Point): The point to be added to the current point.

        Returns:
            Point: The resulting point.

        """
        return Point(self.x + point.x, self.y + point.y)

    def subtract(self, point):
        """
        Calculate the subtraction of two points.

        Args:
            point (Point): The point to be subtracted to the current point.

        Returns:
            Point: The resulting point.

        """
        return Point(self.x - point.x, self.y - point.y)

    def equals(self, point):
        """
        Determine whether two points have the same x and y value.

        Args:
            point (Point): The point to be compared to.

        Returns:
            bool: True for equals, False otherwise.
        """
        return (self.x, self.y) == (point.x, point.y)
