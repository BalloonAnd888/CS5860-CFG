from node import Node 
from parse import parseLines 
from handleIf import handleIf
from handleWhile import handleWhile
from handleFor import handleFor
from handleDoWhile import handleDoWhile

def cfg(filename: str) -> tuple[list, list]:
    lines = parseLines(filename)
    print(lines)

    nodes = []
    nodesToConnect = []
    edges = []
    nodeID = 1
    i = 0
    lastNode, lastElseNode, lastElseIfNode = None, None, None

    while i < len(lines):
        firstWord = lines[i].split()[0]

        if firstWord == "if":
            print(f"\nStart handleIf:", lines[i])
            i, nodeID, nodesToConnect, lastNode, lastElseNode = handleIf(lines, i, nodes, nodeID, edges, nodesToConnect)
            print("After handleIf", "Line:", i, "NodeID:", nodeID)
        elif firstWord == "while":
            print(f"\nStart handleWhile:", lines[i])
            i, nodeID, nodesToConnect, lastNode = handleWhile(lines, i, nodes, nodeID, edges, nodesToConnect)
            print("Last Node", lastNode.nodeID)
            nodesToConnect.append(lastNode)
            print("After handleWhile", "Line:", i, "NodeID:", nodeID)
        elif firstWord == "for":
            print(f"\nStart handleFor:", lines[i])
            i, nodeID, nodesToConnect, lastNode = handleFor(lines, i, nodes, nodeID, edges, nodesToConnect)
            print("Last Node", lastNode.nodeID)
            nodesToConnect.append(lastNode)
            print("After handleFor", "Line:", i, "NodeID:", nodeID)
        elif firstWord == "do":
            print(f"\nStart handleDo:", lines[i])
            i, nodeID, nodesToConnect, lastNode = handleDoWhile(lines, i, nodes, nodeID, edges, nodesToConnect)
            print("After handleDoWhile", "Line:", i, "NodeID:", nodeID)
        elif lines[i] not in {"{", "}"}:
            node = Node(nodeID, lines[i])
            print(f"\n{node.nodeID}", node.statement, "Statement")
            nodes.append(node)
            print("Nodes:", [f"({n.nodeID})" for n in nodes])
            if len(nodesToConnect) == 0 and i + 1 != len(lines):
                nodesToConnect.append(node)
                print("Nodes to connect:", [f"({n.nodeID}) {n.statement}" for n in nodesToConnect])
            if len(nodes) > 1:
                while nodesToConnect:
                    edges.append((nodesToConnect[-1].nodeID, node.nodeID))
                    nodesToConnect.pop()
                nodesToConnect.append(node)
                print("Nodes to connect:", [f"({n.nodeID}) {n.statement}" for n in nodesToConnect])
                print(edges)

            nodeID += 1

        i += 1

    return nodes, edges

if __name__ == "__main__":
    # nodes, edges = cfg("examples/while/whileWithOther.txt")
    # nodes, edges = cfg("examples/elseIf/elseIf.txt")
    # nodes, edges = cfg("examples/ifElse/ifElseWhile.txt")
    nodes, edges = cfg("examples/programs/program5.txt")
    # nodes, edges = cfg("examples/t2.txt")

    print("\nVertices (Nodes):")
    for n in nodes:
        print(f"({n.nodeID}) {n.statement}")

    edges.sort(key=lambda x: (x[1], x[0]))

    print("\nEdges (Connections):")
    for edge in edges:
        print(f"{edge[0]} -> {edge[1]}")
       