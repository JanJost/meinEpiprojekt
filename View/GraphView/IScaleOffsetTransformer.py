from abc import ABC, abstractmethod


class IScaleOffsetTransformer(ABC):
    @abstractmethod
    def get_scaled_coordinates(self, node):
        """
        Transforms node coordinates based on the current zoom and offset.

        :param: node (Node): The node containing coordinates to transform.

        :return: Tuple[int, int]: The transformed (scaled) x and total_height coordinates of the node.
        """

    @abstractmethod
    def get_scaled_mouse_position(self):
        """
        Returns the mouse position on the scaled plane.

        :param: Tuple[float, float]: The scaled x and total_height coordinates of the mouse position.
        """

    @abstractmethod
    def update_mouse_position(self):
        """
        Updates the scaled mouse position based on the current zoom and offset.
        """

    @abstractmethod
    def increase_zoom_by(self):
        """
        Increases the zoom factor by a specified value.

        :param: value (float): The amount by which to increase the zoom factor.
        """

    @abstractmethod
    def decrease_zoom_by(self):
        """
        Decreases the zoom factor by a specified value.

        :param: value (float): The amount by which to decrease the zoom factor.
        """

    @abstractmethod
    def increase_offset_by(self, dx, dy):
        """
        Increases the offset by specified values in the x and total_height directions.

        :param: dx (int): The amount to increase the horizontal offset.
        :param: dy (int): The amount to increase the vertical offset.
        """

    @abstractmethod
    def decrease_offset_by(self, dx, dy):
        """
        Decreases the offset by specified values in the x and total_height directions.

        :param: dx (int): The amount to decrease the horizontal offset.
        :param: dy (int): The amount to decrease the vertical offset.
        """
