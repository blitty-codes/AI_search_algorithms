class Node:
    def __init__(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic

    def get_name(self):
        return self.name

    def get_heuristic(self):
        return self.heuristic

    def get_attribs(self) -> (any, float):
        return self.name, self.heuristic
