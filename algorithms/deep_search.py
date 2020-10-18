# start: node name
# end: node name
# conn: all the connections
import elements.Connections as Connections
from algorithms.expansion import expansion


# deep search algorithm gives you the first path that is find
def deep_search(start, end, conn: Connections):
    # new_path is a List where all the paths will be stored
    paths = [[(start, 0)]]
    total_weight = 0
    # continue while we have no path and the current last node from path is not end
    # paths[0][0][0] reference to [[()]] the first one is to choose the first path
    # the second one refers to the last node in the list, and the third refers to
    # the node name, because de [1] ([0][0][1]) means that we are getting the weight
    # from the last node to this one
    while paths != [] and paths[0][0][0] != end:
        print('paths:', paths)
        exp = expansion(paths[0], conn.successors(paths[0][0][0]))
        paths = exp + paths[1:]

    if paths:
        for i in paths[0]:
            total_weight += float(i[1])

    return (list(reversed(paths[0])), total_weight) if paths != [] else None
