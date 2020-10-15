# this graph is use for visualizing graph
# from graph.Graph import Graph

import elements.Connections as Connections
import elements.Nodes as Nodes
import elements.node as Node


if __name__ == '__main__':
    print('Steps:')
    print('1. Graph')
    print('##### Menu #####')
    print('#  1. Random   #')
    print('#  2. Input    #')
    print('################')

    # sources = targets = [] # integers
    # heuristics = weight = [] # float

    numb = int(input('Option: '))
    size = int(input('Size: '))

    if numb == 1:
        print('one')
    elif numb == 2:
        print('INFO:\n\t- For a non informative graph, use no heuristics.\n\t- Remember that the final node needs '
              'heuristic 0.\n\t- Remember to always input 2 (node_name float).\n\t- Node name can be an int'
              '\n\t- Remember to always input 3 (node_name node_name float).\n------------------------------\n')

        nodes = Nodes.Nodes(size)

        # get nodes and heuristic
        for i in range(size):
            sources, heuristics = input(f'Number: {i} - (Node Heuristic): ').split()
            nodes.new_node(Node.Node(sources, heuristics))
        print(nodes.get_node_names())

        n_conn = int(input('Number of connections: '))
        # print(nodes.get_node_names())

        # validate n_conn < 2^size or if size <=2 and >= 0 then we get (1 << n_conn-1)
        if size == 1:
            n_conn = 0
        elif size == 2:
            n_conn = 1
        elif not n_conn < (1 << size):
            n_conn = (1 << size)

        print('n_conn:', n_conn)
        conn = Connections.Connections(n_conn)

        # connection between nodes
        for i in range(n_conn):
            # source, target, weight
            s, t, w = input(f'Number: {i} - (Source Target Weight): ').split()
            conn.new_connection(s, t, w)

        # todo comment
        print(nodes.get_nodes())
        print(conn.get_connections())
    else:
        print('Try again later with another option...')

