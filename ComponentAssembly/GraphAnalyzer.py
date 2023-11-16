class GraphAnalyzer:
    """
    Class to analyze a given graph.
    """

    def __init__(self):
        """
        Initializes the GraphAnalyzer with a given Graph object.
        """

    def __count_nodes(self, graph):
        """
        Counts the number of nodes in the graph.
        """
        return len(graph.nodes)

    def __count_characters(self, graph):
        """
        Counts the total number of characters in the description and title of each node.
        """
        total_characters = 0
        for node in graph.nodes:
            total_characters += len(node.description) + len(node.titel)
        return total_characters

    def display_statistics(self, graph):
        """
        Prints the number of nodes and the total number of characters.
        """
        print(f"Anzahl der Knoten: {self.__count_nodes(graph)}")
        print(f"Gesamtanzahl der Zeichen in Beschreibungen und Titeln: {self.__count_characters(graph)}")
