import networkx as nx
import matplotlib.pyplot as plt

from elements.Connections import Connections

def plot_graph(conn: Connections):
    G = nx.MultiDiGraph()
    G.add_weighted_edges_from(conn)
    pos = nx.spring_layout(G)
    labels = dict([((u, v,), w) for (u, v, w) in conn])

    nx.draw_networkx(G, pos, with_labels=True,
                     node_color="turquoise", node_size=1500,
                     arrows=True, connectionstyle='arc3, rad = 0.1')
    nx.draw_networkx_edge_labels(G, pos, labels, font_weight='light', label_pos=0.3)

    plt.show()