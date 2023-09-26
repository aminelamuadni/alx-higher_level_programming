#!/usr/bin/python3
"""
Module for Node and SinglyLinkedList classes.
"""


class Node:
    """
    Represents a node in a singly linked list.
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a Node instance.

        Args:
            data (int): Data stored in the node.
            next_node (Node, optional): Next node in the linked list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Get node data.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set node data.

        Args:
            value (int): Data to set.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Get the next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node.

        Args:
            value (Node): Next node or None.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Represents a singly linked list.
    """
    def __init__(self):
        """
        Initializes a SinglyLinkedList instance.
        """
        self.__head = None

    def __str__(self):
        """
        Return a formatted string representation of the linked list.
        """
        values = []
        current = self.__head
        while current:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position.

        Args:
            value (int): Value to insert.
        """
        new_node = Node(value)
        if not self.__head:
            self.__head = new_node
            return

        if value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
