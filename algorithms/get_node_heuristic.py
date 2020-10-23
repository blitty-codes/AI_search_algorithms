import elements.Nodes as Nodes


def get_node_heuristic(node_name, nodes: Nodes):
    i = 0
    while i < len(nodes) and str(nodes[i][0]) != str(node_name):
        i += 1

    return nodes[i][1]
