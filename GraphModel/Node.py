import uuid


class Node:
    """
    The Node class represents a single node in a graph. It encapsulates various attributes of a node,
    such as its position, image representation, and connections to other nodes. This class is fundamental
    in graph structures, providing the basic building block for representing entities within the graph.
    """
    image_name = "image_placeholder.png"

    def __init__(self, description, titel, image_name="image_placeholder.png", x=0, y=0):
        """
        Initializes a new instance of the Node class.

        :param: description: A string providing a description of the node.
        :param: titel: A string representing the title of the node.
        :param: image_name: A string specifying the filename of the image representing the node.
                           Defaults to a placeholder image.
        :param: x: The x-coordinate of the node in the graph. Defaults to 0.
        :param: y: The y-coordinate of the node in the graph. Defaults to 0.
        """
        self.uuid = uuid.uuid4()
        self.description = description
        self.titel = titel
        self.x = x
        self.y = y
        self.__connected_nodes = {}
        self.disp_x = 0
        self.disp_y = 0
        self.mass = 1
        self.velocity_x = 0.0
        self.velocity_y = 0.0
        self.acceleration_x = 0.0
        self.acceleration_y = 0.0
        self.image_name = image_name

    def connect(self, other_node):
        if other_node.uuid not in self.__connected_nodes:
            self.__connected_nodes[other_node.uuid] = other_node

    def get_connected_nodes(self):
        return self.__connected_nodes
