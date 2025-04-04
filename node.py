class Node:
    def __init__(self, nodeID, statement):
        self.nodeID = nodeID
        self.statement = statement
        self.edges = []