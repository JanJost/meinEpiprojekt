import pygame

from ComponentAssembly.IComponentProvider import IComponentProvider


class ApplicationLoopManager:
    """
    ApplicationLoopManager is responsible for managing the main loop of a graph visualization application.
    It coordinates user input handling, visual updates, and interactions with various components like the graph,
    UI elements, and event handlers. This class integrates components provided by IComponentProvider to create
    a cohesive application experience, managing everything from rendering the graph to handling user interactions.
    """

    def __init__(self, component_provider: IComponentProvider):
        """
        Initializes the ApplicationLoopManager with the necessary components from the component provider.

        :param: component_provider: An instance of IComponentProvider that provides access to essential
        application components.
        """
        self.screen = component_provider.get_screen()
        self.uiTheme = component_provider.get_ui_theme()
        self.node_details_window = component_provider.get_node_details_window()
        self.scaleOffsetTransformer = component_provider.get_scale_offset_transformer()
        self.node_finder = component_provider.get_node_finder()
        self.dragHandler = component_provider.get_drag_handler()
        self.subtree_mover = component_provider.get_subtree_mover()
        self.selectedNodeContainer = component_provider.get_selected_node_container()
        self.graphLayoutHandler = component_provider.get_graph_layout_handler()
        self.graphVisualizer = component_provider.get_graph_visualizer()
        self.main_menu = component_provider.get_main_menu()
        self.run()

    def run(self):
        """
        The main loop of the application. This method handles the flow of the application,
        including event handling, rendering, and updating the state of various components.
        It continually updates the display based on user interaction and internal state changes.
        """
        running = True
        start_screen_drag = None
        start_node_drag = None
        pause_layout = True

        while running:
            # Hintergrund zeichnen
            self.screen.fill(self.uiTheme.BACKGROUND_COLOR)

            for event in pygame.event.get():
                # Mouse Down Events
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 3:  # Right Click
                        start_screen_drag = pygame.mouse.get_pos()
                    elif event.button == 4:  # Scroll Wheel up
                        if self.node_details_window.check_text_area_collision(event):
                            self.node_details_window.scroll_up()
                        else:
                            self.scaleOffsetTransformer.increase_zoom_by()

                    elif event.button == 5:  # Scroll Wheel down
                        if self.node_details_window.check_text_area_collision(event):
                            self.node_details_window.scroll_down()
                        else:
                            self.scaleOffsetTransformer.decrease_zoom_by()

                    elif event.button == 1:  # Left Click
                        if self.node_details_window.check_scroll_necessity(event):
                            self.node_details_window.start_scrollbar_scrolling(event)

                        if not self.node_details_window.check_scrollbar_collision(event):
                            mouse_x, mouse_y = self.scaleOffsetTransformer.get_scaled_mouse_position()
                            self.selectedNodeContainer.selected_node = self.node_finder.find_node_at_position(mouse_x,
                                                                                                              mouse_y)
                            if self.selectedNodeContainer.selected_node:
                                start_node_drag = (mouse_x, mouse_y)

                # Mouse Up Events
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1 and start_node_drag:
                        start_node_drag = None
                    if event.button == 1:
                        self.node_details_window.end_scrollbar_scrolling()
                        start_node_drag = None
                    if event.button == 3:
                        start_screen_drag = None

                # Keyboard events
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if pause_layout:
                            pause_layout = False
                        else:
                            pause_layout = True
                    elif event.key == pygame.K_ESCAPE:
                        running = False

                # Scrolling via Scrollbar
                if self.node_details_window.is_drag_scrolling():
                    self.node_details_window.apply_scrollbar_scroll()

                # Screen Drag Event
                if pygame.mouse.get_pressed()[2] and start_screen_drag:
                    start_screen_drag = self.dragHandler.screen_drag(start_screen_drag)

                # Subtree Drag Event
                if pygame.mouse.get_pressed()[0] and start_node_drag:
                    mouse_x, mouse_y = self.scaleOffsetTransformer.get_scaled_mouse_position()
                    dx = mouse_x - start_node_drag[0]
                    dy = mouse_y - start_node_drag[1]
                    start_node_drag = (mouse_x, mouse_y)
                    self.subtree_mover.move_selected_node_subtree(self.selectedNodeContainer.selected_node, dx, dy)

                # Menü-Event-Handling
                self.main_menu.handle_event(event)

            # Start Auto Layout
            # self.graph_layout_handler.auto_layout(pause_layout, 0.05, 100)
            self.graphLayoutHandler.auto_layout(pause_layout)

            self.graphVisualizer.draw_graph()
            # Zeichne das Menü
            self.main_menu.draw(self.screen)

            # Show Details of selected Node
            if self.selectedNodeContainer.selected_node is not None:
                self.node_details_window.show_node_details()

            # Zeichne Barnes Hut Areas
            # self.graph_layout_handler.show_barnes_hut_area()

            # Aktualisiere das Display
            pygame.display.flip()
