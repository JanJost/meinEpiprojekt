import json
import tkinter as tk
from tkinter import filedialog

from ComponentAssembly.GraphAnalyzer import GraphAnalyzer
from GraphModel.Graph import Graph
from GraphModel.Node import Node
import os
import zipfile


class GraphImporter:
    """
    The GraphImporter class is responsible for importing graph data from external sources into the application.
    It supports importing graph data, including node details and connections, from a ZIP file, which may also
    contain related image files. The class handles the extraction and processing of this data, converting it
    into a usable graph structure within the application. It integrates closely with GraphAnalyzer for post-import
    analysis and verification of the graph structure.
    """
    def __init__(self, graph: Graph, resources_folder_path, graph_analyzer: GraphAnalyzer):
        """
        Initializes the GraphImporter with a specific graph, a path to the resources folder, and a graph analyzer.

        :param: graph: An instance of the Graph class, representing the graph data structure into which the imported
        data will be loaded.
        :param: resources_folder_path: A string representing the path to the folder where resources, such as images,
        are to be stored.
        :param: graph_analyzer: An instance of GraphAnalyzer, used to analyze the graph post-import.
        """
        self.graph = graph
        self.image_folder_path = os.path.join(resources_folder_path, "Images")
        self.graph_analyzer = graph_analyzer

    def import_graph(self):
        """
        Imports graph data from a selected ZIP file. The method opens a file dialog for the user to choose the ZIP file.
        It then extracts and processes the contents of the file, including images and JSON data, to reconstruct the graph.
        Post-import, it also uses GraphAnalyzer to provide statistics about the newly imported graph.
        """
        self.graph.nodes.clear()
        root = tk.Tk()
        root.withdraw()
        zip_file_path = filedialog.askopenfilename(filetypes=[("ZIP files", "*.zip")])
        if zip_file_path:
            with zipfile.ZipFile(zip_file_path, 'r') as zipf:
                # Bilder zuerst extrahieren und dabei Namen prüfen und speichern
                image_name_mapping = self.extract_and_rename_images(zipf)

                # Namen der JSON-Datei aus dem ZIP-Dateinamen ableiten
                json_file_name = os.path.basename(zip_file_path).replace('.zip', '.json')

                if json_file_name in zipf.namelist():
                    zipf.extract(json_file_name)
                    with open(json_file_name, 'r') as file:
                        graph_data = json.load(file)
                    os.remove(json_file_name)  # Temporäre JSON-Datei löschen

                    # Graph aus der JSON-Datei erstellen
                    self.create_graph_from_json(graph_data, image_name_mapping)

    def extract_and_rename_images(self, zipf):
        """
        Extracts and renames images from the ZIP file. If an image with the same name already exists in the target folder,
        it is renamed to avoid conflicts. This method returns a mapping of original to new image names.

        :param: zipf: The opened ZIP file object from which images are to be extracted.
        :return: A dictionary mapping original image names to new names (if renamed).
        """
        os.makedirs(self.image_folder_path, exist_ok=True)
        image_name_mapping = {}
        for file in zipf.namelist():
            if file.endswith(('.png', '.jpg', '.jpeg')):
                original_image_name = file
                final_image_name = file
                original_image_path = os.path.join(self.image_folder_path, file)
                if os.path.exists(original_image_path):
                    final_image_name = self.graph.team_name + "_" + file
                final_image_path = os.path.join(self.image_folder_path, final_image_name)
                with open(final_image_path, 'wb') as f_out:
                    f_out.write(zipf.read(file))
                if original_image_name != final_image_name:
                    image_name_mapping[original_image_name] = final_image_name
        return image_name_mapping

    def create_graph_from_json(self, graph_data, image_name_mapping):
        """
        Creates a graph from JSON data. This method processes the JSON data structure to reconstruct the graph,
        including nodes and their connections. It also updates image names based on the mapping provided from
        the image extraction process.

        :param: graph_data: A dictionary containing the graph data extracted from the JSON file.
        :param: image_name_mapping: A dictionary mapping original image names to new names.
        """
        graph = Graph()
        graph.team_name = graph_data.get("team_name", "Standardteamname")
        nodes = {}
        for node_data in graph_data["nodes"]:
            image_name = node_data["image_name"]
            # Update image_name if it's in the mapping
            if image_name in image_name_mapping:
                image_name = image_name_mapping[image_name]

            node = Node(
                node_data["description"],
                node_data["titel"],
                image_name,
                node_data["x"],
                node_data["y"],
            )
            node.uuid = node_data["uuid"]
            nodes[node.uuid] = node
            graph.nodes.append(node)

        for node_data in graph_data["nodes"]:
            for connected_uuid in node_data["connected_nodes"]:
                nodes[node_data["uuid"]].connect(nodes[connected_uuid])

        self.graph = graph
        self.graph_analyzer.display_statistics(graph)
