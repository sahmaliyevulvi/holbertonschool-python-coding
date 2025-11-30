#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """Represents a square shape."""
    def __init__(self, size=0):
        """returns the size of square."""
        self.__size = size

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set a new size for the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current square area"""
        return self.__size * self.__size
