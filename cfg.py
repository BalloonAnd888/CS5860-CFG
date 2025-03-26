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

    if i + 1 < len(lines) and lines[i + 1].startswith("else"):
        lastIfNode = nodeID - 1
        i, nodeID = handleElse(lines, i + 1, nodes, nodeID, edges, ifNode.nodeID)
        print("Out of Else")
        if i + 1 < len(lines):
            edges.append((lastIfNode, nodeID))
    elif i + 1 < len(lines):
        edges.append((ifNode.nodeID, nodeID))

    print(edges)
    print(i, nodeID)

    return i, nodeID

def handleElse(lines, i, nodes, nodeID, edges, ifNodeID):
    print("In Else")
    i += 1
    print(i)
    firstStatementInElse = True
    while lines[i] != "}" and i < len(lines):
        if lines[i] != "{":
            node = Node(nodeID, lines[i])
            nodes.append(node)
            if firstStatementInElse:
                edges.append((ifNodeID, nodeID))
                firstStatementInElse = False
            else:
                edges.append((nodes[-2].nodeID, nodeID))
            print(node.nodeID, node.statement)
            print(edges)
            nodeID += 1
        i += 1
    
    return i, nodeID

def cfg(filename):
    # Lines of code
    lines = []
    inMultilineComment = False
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()

            if "/*" in line:
                inMultilineComment = True
            if "*/" in line:
                inMultilineComment = False
                continue  

            if line and not line.startswith("//") and not inMultilineComment:
                lines.append(line)

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
            i, nodeID = handleIf(lines, i, nodes, nodeID, edges)
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

    return nodes, edges

if __name__ == "__main__":
    # print("Statement")
    # nodes, edges = cfg("examples/statement/statement.txt")
    # print("if")
    # nodes, edges = cfg("examples/if/if.txt")
    print("If-Else")
    nodes, edges = cfg("examples/ifElse/ifElse.txt")

    print("\nVertices (Nodes):")
    for n in nodes:
        print(f"({n.nodeID}) {n.statement}")

    print("\nEdges (Connections):")
    for edge in edges:
        print(f"{edge[0]} -> {edge[1]}")
       