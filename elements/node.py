class Node:
    def __init__(self, name, heuristic, is_end=False):
        self.name = name
        self.heuristic = heuristic
        self.is_end = is_end

    def get_name(self):
        return self.name

    def get_heuristic(self):
        return self.heuristic

    def set_heuristic(self, heuristic):
        self.heuristic = heuristic

    def get_is_end(self):
        return self.is_end

    def get_attribs(self) -> (any, float):
        return self.name, self.heuristic
