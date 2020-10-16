# start: node name
# end: node name
# conn: all the connections
import elements.Connections as Connections


def expansion(current_path, successors):
    new = []
    for i in successors:
        if i not in current_path:
            new.append([i] + current_path)

    return new


# deep search algorithm gives you the first path that is find
def range_search(start, end, conn: Connections):
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
        x = conn.successors(paths[0][0][0])
        print(f'successors of {paths[0][0][0]}: f{x}')
        exp = expansion(paths[0], x)
        paths = paths[1:] + exp

    if paths:
        for i in paths[0]:
            total_weight += float(i[1])

    return (list(reversed(paths[0])), total_weight) if paths != [] else None
