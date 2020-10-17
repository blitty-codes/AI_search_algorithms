# start: node name
# end: node name
# conn: all the connections
import elements.Connections as Connections


def expansion(current_path, successors):
    new = []
    print('successors:', successors)
    for i in successors:
        if i[0] not in current_path[0]:
            new.append([i] + current_path)

    return new


# range search algorithm gives you the first path that is find but
# the difference between deep one is that searches on a range form,
# as it's name is, to be more concrete, this one explores all the
# possibilities after going to (think of a tree) the next level
# https://miro.medium.com/max/2496/1*9BDPv_CI_7vJMGquYTQoOQ.png

def range_search(start, end, conn: Connections):
    # new_path is a List where all the paths will be stored
    paths = [[(start, 0)]]
    total_weight = 0
    # same as deep_range explanation
    # continue while we have no path and the current last node from path is not end
    # paths[0][0][0] reference to [[()]] the first one is to choose the first path
    # the second one refers to the last node in the list, and the third refers to
    # the node name, because de [1] ([0][0][1]) means that we are getting the weight
    # from the last node to this one
    while paths != [] and paths[0][0][0] != end:
        print('paths:', paths)
        exp = expansion(paths[0], conn.successors(paths[0][0][0]))
        paths = paths[1:] + exp # difference with deep_search

    if paths:
        for i in paths[0]:
            total_weight += float(i[1])

    return (list(reversed(paths[0])), total_weight) if paths != [] else None
