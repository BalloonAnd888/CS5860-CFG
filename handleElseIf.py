from node import Node

def handleElseIf(lines: list, i: int, nodes: list, nodeID: int, edges: list, ifNode: int, nodesToConnect: list) -> tuple[int, int, list]:
    from handleIf import handleIf
    from handleWhile import handleWhile
    from handleFor import handleFor
    from handleDoWhile import handleDoWhile
    from handleElse import handleElse
    from handleElseIf import handleElseIf
    
    elseIfNode = Node(nodeID, lines[i])
    if nodes:
        edges.append((ifNode.nodeID, elseIfNode.nodeID))
        nodes.append(elseIfNode)
        print(f"\n{elseIfNode.nodeID}", elseIfNode.statement, "If")
        print("Nodes:", [f"({n.nodeID})" for n in nodes])
        nodesToConnect.append(elseIfNode)
        print("Nodes to connect:", [f"({n.nodeID}) {n.statement}" for n in nodesToConnect])
        print("Edges:", edges)
    else:
        nodes.append(elseIfNode)
        print(f"\n{elseIfNode.nodeID}", elseIfNode.statement, "If")
        print("Nodes:", [f"({n.nodeID})" for n in nodes])
        nodesToConnect.append(elseIfNode)
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
                print("Nodes to connect:", [f"({n.nodeID}) {n.statement}" for n in nodesToConnect])
                print("Edges:", edges)
                nodeID += 1
        i += 1

    if i + 1 < len(lines) and lines[i + 1].startswith("else if", 0, 7):
        i, nodeID, nodesToConnect = handleElseIf(lines, i + 1, nodes, nodeID, edges, elseIfNode.nodeID, nodesToConnect)
    elif i + 1 < len(lines) and lines[i + 1].startswith("else", 0, 4):
        i, nodeID, nodesToConnect = handleElse(lines, i + 1, nodes, nodeID, edges, elseIfNode.nodeID, nodesToConnect)
        print("Out of Else")
    elif i + 1 < len(lines) and lines[i + 1] != "}":
        edges.append((ifNode.nodeID, nodeID))
    else:
        nodesToConnect.append(ifNode)

    print("Edges", edges)
    print("Line:", i, "NodeID:", nodeID)

    return i, nodeID, nodesToConnect