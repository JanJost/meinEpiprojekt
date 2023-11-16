from abc import ABC, abstractmethod

from GraphModel import Node


class IGraphVisualizer(ABC):
    @abstractmethod
    def draw_graph(self):
        """
        Draws the entire graph on the Pygame screen, including edges and nodes.
        """

    @abstractmethod
    def highlight_selected_subtree(self, node: Node):
        """
        Highlights the subtree rooted at the selected node, including edges and nodes.

        :param: node (Node): The root node of the subtree to be highlighted.
        """