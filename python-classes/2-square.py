#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """Represents a square shape."""
    def __init__(self, size=0):
        """returns the size of square."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the current square area"""
        return self.__size * self.__size
