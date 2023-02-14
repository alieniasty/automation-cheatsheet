import argparse

import json

import networkx as nx
import matplotlib.pyplot as plt


if __name__ == "__main__":
    try:
        with open("topology.json", "r") as file:
            graph_data = json.load(file)

        G = nx.DiGraph()

        for resource in graph_data["resources"]:
            G.add_node(resource["name"])

            for association in resource["associations"]:
                G.add_edge(resource["name"], association["name"])

        plt.clf()
        pos = nx.kamada_kawai_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight='bold')

        labels = nx.get_edge_attributes(G, 'name')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.axis("off")

        plt.savefig('topology.png', dpi=200)
    except:
        print("Error")
        raise
