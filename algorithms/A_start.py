import elements.Connections as Connections
import elements.Nodes as Nodes
from algorithms.podar_by_func import podar_by_func
from algorithms.get_node_heuristic import get_node_heuristic


# expansion with the heuristic added
def expansion_with_heu(current_path, successors, nodes: Nodes):
    new = []
    successors_names = [i[0] for i in successors]
    current_path_names = [i[0] for i in current_path]

    # print('successors:', successors)

    # search if in successors we have a node that has
    # already been visited on the current_path, so we
    # search by the name of the nodes
    for i in range(len(successors_names)):
        if successors_names[i] not in current_path_names:
            heuristic = get_node_heuristic(successors_names[i], nodes)
            new.append([(successors[i][0], heuristic, successors[i][1])] + current_path)

    # print('successors_new:', new)

    return new


def A_star(start, end, conn: Connections, nodes: Nodes):
    # new_path is a list where all the paths will be stored
    # (nam_node, heuristic, weight)
    paths = [[(start, get_node_heuristic(start, nodes), 0)]]
    total_weight = 0
    total_heuristic = 0

    while paths != [] and paths[0][0][0] != end:
        exp = expansion_with_heu(paths[0], conn.successors(paths[0][0][0]), nodes)
        paths = paths[1:] + exp  # difference with deep_search
        # print('paths:', paths)
        # we do not want to give the first path because you want to 'pode'
        # from the last node of the actual path
        paths = podar_by_func(paths)
        # print('paths_after:', paths)

    if paths:
        for i in paths[0]:
            total_heuristic += float(i[1])
            total_weight += float(i[2])

    return (list(reversed(paths[0])), total_weight, total_heuristic) if paths != [] else None
