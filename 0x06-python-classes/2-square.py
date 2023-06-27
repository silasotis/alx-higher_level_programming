#!/usr/bin/python3
"""Defines a square"""


class Square:
    """The square"""
    def __init__(self, size=0):
        """Initialise the square

    Args:
        size(int): The size of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    self.__size = size
