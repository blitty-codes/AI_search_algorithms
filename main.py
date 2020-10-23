# this graph is use for visualizing graph
from multiprocessing import Process

import elements.Connections as Connections
import elements.Nodes as Nodes

from algorithms.plot_graph import plot_graph

from options.use_algorithms import use_algorithms
from options.graph_generator import graph_generator


if __name__ == '__main__':
    print('Steps:')
    print('1. Create Graph\n2. Test Algorithm/solve problem\n')
    print('###### Graph ######')
    print('#    1. Random    #')
    print('#    2. Input     #')
    print('###################')

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
    if not n_conn < n_nodes * (n_nodes - 1):
        n_conn = n_nodes * (n_nodes - 1)

    nodes = Nodes.Nodes(n_nodes)
    conn = Connections.Connections(n_conn)

    graph_generator(numb, n_nodes, n_conn, nodes, conn)

    print('(Node, Heuristic):', nodes.get_nodes())
    print('(Source, Target, Weight):', conn.get_connections())
    print()

    opt = input('Print graph with weights? (0 false, 1 true): ')
    opt = int(opt) if opt != '' else 0

    p = Process(target=plot_graph, args=(conn.conn, opt,), daemon=False)
    p.start()

    print('######### Algorithm #########')
    print('#    1. deep_search         #')
    print('#    2. range_search        #')
    print('#    3. hill_climbing       #')
    print('#    4. first the better    #')
    print('#    5. branch & bound      #')
    print('#    6. A*                  #')
    print('#############################')

    use_algorithms(conn, nodes)
