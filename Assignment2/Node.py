"""
Binary Tree Node
----------

This class represents an individual Node in a Binary Tree.

Each Node consists of the following properties:
    - left_child: Pointer to the left child of the Node
    - right_child: Pointer to the right child of the Node
    - parent: Pointer to the parent of the Node
    - weight: The weight of the Node
    - imbalance: The imbalance of the Node (absolute difference between the weight of the left and right subtree)

The class also supports the following functions:
    - add_left_child(Node): Adds the given Node as the left child
    - add_right_child(Node): Adds the given Node as the right child
    - is_external(): Returns True if the Node is a leaf node
    - update_weight(int): Updates the weight of the Node
    - get_left_child(): Returns the left child of the Node
    - get_right_child(): Returns the right child of the Node
    - get_imbalance(): Returns the imbalance of the Node

Your task is to complete the following functions which are marked by the TODO comment.
Note that your Node should automatically update the imbalance as nodes are added and weights are updated!
You are free to add properties and functions to the class as long as the given signatures remain identical
"""


class Node():
    # These are the defined properties as described above
    left_child: 'Node'
    right_child: 'Node'
    parent: 'Node'
    weight: int
    imbalance: int
    max_imbalance = -1

    def __init__(self, weight: int) -> None:
        """
        The constructor for the Node class.
        :param weight: The weight of the node.
        """
        self.weight = weight
        self.left_child = None
        self.right_child = None
        self.parent = None
        self.imbalance = 0

    def add_left_child(self, node: 'Node') -> None:
        """
        Adds the given node as the left child of the current node.
        Should do nothing if the the current node already has a left child.
        The given node is guaranteed to be new and not a child of any other node.
        :param node: The node to add as the left child.
        """

        if self.left_child != None or self == None or node == None:
            return
        self.left_child = node
        node.parent = self
        this_node = self
        while this_node.parent != None:
            this_node = this_node.parent
        Node.max_imbalance = -1
        this_node.imbalance = calculate_imbalance(this_node, this_node)



    def add_right_child(self, node: 'Node') -> None:
        """
        Adds the given node as the right child of the current node.
        Should do nothing if the the current node already has a right child.
        The given node is guaranteed to be new and not a child of any other node.
        :param node: The node to add as the right child.
        """

        if self.right_child != None or self == None or node == None:
            return
        self.right_child = node
        node.parent = self
        this_node = self
        while this_node.parent != None:
            this_node = this_node.parent
        Node.max_imbalance = -1
        this_node.imbalance = calculate_imbalance(this_node, this_node)

    def is_external(self) -> bool:
        """
        Returns True if the node is a leaf node.
        :return: True if the node is a leaf node.
        """

        return self.left_child is None and self.right_child is None

    def update_weight(self, weight: int) -> None:
        """
        Updates the weight of the current node.
        :param weight: The new weight of the node.
        """
        if self == None or weight == None:
            return
        self.weight = weight
        this_node = self
        while this_node.parent != None:
            this_node = this_node.parent
        Node.max_imbalance = -1
        this_node.imbalance = calculate_imbalance(this_node, this_node)

    def get_left_child(self) -> 'Node':
        """
        Returns the left child of the current node.
        :return: The left child of the current node.
        """

        return self.left_child

    def get_right_child(self) -> 'Node':
        """
        Returns the right child of the current node.
        :return: The right child of the current node.
        """

        return self.right_child

    def get_imbalance(self) -> int:
        """
        Returns the imbalance of the current node.
        :return: The imbalance of the current node.
        """
        return self.imbalance

def calculate_imbalance(node, root) -> int:
    right_subtree_weight = 0
    left_subtree_weight = 0
    if root.is_external() == True:
        return 0
    if node.is_external() == True:
        node.imbalance = 0
        return node.weight
    else:
        if node.left_child != None:
            left_subtree_weight = calculate_imbalance(node.left_child, root)
        if node.right_child != None:
            right_subtree_weight = calculate_imbalance(node.right_child, root)
    if node == root:
        node.imbalance = abs(right_subtree_weight-left_subtree_weight)
        if node.imbalance > Node.max_imbalance:
            Node.max_imbalance = node.imbalance
        return node.imbalance
    else:
        node.imbalance = abs(right_subtree_weight-left_subtree_weight)
        if node.imbalance > Node.max_imbalance:
            Node.max_imbalance = node.imbalance
        return (node.weight + right_subtree_weight + left_subtree_weight)
