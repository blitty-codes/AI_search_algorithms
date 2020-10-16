import random
import elements.node as Node


# if the graph has been done correctly, then it returns 0 otherwise 1

def graph_generator(numb, n_nodes, n_conn, nodes, conn):
    if numb == 1:
        typeHeu = int(input('\n1. Heuristics\n2. No Heuristics\nType graph: '))

        if typeHeu == 1:
            # end node
            nodes.new_node(Node.Node(n_nodes, 0, True), True)
            # generate random heuristics nodes
            for i in range(n_nodes-1):
                nodes.new_node(Node.Node(i + 1, round(random.uniform(0.1, 2), 2)))
        else:
            # generate random heuristics nodes
            for i in range(n_nodes):
                nodes.new_node(Node.Node(i + 1, 0))

        # if we get all type of possibilities then we just have to create them
        if n_conn >= n_nodes*(n_nodes-1):
            print('Generating all connections... (if have wait an amount of time, please restart)')
            print(n_conn)
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
                src_rnd = random.randint(0, n_nodes - 1)
                tar_rnd = random.randint(0, n_nodes - 1)
                if src_rnd != tar_rnd:
                    conn.new_connection(nodes.get_node_names()[src_rnd],
                                        nodes.get_node_names()[tar_rnd],
                                        round(random.uniform(0, 3), 2))
                    i += 1

            while i < n_conn:
                src_rnd = random.randint(0, n_nodes - 1)
                tar_rnd = random.randint(0, n_nodes - 1)

                # no reflexive connections and no repeat connections (1, 2) != (2, 1)
                if src_rnd != tar_rnd and not conn.is_connection(nodes.get_node_names()[src_rnd],
                                                                 nodes.get_node_names()[tar_rnd]):
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
            sources, heuristics = input(f'Node: {i} - (Node Heuristic): ').split()
            nodes.new_node(Node.Node(sources, heuristics), (lambda x: int(x) == 0)(float(heuristics)))
        print('Node names:', nodes.get_node_names())

        # connection between nodes
        for i in range(n_conn):
            # source, target, weight
            s, t, w = input(f'Connection: {i} - (Source Target Weight): ').split()
            conn.new_connection(s, t, w)

    else:
        print('Try again later with another option... (Restart)')
