# this graph is use for visualizing graph
# from graph.Graph import Graph

import random
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
    n_nodes = int(input('Number of nodes: '))
    n_conn = int(input('Number of connections: '))

    # validate n_conn < 2^size or if size <=2 and >= 0 then we get (1 << n_conn-1)
    # for a graph of 4 nodes we have 3 connections in each -> 4*3 = 12
    # when we have this graphs, we ha to think that the total maximum we want is
    # without the reflexive connections, so we have that for a graph of nodes N
    # we got the connections from the graph N-1 (the new connections to be generated) * N
    # (the number of nodes)
    if not n_conn < n_nodes*(n_nodes-1):
        n_conn = n_nodes*(n_nodes-1)

    nodes = Nodes.Nodes(n_nodes)
    conn = Connections.Connections(n_conn)

    if numb == 1:
        typeT = int(input('\n1. Heuristics\n2. No Heuristics\nType graph: '))

        if typeT == 1:
            # generate random heuristics nodes
            for i in range(n_nodes):
                nodes.new_node(Node.Node(i + 1, round(random.uniform(0, 2), 2)))
        else:
            # generate random heuristics nodes
            for i in range(n_nodes):
                nodes.new_node(Node.Node(i + 1, 0))

        # if we get all type of possibilities then we just have to create them
        if n_conn >= n_nodes:
            print('Generating all connections... (if have wait an amount of time, please restart)')
            print(n_conn)
            i = j = 0
            for i in range(n_nodes):
                j = i + 1
                while j < n_nodes:
                    conn.new_connection(nodes.get_node_names()[i],
                                        nodes.get_node_names()[j],
                                        round(random.uniform(0, 3), 2))
                    conn.new_connection(nodes.get_node_names()[j],
                                        nodes.get_node_names()[i],
                                        round(random.uniform(0, 3), 2))
                    j += 1

        else:
            print('Creating a random graph... (if have wait an amount of time, please restart)')
            # first element
            i = 0
            while i < 1:
                src_rnd = random.randint(0, n_nodes-1)
                tar_rnd = random.randint(0, n_nodes-1)
                if src_rnd != tar_rnd:
                    conn.new_connection(nodes.get_node_names()[src_rnd],
                                        nodes.get_node_names()[tar_rnd],
                                        round(random.uniform(0, 3), 2))
                    i += 1

            while i < n_conn:
                src_rnd = random.randint(0, n_nodes-1)
                tar_rnd = random.randint(0, n_nodes-1)

                # no reflexive connections and no repeat connections (1, 2) != (2, 1)
                if src_rnd != tar_rnd and not conn.is_connection(nodes.get_node_names()[src_rnd], nodes.get_node_names()[tar_rnd]):
                    conn.new_connection(nodes.get_node_names()[src_rnd],
                                        nodes.get_node_names()[tar_rnd],
                                        round(random.uniform(0, 3), 2))
                    i += 1

    elif numb == 2:
        print('INFO:\n\t- For a non informative graph, use no heuristics.\n\t- Remember that the final node needs '
              'heuristic 0.\n\t- Remember to always input 2 (node_name float).\n\t- Node name can be an int'
              '\n\t- Remember to always input 3 (node_name node_name float).\n------------------------------\n')

        # get nodes and heuristic
        for i in range(n_nodes):
            sources, heuristics = input(f'Number: {i} - (Node Heuristic): ').split()
            nodes.new_node(Node.Node(sources, heuristics))
        print(nodes.get_node_names())

        # connection between nodes
        for i in range(n_conn):
            # source, target, weight
            s, t, w = input(f'Number: {i} - (Source Target Weight): ').split()
            conn.new_connection(s, t, w)

    else:
        print('Try again later with another option...')

    print(nodes.get_nodes())
    print(conn.get_connections())
