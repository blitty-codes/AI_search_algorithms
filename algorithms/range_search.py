# start: node name
# end: node name
# conn: all the connections
import elements.Connections as Connections
from algorithms.expansion import expansion


# range search algorithm gives you the first path that finds but
# the difference with deep one is that searches on a range form,
# as it's name says, to be more concrete, this one explores all the
# possibilities after going to (think of a tree) the next level
# https://miro.medium.com/max/2496/1*9BDPv_CI_7vJMGquYTQoOQ.png

def range_search(start, end, conn: Connections):
    # new_path is a List where all the paths will be stored
    paths = [[(start, 0)]]
    total_weight = 0
    # same as deep_range explanation

    while paths != [] and paths[0][0][0] != end:
        # print('paths:', paths)
        exp = expansion(paths[0], conn.successors(paths[0][0][0]))
        paths = paths[1:] + exp  # difference with deep_search

    if paths:
        for i in paths[0]:
            total_weight += float(i[1])

    return (list(reversed(paths[0])), total_weight) if paths != [] else None
