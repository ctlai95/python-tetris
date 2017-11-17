class Coordinate:
    """A coordinate is a point on the map with an x and y position"""

    def __init__(self, coordinate):
        self.x = coordinate[0]
        self.y = coordinate[1]

    def _x(self):
        """Returns the x position"""
        return self.x

    def _y(self):
        """Returns the y position"""
        return self.y

    def _xy(self):
        """Returns the x and y positions as a tuple"""
        return (self.x, self.y)
