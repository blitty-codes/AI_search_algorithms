class Connections:
    def __init__(self, n_conn):
        self.n_conn = n_conn
        self.conn = []
        self.srcs_to_targets = []

    # source and target are not nodes because we just want the names
    # to them associated
    def new_connection(self, source, target, weight: float):
        weight = round(weight, 2)
        self.conn.append((source, target, weight))
        self.srcs_to_targets.append((source, target))

    def successors(self, node_name):
        succ = []
        all_conn = self.get_connections()
        for i in all_conn:
            if str(i[0]) == node_name:
                succ.append((i[1], i[2]))

        return succ

    def is_connection(self, src, target):
        try:
            self.srcs_to_targets.index((src, target))
            return True
        except ValueError:
            # print(f'({src}, {target}) - not in list')
            return False

    def get_connections(self):
        return self.conn
