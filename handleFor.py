from node import Node 

def handleFor(lines: list, i: int, nodes: list, nodeID: int, edges: list, nodesToConnect: list) -> tuple[int, int, list, Node]:
    from handleIf import handleIf
    from handleWhile import handleWhile
    from handleDoWhile import handleDoWhile

    forNode = Node(nodeID, lines[i])
    if nodes:
        edges.append((nodesToConnect[-1].nodeID, forNode.nodeID))
        nodes.append(forNode)
        print(f"\n{forNode.nodeID}", forNode.statement, "For")
        print("Nodes:", [f"({n.nodeID})" for n in nodes])
        nodesToConnect.pop()
        nodesToConnect.append(forNode)
        print("Nodes to connect:", [f"({n.nodeID}) {n.statement}" for n in nodesToConnect])
        print("Edges:", edges)
    else:
        nodes.append(forNode)
        print(f"\n{forNode.nodeID}", forNode.statement, "For")
        print("Nodes:", [f"({n.nodeID})" for n in nodes])
        nodesToConnect.append(forNode)
        print("Nodes to connect:", [f"({n.nodeID}) {n.statement}" for n in nodesToConnect])
    nodeID += 1
    i += 1
    print("Line:", i, "NodeID:", nodeID)

    while lines[i] != "}" and i < len(lines):
        if lines[i] != "{":
            firstWord = lines[i].split()[0]
            if firstWord == "if":
                print(f"\nStart handleIf:", lines[i])
                i, nodeID, nodesToConnect = handleIf(lines, i, nodes, nodeID, edges, nodesToConnect)
                print("After handleIf","Line:", i, "NodeID:", nodeID)
            elif firstWord == "while":
                print(f"\nStart handleWhile:", lines[i])
                i, nodeID, nodesToConnect, lastNode = handleWhile(lines, i, nodes, nodeID, edges, nodesToConnect)
                nodesToConnect.append(lastNode)
                print("Last Node", lastNode.nodeID)
                print("After handleWhile","Line:", i, "NodeID:", nodeID)
            elif firstWord == "for":
                print(f"\nStart handleFor:", lines[i])
                i, nodeID, nodesToConnect, lastNode = handleFor(lines, i, nodes, nodeID, edges, nodesToConnect)
                nodesToConnect.append(lastNode)
                print("Last Node", lastNode.nodeID)
                print("After handleFor","Line:", i, "NodeID:", nodeID)
            elif firstWord == "do":
                print(f"\nStart handleDo:", lines[i])
                i, nodeID, nodesToConnect = handleDoWhile(lines, i, nodes, nodeID, edges, nodesToConnect)
                print("After handleDoWhile","Line:", i, "NodeID:", nodeID)
            else:
                node = Node(nodeID, lines[i])
                print(f"\n{node.nodeID}", node.statement, "Statement")
                nodes.append(node)
                print("Nodes:", [f"({n.nodeID})" for n in nodes])
                edges.append((nodesToConnect[-1].nodeID, node.nodeID))
                nodesToConnect.pop()
                nodesToConnect.append(node)
                lastNode = node
                print("Nodes to connect:", [f"({n.nodeID}) {n.statement}" for n in nodesToConnect])
                print("Edges:", edges)
                nodeID += 1
        i += 1
    if nodesToConnect:
        edges.append((nodesToConnect[-1].nodeID, forNode.nodeID))
        nodesToConnect.pop()

    print("Edges", edges)
    print("Line:", i, "NodeID:", nodeID)

    return i, nodeID, nodesToConnect, forNode
