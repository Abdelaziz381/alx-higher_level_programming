#!/usr/bin/python3
"""Square Class."""


class Square():
    """Square Empty Class."""
    def __init__(self, size):
        """Constructir.
        Args:
            size: side square length
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise TypeError("size must be >= 0")
        self.__size = size
