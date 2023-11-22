import pygame.freetype
import sys

from GraphContent import GraphContent
from View.ApplicationLoopManager import ApplicationLoopManager
from ComponentAssembly.ComponentAssembler import ComponentAssembler
from GraphModel.Graph import Graph

if __name__ == '__main__':
    # Graph
    graph = Graph()
    graph.team_name = "Die mutigen Mungos"  # TODO: Geben Sie Ihrem Team einen Namen!
    graph_content = GraphContent(graph)  # TODO: Hier können Sie den Inhalt und Verbindungen ihrer Knoten anlegen.

    # Application
    component_assembler = ComponentAssembler(graph, True)
    main = ApplicationLoopManager(component_assembler)
    # pygame beenden
    pygame.quit()
    sys.exit()
    print("test")
