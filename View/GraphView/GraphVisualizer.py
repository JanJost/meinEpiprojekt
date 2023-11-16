from collections import deque

import pygame

from GraphModel import Node, Graph, SelectedNodeContainer
from View.GraphView import IScaleOffsetTransformer
from View.GraphView.IGraphVisualizer import IGraphVisualizer


class GraphVisualizer(IGraphVisualizer):
    """
    The GraphVisualizer class is responsible for rendering a graph onto a screen using Pygame.
    It manages the drawing of nodes and edges and handles the visual representation of the graph,
    including highlighting selected nodes and their subtrees.
    """
    scaleOffsetTransformer: IScaleOffsetTransformer
    selectedNodeContainer: SelectedNodeContainer
    graph: Graph
    screen = None
    edge_color = (0, 0, 0)
    node_color = (0, 0, 0)
    selected_node_color = (0, 0, 0)
    selected_node_subtree_color = (0, 0, 0)
    BASE_NODE_DIAMETER = 5
    BASE_NODE_HIGHLIGHT_DIAMETER = 8

    def __init__(self, scale_offset_transformer: IScaleOffsetTransformer,
                 screen, graph: Graph, selected_node_container: SelectedNodeContainer,
                 edge_color, node_color, selected_node_color, selected_node_subtree_color):
        """
        Initializes the GraphVisualizer with necessary components and visual properties.

        :param: scale_offset_transformer: An instance of IScaleOffsetTransformer for coordinate scaling and transformation.
        :param: screen: The Pygame screen object where the graph will be drawn.
        :param: graph: The graph to be visualized.
        :param: selected_node_container: A container holding the currently selected node, if any.
        :param: edge_color: The color to be used for drawing graph edges.
        :param: node_color: The color to be used for drawing nodes.
        :param: selected_node_color: The color to be used for highlighting the selected node.
        :param: selected_node_subtree_color: The color to be used for highlighting the subtree of the selected node.
        """

        self.scaleOffsetTransformer = scale_offset_transformer
        self.graph = graph
        self.selectedNodeContainer = selected_node_container
        self.screen = screen

        self.edge_color = edge_color
        self.node_color = node_color
        self.selected_node_color = selected_node_color
        self.selected_node_subtree_color = selected_node_subtree_color

    def draw_graph(self):
        """
        Renders the graph on the screen, drawing both nodes and edges.
        This method also handles the highlighting of the selected node and its subtree if applicable.
        """
        # Zeichne Kanten
        for node in self.graph.nodes:
            for connected_node in node.get_connected_nodes().values():
                scaled_start = self.scaleOffsetTransformer.get_scaled_coordinates(node)
                scaled_end = self.scaleOffsetTransformer.get_scaled_coordinates(connected_node)
                pygame.draw.line(self.screen, self.edge_color, scaled_start, scaled_end)

        if self.selectedNodeContainer.selected_node is not None:
            self.highlight_selected_subtree(self.selectedNodeContainer.selected_node)

        # Zeichne Knoten
        for node in self.graph.nodes:
            scaled_x, scaled_y = self.scaleOffsetTransformer.get_scaled_coordinates(node)
            pygame.draw.circle(self.screen, self.node_color, (scaled_x, scaled_y), self.BASE_NODE_DIAMETER)

    def highlight_selected_subtree(self, node: Node):
        """
        Highlights the subtree rooted at a specified node. This method visually differentiates
        the selected node and its connected nodes from the rest of the graph.

        :param: node: The root node of the subtree to be highlighted.
        """
        if node is None:
            return

        stack = deque()
        stack.append(node)

        visited_nodes = set()

        while stack:
            current_node = stack.pop()
            scaled_start = self.scaleOffsetTransformer.get_scaled_coordinates(current_node)
            pygame.draw.circle(self.screen, self.selected_node_color, scaled_start, self.BASE_NODE_HIGHLIGHT_DIAMETER)

            visited_nodes.add(current_node)

            for connected_node in current_node.get_connected_nodes().values():
                scaled_end = self.scaleOffsetTransformer.get_scaled_coordinates(connected_node)
                pygame.draw.line(self.screen, self.selected_node_subtree_color, scaled_start, scaled_end)

                if connected_node not in visited_nodes:
                    stack.append(connected_node)

        """
        for connected_node in node.get_connected_nodes().values():
            scaled_start = self.scale_offset_transformer.get_scaled_coordinates(node)
            scaled_end = self.scale_offset_transformer.get_scaled_coordinates(connected_node)
            pygame.draw.line(self.screen, self.selected_node_subtree_color, scaled_start, scaled_end)
            self.highlight_selected_subtree(connected_node)
        scaled_x, scaled_y = self.scale_offset_transformer.get_scaled_coordinates(node)
        pygame.draw.circle(self.screen, self.selected_node_color, (scaled_x, scaled_y), 8)
        """
