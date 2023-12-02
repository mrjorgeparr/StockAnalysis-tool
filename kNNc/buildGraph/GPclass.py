import numpy as np
import networkx as nx
from sklearn.metrics import pairwise_distances
from baseBuilder import baseBuilder

class GPclass(baseBuilder):
    def __init__(self):
        super().__init__()

    def ccrm(self, centrality_measure, data, *, VERBOSE=False, plot=False):

        if centrality_measure not in ["page_rank", "betweenness", "closeness", "degree", "eigenvector"]:
            raise ValueError("Invalid centrality measure")
        
        self.build_graph(data)
        class_labels = data[:,-1]

        centrality = {      
            "page_rank": nx.pagerank,
            "betweenness": nx.betweenness_centrality,
            "closeness": nx.closeness_centrality,
            "degree": nx.degree_centrality,
            "eigenvector": nx.eigenvector_centrality,
        }

        centrality_values = centrality[centrality_measure](self.graph)
        # print(f"Centrality values found: {centrality_values}")
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
            if VERBOSE:
                print(f"Removed nodes class {target_class}: {class_nodes[num_nodes_to_keep:]}")
        print(f"Length: {len(nodes_to_remove)}")
        # print(len(nodes_to_remove))
        self.graph.remove_nodes_from(nodes_to_remove)
        if plot: 
            self.plot_graph(title='Filtered graph')



if __name__ == "__main__":

# Sample data with features and class labels
    npoints = 40
    data = np.random.rand(npoints, 3)
    for i in range(40):
        if i // 2 == 0:
            data[i,2] = 1
        else:
            data[i,2] = 2
    processor = GPclass()
    processor.ccrm("betweenness", data, VERBOSE=True)
    graph = processor.get_graph()
    print("Edges in the graph after removing nodes:", graph.edges())