import numpy as np
import networkx as nx
from baseBuilder import baseBuilder

class GPglobal(baseBuilder):
    def __init__(self):
        super().__init__()

    def ccrm(self, centrality_measure):
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

        # Determine the number of nodes to keep (top 20%)
        num_nodes_to_keep = int(0.2 * len(sorted_nodes))

        # Remove nodes from the graph
        nodes_to_remove = sorted_nodes[num_nodes_to_keep:]
        print(nodes_to_remove)
        self.graph.remove_nodes_from(nodes_to_remove)

if __name__ == "__main__":
    # Example usage

    """
    npoints = 100
    data = np.random.rand(npoints, 2)
    processor = GraphProcessor()
    processor.build_graph(data)
    processor.ccrm("page_rank")
    graph = processor.get_graph()
    print("Edges in the graph after removing nodes:", graph.edges())
    """