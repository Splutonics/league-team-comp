import json
import networkx as nx
import matplotlib.pyplot as plt

# https://www.askpython.com/python-modules/networkx-package
# from DF https://www.askpython.com/python/examples/creating-weighted-graph-dataframe

# TODO import all champs

# wins_lane = 0
# loses_lane = 1
# best_with = 2
# wins_more_against = 3
# loses_more_against = 4

# TODO add each champ as a node to a graph

G = nx.DiGraph()
# or
G = nx.Graph()


# TODO add each data point as an edge between champs
# ? one way relationships (synergies) should be digraphs
# ? two way relationships (losing lane) should be a graph


# TODO visualize graph

# TODO for synergies, evaluate modularity of relationships
# https://stackoverflow.com/questions/29897243/graph-modularity-in-python-networkx
# https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.community.quality.modularity.html
