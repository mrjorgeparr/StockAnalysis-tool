import numpy as np
import networkx as nx
from sklearn.metrics import pairwise_distances
from baseBuilder import baseBuilder

class GPclass(baseBuilder):
    def __init__(self):
        super().__init__()

    def ccrm(self, centrality_measure, class_labels):
        if centrality_measure not in ["page_rank", "betweenness", "closeness", "degree", "eigenvector"]:
            raise ValueError("Invalid centrality measure")

        centrality = {
            "page_rank": nx.pagerank,
            "betweenness": nx.betweenness_centrality,
            "closeness": nx.closeness_centrality,
            "degree": nx.degree_centrality,
            "eigenvector": nx.eigenvector_centrality,
        }

        centrality_values = centrality[centrality_measure](self.graph)
        print(f"Centrality values found: {centrality_values}")
        # Sort nodes by centrality measure
        sorted_nodes = sorted(centrality_values, key=centrality_values.get, reverse=True)

        # Access and use class labels from the input data
        class_labels = {node: class_labels[node] for node in self.graph.nodes()}

        # Initialize an empty list to store nodes to remove
        nodes_to_remove = []

        # Iterate through each class
        for target_class in np.unique(list(class_labels.values())):
            # Filter nodes belonging to the current class
            class_nodes = [node for node in sorted_nodes if class_labels[node] == target_class]
            
            # Calculate the number of nodes to keep (top 20%)
            num_nodes_to_keep = int(0.2 * len(class_nodes))
            
            # Calculate the number of nodes to remove (bottom 80%)
            num_nodes_to_remove = len(class_nodes) - num_nodes_to_keep
            
            # Add the bottom 80% of nodes to the removal list
            nodes_to_remove.extend(class_nodes[num_nodes_to_keep:])
        
        print(nodes_to_remove)
        self.graph.remove_nodes_from(nodes_to_remove)



if __name__ == "__main__":

# Sample data with features and class labels
    data = np.array([
        [0.1, 0.2, "ClassA"],
        [0.3, 0.4, "ClassB"],
        [0.5, 0.6, "ClassA"],
        [0.7, 0.8, "ClassB"],
        # Add more data points with class labels
    ])

    # Create a networkx graph from your data
    G = nx.Graph()

    # Initialize your GPglobal object
    gpClass = GPclass()

    # Set the graph in your GPglobal object
    gpClass.build_graph(data)

    # Extract class labels
    class_labels = {i: data[i, -1] for i in range(data.shape[0])}

    # Call the ccrm method with your chosen centrality measure
    gpClass.ccrm(centrality_measure="page_rank", class_labels=class_labels)