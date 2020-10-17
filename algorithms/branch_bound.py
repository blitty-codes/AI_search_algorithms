# start: node name
# end: node name
# conn: all the connections
import elements.Connections as Connections
from algorithms.podar import podar


def expansion(current_path, successors):
    new = []
    print('successors:', successors)
    for i in successors:
        if i[0] not in current_path[0]:
            new.append([i] + current_path)

    return new


def branch_bound(start, end, conn: Connections):
    # new_path is a list where all the paths will be stored
    paths = [[(start, 0)]]
    total_weight = 0

    while paths != [] and paths[0][0][0] != end:
        exp = expansion(paths[0], conn.successors(paths[0][0][0]))
        paths = paths[1:] + exp  # difference with deep_search
        print('paths:', paths)
        # we do not want to give the first path because you want to 'pode'
        # from the last node of the actual path
        paths = podar(paths)
        print('paths_after:', paths)

    if paths:
        for i in paths[0]:
            total_weight += float(i[1])

    return (list(reversed(paths[0])), total_weight) if paths != [] else None
