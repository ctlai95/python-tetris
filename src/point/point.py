import logging

log = logging.getLogger(__name__)


class Point:
    """A point is a coordinate on the board with an x and y position."""

    def __init__(self, x, y):
        """
        Initialize a Point object.

        Args:
            x (int): The x coordinate
            y (int): The y coorindate
        """
        self.x = x
        self.y = y

    def tuple(self):
        """
        Return the x and y positions as a tuple.

        Returns:
            int tuple: The x and y coordinates.

        """
        return (self.x, self.y)
