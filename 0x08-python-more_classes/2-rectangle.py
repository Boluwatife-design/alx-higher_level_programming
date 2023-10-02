#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represents a rectangle"""
    
    def __init__(self, width=0, height=0):
        """Initialize a new rectangle
            
        :width(int): The width of the rectangle.
        :height(int): The height of a rectangle
        """
        self.width = width
        self.height = height
            
    @property
    def width(self):
        """Get/set the width of a rectangle."""
        return self.__width
        
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >=0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of a rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")
        self.__height = value
        
    def area(self):
        """returns rectangle area"""
        return (self.__width * self.__height)
    
    def perimeter(self):
        """returns perimeter area"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))
