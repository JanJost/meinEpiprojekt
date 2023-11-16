from abc import ABC, abstractmethod


class INodeDetailsWindow(ABC):
    @abstractmethod
    def check_text_area_collision(self, event):
        """
        Checks if an event collides with the text area.

        Args:
            event (pygame.event.Event): The event to be checked.

        Returns:
            bool: True if collision with the text area, False otherwise.
        """

    @abstractmethod
    def check_scrollbar_collision(self, event):
        """
        Checks if an event collides with the scroll bar.

        Args:
            event (pygame.event.Event): The event to be checked.

        Returns:
            bool: True if collision with the scroll bar, False otherwise.
        """

    @abstractmethod
    def check_scroll_necessity(self, event):
        """
        Checks if scrolling is necessary based on the given event.

        Args:
            event: The event that triggers the check.

        Returns:
            bool: True if scrolling is necessary, False otherwise.
        """

    @abstractmethod
    def start_scrollbar_scrolling(self, event):
        """
        Initiates scrolling when the user interacts with the scroll bar.

        Args:
            event (pygame.event.Event): The event that triggers scrolling.
        """

    @abstractmethod
    def end_scrollbar_scrolling(self):
        """
        Ends scrolling when the user releases die Scrollbar.
        """

    @abstractmethod
    def scroll_up(self):
        """
        Scrolls the text content upward.
        """

    @abstractmethod
    def scroll_down(self):
        """
        Scrolls the text content downward.
        """

    @abstractmethod
    def apply_scrollbar_scroll(self):
        """
        Applies scrolling based on user interaction.
        """

    @abstractmethod
    def show_node_details(self):
        """
        Displays the detailed information about the selected node, including scrolling functionality.
        """

    @abstractmethod
    def is_drag_scrolling(self):
        """
        Checks if drag scrolling is currently active.

        Returns:
            bool: True if drag scrolling is active, False otherwise.
        """
        pass

