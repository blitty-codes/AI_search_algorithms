# podar_by_func does the same as podar but, here what we want to
# delete not only by the total weight, but algo by the heuristics,
# so the function is: f(n) = weight(n) + heuristic(n)


def podar_by_func(paths):
    p = []
    new_paths = []
    total_w_and_h = []

    if paths:
        f = 0
        # the first element is special
        for i in paths[0]:
            f += float(i[1]) + float(i[2])

        # (path, total heuristic of the path + total weight of the path, index)
        end_less_weight = [paths[0], f, 0]
        # print('end_less_weight:', end_less_weight)

        # get total path weight+heuristic
        pos = 0
        for i in paths:
            f = 0
            for j in i:
                f += float(j[1]) + float(j[2])
            total_w_and_h.append((pos, f))
            pos += 1

        # sort by total function
        total_w_and_h.sort(key=lambda x: x[1])
        # print('sorted total_weights:', total_weights)

        pos = 0
        # new list with the paths sorted by their total weights
        for i in total_w_and_h:
            # set new position to get track of it
            if i[0] == end_less_weight[2]:
                end_less_weight[2] = pos
            p.append(paths[i[0]])
            pos += 1

        # print('SORTED PATH:', p)

        # here we make the 'podar' mode
        i = 0
        while i < len(p):
            # if the end node from the actual path != the end node
            if p[i][0][0] != paths[0][0][0]:
                new_paths.append(p[i])
            # this case is when we found the same first path, so we just append it
            # same previous end node and same total weight, then we can say that they are the same path
            # so we just append one of them
            elif p[total_w_and_h[i][0]][1][0] == end_less_weight[0][1][0] and total_w_and_h[i][1] == end_less_weight[1]:
                new_paths.append(p[total_w_and_h[i][0]])
            else:  # we found same end node
                # since we have the total_weights and p in the same order
                # and associated, we can use it to compare the weights
                # and append the smallest one.
                if float(total_w_and_h[i][1]) < float(end_less_weight[1]):
                    if total_w_and_h[0] not in new_paths:
                        new_paths.append(end_less_weight[0])
                        end_less_weight = [new_paths[i], total_w_and_h[i][1], i]

            i += 1

        # print('NEW PATHS:', new_paths)
    return new_paths
