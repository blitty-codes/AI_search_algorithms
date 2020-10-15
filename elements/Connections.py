class Connections:
    def __init__(self, n_conn):
        self.n_conn = n_conn
        self.conn = []

    # source and target are not nodes because we just want the names
    # to them associated
    def new_connection(self, source, target, weight: float):
        self.conn.append((source, target, weight))

    def get_connections(self):
        return self.conn
