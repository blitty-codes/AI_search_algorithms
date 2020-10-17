# start: node name
# end: node name
# conn: all the connections
import elements.Connections as Connections
import elements.Nodes as Nodes


def get_node_heuristic(node_name, nodes: Nodes):
    for i in nodes:
        if i[0] is node_name:
            return i[1]


def expansion(current_path, successors, nodes: Nodes):
    new = []
    print('successors:', successors)
    # successors: [node_name, weight]
    for i in successors:
        # print('i:', i)
        if i[0] not in current_path[0]:
            heuristic = get_node_heuristic(i[0], nodes)
            new.append([(i[0], heuristic, i[1])] + current_path)

    if new:
        new_path = []
        # [position, heuristic]
        heuristic = [(i, float(new[i][0][1])) for i in range(len(new))]
        print('(position, heuristic)', heuristic)
        heuristic.sort(key=lambda x: x[1])
        # sort by heuristic sort
        for i in range(len(heuristic)):
            new_path.append(new[heuristic[i][0]])
        # print(new)
        print('new_path:', new_path)
        return new_path

    return new


# hill_climbing is an algorithm that uses heuristics and
# takes the path which less heuristic node has. For example:
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
    paths = [[(start, 0, 0)]]
    total_weight = 0
    total_heuristic = 0

    while paths != [] and paths[0][0][0] != end:
        print('paths:', paths)
        exp = expansion(paths[0], conn.successors(paths[0][0][0]), nodes)
        paths = exp + paths[1:]

    if paths:
        for i in paths[0]:
            total_weight += float(i[2])
            total_heuristic += float(i[1])

    return (list(reversed(paths[0])), total_weight,  total_heuristic) if paths != [] else None
