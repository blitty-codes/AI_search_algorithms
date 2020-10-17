# when we 'podamos' what we are doing is sorting the paths where we get
# the same last node, once we have done this, we just keep the one with the
# smallest cost.
def podar(paths):
    # print('ppp', paths, 'end_name_node:', end_node)

    p = []
    new_paths = []
    total_weights = []
    count = 0

    if paths:
        for i in paths[0]:
            count += i[1]

        # (path, total weight of the path, index)
        end_less_weight = [paths[0], count, 0]
        print('end_less_weight:', end_less_weight)

        # get total path weight
        count = 0
        for i in paths:
            w = 0
            for j in i:
                w += float(j[1])
            total_weights.append((count, w))
            count += 1

        # sort by total path weight
        total_weights.sort(key=lambda x: x[1])
        print('sorted total_weights:', total_weights)

        count = 0
        # new list with the paths sorted by their total weights
        for i in total_weights:
            # set the new position to get track of it
            if i[0] == end_less_weight[2]:
                end_less_weight[2] = count
            p.append(paths[i[0]])
            count += 1

        print('SORTED PATH:', p)

        # here we make the 'podar' mode
        i = 0
        new_paths = []
        while i < len(p):
            if p[i][0][0] != paths[0][0][0]:
                new_paths.append(p[i])
            elif p[total_weights[i][0]][1][0] == end_less_weight[0][1][0]: # this case is when we found the same
                # first path, so we just append it
                new_paths.append(p[total_weights[i][0]])
            else:  # we found same end node
                # since we have the total_weights and p in the same order
                # and associated, we can use it to compare the weights
                # and append the smallest one.
                if float(total_weights[i][1]) < float(end_less_weight[1]):
                    if total_weights[0] not in new_paths:
                        new_paths.append(end_less_weight[0])
                        end_less_weight = [new_paths[i], total_weights[i][1], i]

            i += 1

        print('NEW PATHS:', new_paths)
    return new_paths
