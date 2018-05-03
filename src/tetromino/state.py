"""Tetromino rotation state."""
from enum import Enum


class State(Enum):
    """State is used to keep track of a tetromino's rotation state."""

    ZERO = 0  # Initial spawn state
    ONE = 1  # 1 clockwise or 3 counterclockwise rotations from spawn state
    TWO = 2  # 2 rotations in either direction from spawn state
    THREE = 3  # 3 clockwise or 1 counterclockwise rotations from spawn state

    def next(self):
        """
        Get the next rotation state.

        Returns:
            State: the next rotation state.

        """
        v = (self.value + 1) % 4
        return State(v)

    def prev(self):
        """
        Get the previous rotation state.

        Returns:
            State: the previous rotation state.

        """
        v = (self.value - 1) % 4
        return State(v)
