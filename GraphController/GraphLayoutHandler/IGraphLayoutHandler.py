from abc import ABC, abstractmethod


class IGraphLayoutHandler(ABC):
    @abstractmethod
    def auto_layout(self, pause_layout):
        """
        Performs automatic layout for graphs.

        :param: pause_layout (bool): A flag indicating whether layout should be paused.
        """

    @abstractmethod
    def show_barnes_hut_area(self):
        """
        Request a visualisation of the Barnes Hut Areas.
        """