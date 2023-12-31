#!/usr/bin/python3
"""Defines the Square class, a subclass of Rectangle."""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for Square.

        Attributes:
            size (int): Size of the square.
            x (int, optional): x position. Defaults to 0.
            y (int, optional): y position. Defaults to 0.
            id (int, optional): Id of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        String representation of the Square.

        Returns:
            str: [Square] (<id>) <x>/<y> - <size>
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        Gets the size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the Square attributes.
        """
        attrs = ["id", "size", "x", "y"]

        if args and len(args) > 0:
            for i, value in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], value)
            return

        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Square instance.
        """
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
