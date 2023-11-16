from GraphModel import Node


class SelectedNodeContainer:
    """
    The SelectedNodeContainer class acts as a container for storing and managing the currently selected node in a graph.
    This class is particularly useful in user interface contexts where actions or information displayed are dependent
    on the current node selection. By encapsulating the selected node in a dedicated class, it becomes easier to manage
    and track changes to the selection state across different parts of the application.
    """

    selected_node: Node
    selected_node = None
