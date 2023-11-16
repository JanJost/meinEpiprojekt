from abc import ABC, abstractmethod


class IDragHandler(ABC):
    @abstractmethod
    def screen_drag(self, start_drag):
        """
        Handles screen_drag interactions by updating the offset based on mouse movement.

        :param: start_drag: The initial mouse position at the start of the screen_drag.
        :return: The updated mouse position.
        """