import numpy as np
import networkx as nx
from sklearn.metrics import pairwise_distances

class baseBuilder:
    def __init__(self):
        self.graph = nx.Graph()

    def build_graph(self, data):
        """
        Input: data including features and labels, labels are stored, graph is built
        Output: None
        """

        self.features, self.labels = data[:,:-1], data[:,-1]
        # Calculate pairwise distances
        distances = pairwise_distances(self.features)
        mean_distance = np.mean(distances)
        num_samples = self.features.shape[0]

        # Add nodes to the graph
        self.graph.add_nodes_from(range(num_samples))

        # Connect samples whose distance is below the mean pairwise distance
        for i in range(num_samples):
            for j in range(i + 1, num_samples):
                if distances[i, j] < mean_distance:
                    self.graph.add_edge(i, j)

    def get_graph(self):
        return self.graph

if __name__ == "__main__":
    # Example usage
    data = np.array([[0, 0,'A'], [1, 1, 'A'], [2, 2, 'B'], [3, 3,'B'], [4, 4,'B']])
    graph_builder = baseBuilder()
    graph_builder.build_graph(data)
    graph = graph_builder.get_graph()
    print("Edges in the graph:", graph.edges())
