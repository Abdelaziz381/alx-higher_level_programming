#!/usr/bin/python3
"""Square Class."""


class Square():
    """Square Empty Class."""
    def __init__(self, size=0):
        """Constructir.
        Args:
            size: side square length
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Area of square
        Returns:
            Squared size
        """
        return self.__size ** 2
