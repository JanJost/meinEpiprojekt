import pygame

from View.GraphView import IScaleOffsetTransformer
from GraphController.ScreenDragHandler.IScreenDragHandler import IDragHandler


class ScreenDragHandler(IDragHandler):
    """
    The ScreenDragHandler class is responsible for managing the dragging interaction on the screen in a graph visualization tool.
    It works in conjunction with the IScaleOffsetTransformer to update the view based on user interaction, specifically by
    handling the drag-and-drop movement of the graph's view. This class is crucial for providing a smooth and responsive user
    experience in navigating large graphs.
    """

    scaleOffsetTransformer: IScaleOffsetTransformer

    def __init__(self, scale_offset_transformer: IScaleOffsetTransformer):
        """
        Initializes a ScreenDragHandler instance with a scale and offset transformer.

        :param: scale_offset_transformer: An instance of IScaleOffsetTransformer which is responsible for scaling and
                                         transforming the graph view based on user interactions.
        """
        self.scaleOffsetTransformer = scale_offset_transformer

    def screen_drag(self, start_drag):
        """
        Handles the screen drag interaction. This method updates the graph's view offset based on the change in
        mouse position during a drag action, allowing the user to navigate around the graph by clicking
        and dragging the view.

        :param: start_drag: A tuple containing the x and y coordinates of the initial mouse position at the start
        of the drag.
        :return: The updated mouse position after the drag.
        """
        prev_drag_pos = start_drag
        updated_drag = pygame.mouse.get_pos()
        dx, dy = updated_drag[0] - prev_drag_pos[0], updated_drag[1] - prev_drag_pos[1]
        self.scaleOffsetTransformer.increase_offset_by(dx, dy)
        return updated_drag
