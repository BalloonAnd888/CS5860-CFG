from node import Node 

def handleDoWhile(lines: list, i: int, nodes: list, nodeID: int, edges: list, nodesToConnect: list) -> tuple[int, int, list]:
    from handleIf import handleIf
    from handleWhile import handleWhile
    from handleFor import handleFor

    i += 2

    doFirstNode = Node(nodeID, lines[i])

    if nodes:
        edges.append((nodesToConnect[-1].nodeID, doFirstNode.nodeID))
        nodes.append(doFirstNode)
        print(f"\n{doFirstNode.nodeID}", doFirstNode.statement, "Do")
        print("Nodes:", [f"({n.nodeID})" for n in nodes])
        nodesToConnect.pop()
        nodesToConnect.append(doFirstNode)
        print([f"Nodes to connect: ({n.nodeID}) {n.statement}" for n in nodesToConnect])
        print("Edges:", edges)
    else:
        nodes.append(doFirstNode)
        print(f"\n{doFirstNode.nodeID}", doFirstNode.statement, "Do")
        print("Nodes:", [f"({n.nodeID})" for n in nodes])
        nodesToConnect.append(doFirstNode)
        print([f"Nodes to connect: ({n.nodeID}) {n.statement}" for n in nodesToConnect])
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
                print([f"Nodes to connect: ({n.nodeID}) {n.statement}" for n in nodesToConnect])
                print("Edges:", edges)
                nodeID += 1
        i += 1

    i += 1

    node = Node(nodeID, lines[i])
    nodes.append(node)
    edges.append((nodesToConnect[-1].nodeID, node.nodeID))
    nodesToConnect.pop()
    nodesToConnect.append(node)

    edges.append((nodesToConnect[-1].nodeID, doFirstNode.nodeID))
    nodeID += 1

    return i, nodeID, nodesToConnect
