import numpy as np
import networkx as nx
from sklearn.metrics import pairwise_distances
import matplotlib.pyplot as plt


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
        self.plot_graph()


    def get_graph(self):
        return self.graph
    

    def plot_graph(self, title='Complete graph'):
        """
        Plot the built graph in an aesthetic way
        """
        pos = nx.spring_layout(self.graph)  # Set the layout algorithm (you can try different layouts)

        # Plot nodes
        nx.draw_networkx_nodes(self.graph, pos, node_size=50, node_color='skyblue', alpha=0.8)

        # Plot edges
        nx.draw_networkx_edges(self.graph, pos, width=1.0, alpha=0.5)

        # Plot labels
        nx.draw_networkx_labels(self.graph, pos, font_size=8, font_color='black')

        # Display the plot
        plt.title(title)
        plt.show()

if __name__ == "__main__":
    
    # Example usage
    npoints = 20
    data = np.random.rand(npoints, 3)
    for i in range(20):
        if i // 2 == 0:
            data[i,2] = 1
        else:
            data[i,2] = 2
    graph_builder = baseBuilder()
    graph_builder.build_graph(data)
    graph = graph_builder.get_graph()
    print("Edges in the graph:", graph.edges())
    
