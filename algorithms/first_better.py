# start: node name
# end: node name
# conn: all the connections
import elements.Connections as Connections
import elements.Nodes as Nodes


def get_node_heuristic(node_name, nodes: Nodes):
    for i in nodes:
        if str(i[0]) == str(node_name):
            return i[1]


def sort_by_heuristic(paths):
    sort_paths = []
    if paths:
        # [position, heuristic]
        heuristic = [(i, float(paths[i][0][1])) for i in range(len(paths))]
        # print('(position, heuristic)', heuristic)
        heuristic.sort(key=lambda x: x[1])
        # sort by heuristic sort
        for i in range(len(heuristic)):
            sort_paths.append(paths[heuristic[i][0]])
        # print('new_path:', sort_paths)

    return sort_paths


def expansion_heuristic(current_path, successors, nodes: Nodes):
    new = []
    successors_names = [i[0] for i in successors]
    current_path_names = [i[0] for i in current_path]

    # print('successors:', successors)

    for i in range(len(successors_names)):
        if successors_names[i] not in current_path_names:
            heuristic = get_node_heuristic(successors_names[i], nodes)
            new.append([(successors[i][0], heuristic, successors[i][1])] + current_path)

    return new


# first the better is like the hill climbing, but we first add
# the expansion after all paths and then we sort all the paths
# by the heuristics
def first_better(start, end, conn: Connections, nodes: Nodes):
    # new_path is a list where all the paths will be stored type of the node: (node_name, heuristic, weight)
    paths = [[(start, get_node_heuristic(start, nodes), 0)]]
    total_weight = 0
    total_heuristic = 0

    while paths != [] and paths[0][0][0] != end:
        # print('paths:', paths)
        exp = expansion_heuristic(paths[0], conn.successors(paths[0][0][0]), nodes)
        paths = paths[1:] + exp
        paths = sort_by_heuristic(paths)

    if paths:
        for i in paths[0]:
            total_weight += float(i[2])
            total_heuristic += float(i[1])

    return (list(reversed(paths[0])), total_weight,  total_heuristic) if paths != [] else None
