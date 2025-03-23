class Node:
    def __init__(self, nodeID, statement):
        self.nodeID = nodeID
        self.statement = statement
        self.edges = []

def handleIf(lines, i, nodes, nodeID, edges):
    ifNode = Node(nodeID, lines[i])
    nodes.append(Node(nodeID, lines[i]))
    nodeID += 1
    i += 1
    print(i, nodeID)

    while lines[i] != "}" and i < len(lines):
        if lines[i] != "{":
            node = Node(nodeID, lines[i])
            nodes.append(node)
            edges.append((nodes[-2].nodeID, nodeID))
            print(node.nodeID, node.statement)
            print(edges)
            nodeID += 1
        i += 1

    if i + 1 < len(lines):
        edges.append((ifNode.nodeID, nodeID))


    return i, nodeID

def cfg(filename):
    # Lines of code
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            if line != "\n":
                lines.append(line.rstrip().lstrip())
    
    print(lines)

    # Create nodes
    nodes = []
    nodeID = 1

    edges = []
    i = 0
    while i < len(lines):
        if lines[i].startswith("if"):
            print(lines[i], "If")
            if nodes:
                edges.append((nodes[-1].nodeID, nodeID))
                print(edges)
            i, nodeID = handleIf(lines, i, nodes, nodeID, edges) # i = 3, nodeID = 4
            print("After handleIF", i, nodeID)
        elif lines[i] not in {"{", "}"}:
            print(lines[i], "Statement")
            node = Node(nodeID, lines[i])
            print(node.nodeID, node.statement)
            nodes.append(node)
            if len(nodes) > 1:
                edges.append((nodes[-2].nodeID, nodes[-1].nodeID))
                print(edges)
            nodeID += 1

        i += 1

    print("\nVertices (Nodes):")
    for n in nodes:
        print(f"({n.nodeID}) {n.statement}")

    print("\nEdges (Connections):")
    for edge in edges:
        print(f"{edge[0]} -> {edge[1]}")


if __name__ == "__main__":
    print("Statement")
    cfg("statement.txt")
    print("if")
    cfg("if.txt")
        