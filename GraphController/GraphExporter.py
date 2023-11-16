import json
import tkinter as tk
from tkinter import filedialog
from GraphModel import Graph
import os
import zipfile


class GraphExporter:
    """
    The GraphExporter class is responsible for exporting the data of a graph into different formats.
    This includes gathering all relevant information from the Graph object, such as node details and
    connections, and then saving this data into a file. The class supports exporting to various formats,
    including JSON and ZIP, allowing for easy sharing and storage of graph data. It also handles
    the inclusion of associated image files in the export, ensuring a complete representation of the graph.
    """

    def __init__(self, graph: Graph, resources_folder_path):
        """
        Initializes the GraphExporter with a specific graph and a path to the resources folder.

        :param: graph: An instance of the Graph class, representing the graph data structure to be exported.
        :param: resources_folder_path: A string representing the path to the folder where resources, such as images,
        are stored.
        """
        self.graph = graph
        self.image_folder_path = os.path.join(resources_folder_path, "Images")

    def export_graph(self):
        """
        Exports the graph data to a file. The method allows the user to choose the file format and save location
        through a file dialog. It supports exporting the graph data as a JSON file and as a ZIP file, which includes
        the JSON data and associated images. The function handles the creation of the JSON data structure, the
        saving of the file, and the management of the ZIP archive.
        """
        # Prepare graph data for export
        graph_data = {
            "team_name": self.graph.team_name,  # Adding the team name
            "nodes": [
                {
                    "uuid": str(node.uuid),
                    "description": node.description,
                    "titel": node.titel,
                    "x": node.x,
                    "y": node.y,
                    "image_name": node.image_name,
                    "connected_nodes": [str(uuid) for uuid in node.get_connected_nodes()]
                } for node in self.graph.nodes
            ]
        }

        # Initialize file dialog for saving the file
        root = tk.Tk()
        root.withdraw()

        # Uncomment to enable JSON export
        # Export to JSON
        # file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        # if file_path:
        #     with open(file_path, 'w') as file:
        #         json.dump(graph_data, file)

        # Export to ZIP
        file_path = filedialog.asksaveasfilename(defaultextension=".zip", filetypes=[("ZIP files", "*.zip")])
        if file_path:
            with zipfile.ZipFile(file_path, 'w') as zipf:
                # Add JSON file to ZIP
                json_path = file_path.replace('.zip', '.json')
                with open(json_path, 'w') as file:
                    json.dump(graph_data, file)
                zipf.write(json_path, os.path.basename(json_path))
                os.remove(json_path)  # Delete temporary JSON file

                # Add images to ZIP
                for image in os.listdir(self.image_folder_path):
                    zipf.write(os.path.join(self.image_folder_path, image), image)

