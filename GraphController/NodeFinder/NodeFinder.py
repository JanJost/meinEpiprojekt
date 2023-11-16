import pygame

from GraphModel import Graph
from View.GraphView import ScaleOffsetTransformer


class NodeFinder:
    """
    The NodeFinder class is responsible for locating a node in a graph
    based on the given coordinates (x, total_height). It allows identifying a node
    that is in proximity to the specified position by comparing
    distances between coordinates and applying a tolerance threshold based
    on the current zoom factor.
    """

    graph: Graph
    scale_offset_transformer: ScaleOffsetTransformer

    def __init__(self, graph, scale_offset_transformer):
        self.graph = graph
        self.scale_offset_transformer = scale_offset_transformer

    def find_node_at_position(self, x, y):
        # Find the node located at the given position
        for node in self.graph.nodes:
            node_x = node.x
            node_y = node.y
            # Calculate the distance between the given coordinates (x, total_height) and the node's coordinates
            distance = pygame.math.Vector2(x - node_x, y - node_y).length()
            # Check if the distance is less than a certain threshold dependent on self.scale_offset_transformer.zoom
            if distance < 8 / self.scale_offset_transformer.zoom:
                # If the distance is less, return the current node
                return node
        # If no matching node is found, return None
        return None
