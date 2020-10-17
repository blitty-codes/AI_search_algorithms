import elements.Connections as Connects
import elements.Nodes as Nodes
from algorithms.deep_search import deep_search
from algorithms.range_search import range_search
from algorithms.hill_climbing import hill_climbing
from algorithms.branch_bound import branch_bound

def use_algorithms(opt_al, cons: Connects, nodes: Nodes):
    global al
    print(f'The end node is: {nodes.get_end_node().get_name()}. Do you want it?'
          if nodes.get_has_end() else 'No end node applied, please give a new end node')
    end = input('(if there is no end node or you want another): ')
    if end == '':
        end = nodes.get_end_node().get_name()
    else:
        nodes.new_end(end)

    start = input('The start node: ')

    opt_al = int(opt_al)
    if opt_al == 1:
        al = deep_search(start, end, cons)
    elif opt_al == 2:
        al = range_search(start, end, cons)
    elif opt_al == 3:
        al = hill_climbing(start, end, cons, nodes.get_nodes())
    elif opt_al == 4:
        al = branch_bound(start, end, cons)

    print('al:', al)
    print('end:', end)

    if al is not None:
        node_path = []
        for i in al[0]:
            node_path.append(i[0])

        print(f'Path from {start} to {end}: {str(node_path)}')
        print(f'it\'s wight is: {al[1]}')

        if len(al) == 3:
            print(f'it\'s total heuristic is: {al[2]}')

    else:
        print('No path found!')