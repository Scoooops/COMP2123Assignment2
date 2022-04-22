from Node import Node, calculate_imbalance

"""
Tree
----------

This class represents the Binary Tree used to model our baby mobile.

Each Tree consists of the following properties:
    - root: The root of the Tree

The class also supports the following functions:
    - put(node, child, left_child): Adds child to the given node as the left or right child depending on the value of left_child
    - move_subtree(node_a, node_b, left_child): Move node_a to the left or right child of node_b depending on the value of left_child
    - find_max_imbalance(): Finds the node with the maximum imbalance in the tree

Your task is to complete the following functions which are marked by the TODO comment.
Note that your modifications to the structure of the tree should be correctly updated in the underlying Node class!
You are free to add properties and functions to the class as long as the given signatures remain identical.
"""


class Tree():
    # These are the defined properties as described above
    root: Node

    def __init__(self, root: Node = None) -> None:
        """
        The constructor for the Tree class.
        :param root: The root node of the Tree.
        """
        self.root = root
        Node.max_imbalance = -1
        root.imbalance = calculate_imbalance(root, root)

    def put(self, node: Node, child: Node, left_child: bool) -> None:
        """
        Adds the given child to the given node as the left or right child depending on the value of left_child.
        If a node already has a child at the indicated position, this function should do nothing.
        You are guranteed that the given node is not already part of the tree
        :param node: The node to add the child to.
        :param child: The child to add to the node.
        :param left_child: True if the child should be added to the left child, False otherwise.
        """
        if node == None or child == None or left_child == None:
            return
        if left_child == False:
            if node.right_child != None:
                return
            node.right_child = child
        else:
            if node.left_child != None:
                return
            node.left_child = child
        child.parent = node
        this_node = node
        while this_node.parent != None:
            this_node = this_node.parent
        Node.max_imbalance = -1
        this_node.imbalance = calculate_imbalance(this_node, this_node)

    def move_subtree(self, node_a: Node, node_b: Node, left_child: bool) -> None:
        """
        Moves the subtree rooted at node_a to the left or right child of node_b depending on the value of left_child.
        If node_b already has a child at the indicated position, this function should do nothing
        You can safely assume that node_b is not descendent of node_a.
        :param node_a: The root of the subtree to move.
        :param node_b: The node to add the subtree to.
        :param left_child: True if the subtree should be added to the left child, False otherwise.
        """

        if node_a == None or node_b == None or left_child == None:
            return
        this_node = node_b
        while this_node.parent != None:
            if this_node.parent == node_a:
                return
            this_node = this_node.parent

        if left_child == False:
            if node_b.right_child != None:
                return
            if node_a.parent != None:
                node_a.parent.right_child = None
            node_a.parent = node_b
            node_b.right_child = node_a

        else:
            if node_b.left_child != None:
                return
            if node_a.parent != None:
                node_a.parent.left_child = None
            node_a.parent = node_b
            node_b.left_child = node_a
        this_node = node_b
        while this_node.parent != None:
            this_node = this_node.parent
        Node.max_imbalance = -1
        this_node.imbalance = calculate_imbalance(this_node, this_node)

    def find_max_imbalance(self) -> int:
        """
        Finds the node with the maximum imbalance in the tree.
        :return: The node with the maximum imbalance.
        """
        return Node.max_imbalance
