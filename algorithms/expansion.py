def expansion(current_path, successors):
    new = []
    successors_names = [i[0] for i in successors]
    current_path_names = [i[0] for i in current_path]

    print('successors:', successors)

    # search if in successors we have a node that has been
    # already visited on the current_path, so we search
    # by the names of the nodes
    for i in range(len(successors_names)):
        if successors_names[i] not in current_path_names:
            new.append([successors[i]] + current_path)

    print('successors_new:', new)

    return new