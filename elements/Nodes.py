from .node import Node


class Nodes:
    def __init__(self, n_nodes):
        self.n_nodes = n_nodes
        self.nodes = []

    def new_node(self, node: Node):
        self.nodes.append(node)

    def get_nodes(self) -> [Node]:
        return [self.nodes[i].get_attribs() for i in range(self.n_nodes)]

    def get_node_names(self) -> []:
        return [self.nodes[i].get_name() for i in range(self.n_nodes)]
