class Connections:
    def __init__(self, n_conn):
        self.n_conn = n_conn
        self.conn = []

    # source and target are not nodes because we just want the names
    # to them associated
    def new_connection(self, source, target, weight: float):
        self.conn.append((source, target, weight))

    def successors(self, node_name):
        succ = []
        all_conn = self.get_connections()
        for i in all_conn:
            if str(i[0]) == node_name:
                succ.append((i[1], i[2]))

        return succ

    def is_connection(self, src, target):
        try:
            self.get_src_tar().index((src, target))
            return True
        except ValueError:
            # print(f'({src}, {target}) - not in list')
            return False

    def get_connections(self):
        return self.conn

    def get_sources(self):
        src = []
        for i in self.conn:
            src.append(i[0])

        return src

    def get_targets(self):
        target = []
        for i in self.conn:
            target.append(i[1])

        return target

    def get_src_tar(self):
        src_target = []
        for i in self.conn:
            src_target.append((i[0], i[1]))

        return src_target