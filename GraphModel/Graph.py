import random

from GraphModel.Node import Node


class Graph:
    """
    The Graph class represents a graph structure consisting of nodes.
    It provides functionality to manage and manipulate a collection of nodes,
    including adding new nodes and defining their initial positions.
    This class serves as the core data structure.
    """
    # Default team name associated with the graph
    team_name = "Die mutigen Mungos"
    # Initial central position for new nodes
    INITIAL_CENTER_POSITION = 5000000
    # List to store all nodes in the graph
    nodes = []

    def add_new_node_to_graph(self, node: Node):
        """
        Adds a new Node to the graph. This method calculates a random position for the node
        near the center of the graph's defined initial central position.

        :param: node: An instance of Node to be added to the graph.
        """
        node.x = random.randint(self.INITIAL_CENTER_POSITION - 5, self.INITIAL_CENTER_POSITION + 5)
        node.y = random.randint(self.INITIAL_CENTER_POSITION - 5, self.INITIAL_CENTER_POSITION + 5)
        self.nodes.append(node)
