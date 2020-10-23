# start: node name
# end: node name
# conn: all the connections
import elements.Connections as Connections
import elements.Nodes as Nodes
from algorithms.get_node_heuristic import get_node_heuristic


def expansion_heuristic(current_path, successors, nodes: Nodes):
    new = []
    successors_names = [i[0] for i in successors]
    current_path_names = [i[0] for i in current_path]

    # print('successors:', successors)

    # search if in successors we have a node that has been
    # already visited on the current_path, so we search
    # by the names of the nodes
    for i in range(len(successors_names)):
        if successors_names[i] not in current_path_names:
            heuristic = get_node_heuristic(successors_names[i], nodes)
            new.append([(successors[i][0], heuristic, successors[i][1])] + current_path)

    if new:
        new_path = []
        # [position, heuristic]
        heuristic = [(i, float(new[i][0][1])) for i in range(len(new))]
        # print('(position, heuristic)', heuristic)
        heuristic.sort(key=lambda x: x[1])
        # sort by heuristic sort
        for i in range(len(heuristic)):
            new_path.append(new[heuristic[i][0]])
        # print(new)
        # print('new_path:', new_path)
        return new_path

    return new


# hill_climbing is an algorithm that uses heuristics and
# takes the path which has the less heuristic node. For example:
#   Node, heuristic: (1,0.3) (2, 1) (3, 0.2)
#       1 -> 2 (heuristic of 2 is 1)
#       1 -> 3 (heuristic of 3 is 0.2)
# since 0.2 < 1 the path is going to be updated as:
# [(3, 1), (2, 1)] always the node with the less heuristic near
# is going to be the first path, and so on.

# problems of this algorithm:
#   - sensibility to heuristic (depends on the heuristic)
#   - sensibility to locals minimum (it search for minimum heuristic)

# more info found in README.md on utility
def hill_climbing(start, end, conn: Connections, nodes: Nodes):
    # new_path is a list where all the paths will be stored type of the node: (node_name, heuristic, weight)
    paths = [[(start, get_node_heuristic(start, nodes), 0)]]
    total_weight = 0
    total_heuristic = 0

    while paths != [] and paths[0][0][0] != end:
        # print('paths:', paths)
        exp = expansion_heuristic(paths[0], conn.successors(paths[0][0][0]), nodes)
        paths = exp + paths[1:]

    if paths:
        for i in paths[0]:
            total_weight += float(i[2])
            total_heuristic += float(i[1])

    return (list(reversed(paths[0])), total_weight,  total_heuristic) if paths != [] else None
