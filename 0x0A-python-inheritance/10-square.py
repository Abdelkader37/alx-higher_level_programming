#!/usr/bin/python3
'''Module for Square class.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''A subclass representing a square.'''

    def __init__(self, size):
        '''Constructor.'''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        '''Method for calculating the area of a square.'''
        return self.__size ** 2
