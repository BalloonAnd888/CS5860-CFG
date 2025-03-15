class Node:
    def __init__(self, nodeID, statement):
        self.nodeID = nodeID
        self.statement = statement

def cfg(filename):
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            if line != "\n":
                lines.append(line.rstrip())
    
    print(lines)

    nodes = []
    nodeID = 1
    for line in lines:
        nodes.append(Node(nodeID, line.rstrip()))
        nodeID += 1

    for n in nodes:
        print(n.nodeID, n.statement)

    vertices = [node.nodeID for node in nodes]
    edges = [(nodes[i].nodeID, nodes[i+1].nodeID) for i in range(len(nodes) - 1)]

    print("Vertices:", vertices)
    print("Edges:", edges)

    print("Vertices (Nodes):")
    for node in nodes:
        print(f"({node.nodeID}) {node.statement}")

    print("\nEdges (Connections):")
    for edge in edges:
        print(f"{edge[0]} -> {edge[1]}")


if __name__ == "__main__":
    print("Statement")
    cfg("statement.txt")
    print("\nif")
    cfg("if.txt")




