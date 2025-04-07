from node import Node 
from parse import parseLines 
from handleIf import handleIf
from handleWhile import handleWhile
from handleFor import handleFor
from handleDoWhile import handleDoWhile

def cfg(filename):
    lines = parseLines(filename)

    nodes = []
    nodesToConnect = []
    edges = []
    nodeID = 1
    i = 0

    while i < len(lines):
        firstWord = lines[i].split()[0]

        if firstWord == "if":
            print(lines[i], "If")
            i, nodeID, nodesToConnect = handleIf(lines, i, nodes, nodeID, edges, nodesToConnect)
            print("After handleIf", i, nodeID)
        elif firstWord == "while":
            print(lines[i], "While")
            i, nodeID, nodesToConnect, lastNode = handleWhile(lines, i, nodes, nodeID, edges, nodesToConnect)
            print("Last Node", lastNode.nodeID)
            nodesToConnect.append(lastNode)
            print("After handleWhile", i, nodeID)
        elif firstWord == "for":
            print(lines[i], "For")
            i, nodeID, nodesToConnect = handleFor(lines, i, nodes, nodeID, edges, nodesToConnect)
            print("After handleFor", i, nodeID)
        elif firstWord == "do":
            print(lines[i], "Do")
            i, nodeID, nodesToConnect = handleDoWhile(lines, i, nodes, nodeID, edges, nodesToConnect)
            print("After handleDoWhile", i, nodeID)
        elif lines[i] not in {"{", "}"}:
            print(lines[i], "Statement")
            node = Node(nodeID, lines[i])
            print(node.nodeID, node.statement)
            nodes.append(node)
            if len(nodesToConnect) == 0 and i + 1 != len(lines):
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
    # print("If-Else")
    # nodes, edges = cfg("examples/ifElse/ifElse.txt")
    print("While")
    nodes, edges = cfg("examples/while/whileNested.txt")
    # print("For")
    # nodes, edges = cfg("examples/for/for.txt")
    # print("Do While")
    # nodes, edges = cfg("examples/doWhile/doWhile.txt")
    # print("Test")
    # nodes, edges = cfg("examples/test.txt")

    print("\nVertices (Nodes):")
    for n in nodes:
        print(f"({n.nodeID}) {n.statement}")

    edges.sort(key=lambda x: (x[1], x[0]))

    print("\nEdges (Connections):")
    for edge in edges:
        print(f"{edge[0]} -> {edge[1]}")
       