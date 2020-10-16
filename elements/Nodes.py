from .node import Node


class Nodes:
    def __init__(self, n_nodes, has_end=False):
        self.n_nodes = n_nodes
        self.has_end = has_end
        self.end_node = None
        self.nodes = []

    def new_node(self, node: Node, is_end=False):
        self.nodes.append(node)
        if is_end and not self.has_end:
            self.set_has_end()
            self.end_node = node

    def new_end(self, new_end: Node):
        i = j = 0
        while i < self.n_nodes and str(self.nodes[i].get_name()) != str(new_end):
            i += 1
        while j < self.n_nodes and str(self.nodes[j].get_name()) != str(self.end_node.get_name()):
            j += 1

        # the new end node
        heuristic = self.nodes[i].get_heuristic()

        if j == self.n_nodes and str(self.nodes[j-1].get_name()) != str(self.end_node):
            j -= 1

        # change with the last end node
        self.nodes[j].set_heuristic(heuristic)
        self.nodes[i].set_heuristic(0)

        self.end_node = self.nodes[i]

    def get_nodes(self) -> [Node]:
        return [self.nodes[i].get_attribs() for i in range(self.n_nodes)]

    def get_node_names(self) -> []:
        return [self.nodes[i].get_name() for i in range(self.n_nodes)]

    def get_end_node(self):
        return self.end_node

    def set_has_end(self):
        self.has_end = True

    def get_has_end(self):
        return self.has_end
