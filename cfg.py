class Node:
    def __init__(self, nodeID, statement):
        self.nodeID = nodeID
        self.statement = statement
        self.edges = []

def handleIf(lines, i, nodes, nodeID, edges, nodesToConnect):
    ifNode = Node(nodeID, lines[i])
    if nodes:
        edges.append((nodesToConnect[-1].nodeID, ifNode.nodeID))
        nodes.append(ifNode)
        nodesToConnect.pop()
        nodesToConnect.append(ifNode)
        print(edges)
    else:
        nodes.append(ifNode)
        nodesToConnect.append(ifNode)
    nodeID += 1
    i += 1
    print(i, nodeID)

    while lines[i] != "}" and i < len(lines):
        if lines[i] != "{":
            node = Node(nodeID, lines[i])
            nodes.append(node)
            edges.append((nodesToConnect[-1].nodeID, nodeID))
            nodesToConnect.pop()
            nodesToConnect.append(node)
            print(node.nodeID, node.statement)
            print(edges)
            nodeID += 1
        i += 1

    if i + 1 < len(lines) and lines[i + 1].startswith("else"):
        i, nodeID, nodesToConnect = handleElse(lines, i + 1, nodes, nodeID, edges, ifNode.nodeID, nodesToConnect)
        print("Out of Else")
    elif i + 1 < len(lines):
        edges.append((ifNode.nodeID, nodeID))

    print(edges)
    print(i, nodeID)

    return i, nodeID, nodesToConnect

def handleElse(lines, i, nodes, nodeID, edges, ifNodeID, nodesToConnect):
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
                nodesToConnect.append(node)
                firstStatementInElse = False
            else:
                edges.append((nodesToConnect[-1].nodeID, nodeID))
                nodesToConnect.pop()
                nodesToConnect.append(node)
            print(node.nodeID, node.statement)
            print(edges)
            nodeID += 1
        i += 1

    print(edges)
    print(i, nodeID)

    return i, nodeID, nodesToConnect

# def handleWhile(lines, i , nodes, nodeID, edges):
#     whileNode = Node(nodeID, lines[i])
#     nodes.append(Node(nodeID, lines[i]))
#     nodeID += 1
#     i += 1
#     print(i, nodeID)

#     while lines[i] != "}" and i < len(lines):
#         if lines[i] != "{":
#             node = Node(nodeID, lines[i])
#             nodes.append(node)
#             edges.append((nodes[-2].nodeID, nodeID))
#             print(node.nodeID, node.statement)
#             print(edges)
#             nodeID += 1
#         i += 1
#     edges.append((nodes[-1].nodeID, whileNode.nodeID))

#     if i + 1 < len(lines):
#         node = Node(nodeID, lines[i+1])
#         edges.append((whileNode.nodeID, node.nodeID))

#     print(edges)
#     print(i, nodeID)

#     return i, nodeID

def parseLines(filename):
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

    return lines

def cfg(filename):
    lines = parseLines(filename)

    nodes = []
    nodeID = 1

    edges = []
    i = 0
    nodesToConnect = []

    while i < len(lines):
        if lines[i].startswith("if"):
            print(lines[i], "If")
            i, nodeID, nodesToConnect = handleIf(lines, i, nodes, nodeID, edges, nodesToConnect)
            print("After handleIf", i, nodeID)
        # elif lines[i].startswith("while"):
        #     print(lines[i], "While")
        #     if nodes:
        #         edges.append((nodes[-1].nodeID, nodeID))
        #         print(edges)
        #     i, nodeID = handleWhile(lines, i, nodes, nodeID, edges)
        #     print("After handleWhile", i, nodeID)
        elif lines[i] not in {"{", "}"}:
            print(lines[i], "Statement")
            node = Node(nodeID, lines[i])
            print(node.nodeID, node.statement)
            nodes.append(node)
            if len(nodesToConnect) == 0:
                nodesToConnect.append(node)
            if len(nodes) > 1:
                while nodesToConnect:
                    edges.append((nodesToConnect[-1].nodeID, node.nodeID))
                    nodesToConnect.pop()
                nodesToConnect.append(node)
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
    # print("While")
    # nodes, edges = cfg("examples/while/while.txt")

    print("\nVertices (Nodes):")
    for n in nodes:
        print(f"({n.nodeID}) {n.statement}")

    edges.sort(key=lambda x: (x[1], x[0]))

    print("\nEdges (Connections):")
    for edge in edges:
        print(f"{edge[0]} -> {edge[1]}")
       