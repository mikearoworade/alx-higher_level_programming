#!/usr/bin/python3
# base.py
# Michael Aroworade
""" Define a base model class. """


class Base:
    """ Represent the base model.
    base for all other classes in project

    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
