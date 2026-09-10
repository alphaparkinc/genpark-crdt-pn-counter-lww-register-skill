class PNCounter:
    """
    CRDT PN-Counter (Positive-Negative Counter).
    Guarantees strong eventual consistency across decentralized replicas without locking.
    """
    def __init__(self, node_id):
        self.node_id = node_id
        self.p = {node_id: 0}
        self.n = {node_id: 0}

    def inc(self, step=1):
        self.p[self.node_id] = self.p.get(self.node_id, 0) + step

    def dec(self, step=1):
        self.n[self.node_id] = self.n.get(self.node_id, 0) + step

    def value(self):
        return sum(self.p.values()) - sum(self.n.values())

    def merge(self, other):
        for k, v in other.p.items():
            self.p[k] = max(self.p.get(k, 0), v)
        for k, v in other.n.items():
            self.n[k] = max(self.n.get(k, 0), v)
