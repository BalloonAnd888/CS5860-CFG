from node import Node 

def handleWhile(lines: list, i: int, nodes: list, nodeID: int, edges: list, nodesToConnect: list) -> tuple[int, int, list, Node]:
    from handleIf import handleIf
    from handleFor import handleFor
    from handleDoWhile import handleDoWhile
    
    whileNode = Node(nodeID, lines[i])
    lastNode, lastElseNode, lastElseIfNode = None, None, None

    if nodes:
        edges.append((nodesToConnect[-1].nodeID, whileNode.nodeID))
        nodes.append(whileNode)
        print(f"\n{whileNode.nodeID}", whileNode.statement, "While")
        print("Nodes:", [f"({n.nodeID})" for n in nodes])
        nodesToConnect.pop()
        nodesToConnect.append(whileNode)
        print("Nodes to connect:", [f"({n.nodeID}) {n.statement}" for n in nodesToConnect])
        print("Edges:", edges)
    else:
        nodes.append(whileNode)
        print(f"\n{whileNode.nodeID}", whileNode.statement, "While")
        print("Nodes:", [f"({n.nodeID})" for n in nodes])
        nodesToConnect.append(whileNode)
        print("Nodes to connect:", [f"({n.nodeID}) {n.statement}" for n in nodesToConnect])
    nodeID += 1
    i += 1
    print("Line:", i, "NodeID:", nodeID)

    while lines[i] != "}" and i < len(lines):
        if lines[i] != "{":
            firstWord = lines[i].split()[0]
            if firstWord == "if":
                print(f"\nStart handleIf:", lines[i])
                i, nodeID, nodesToConnect, lastNode, lastElseNode = handleIf(lines, i, nodes, nodeID, edges, nodesToConnect)
                print("After handleIf", "Line:", i, "NodeID:", nodeID)
            elif firstWord == "while":
                print(f"\nStart handleWhile:", lines[i])
                i, nodeID, nodesToConnect, lastNode = handleWhile(lines, i, nodes, nodeID, edges, nodesToConnect)
                nodesToConnect.append(lastNode)
                print("Last Node", lastNode.nodeID)
                print("After handleWhile", "Line:", i, "NodeID:", nodeID)
            elif firstWord == "for":
                print(f"\nStart handleFor:", lines[i])
                i, nodeID, nodesToConnect, lastNode = handleFor(lines, i, nodes, nodeID, edges, nodesToConnect)
                nodesToConnect.append(lastNode)
                print("Last Node", lastNode.nodeID)
                print("After handleFor", "Line:", i, "NodeID:", nodeID)
            elif firstWord == "do":
                print(f"\nStart handleDo:", lines[i])
                i, nodeID, nodesToConnect, lastNode = handleDoWhile(lines, i, nodes, nodeID, edges, nodesToConnect)
                print("After handleDoWhile", "Line:", i, "NodeID:", nodeID)
            else:
                node = Node(nodeID, lines[i])
                print(f"\n{node.nodeID}", node.statement, "Statement")
                nodes.append(node)
                print("Nodes:", [f"({n.nodeID})" for n in nodes])
                if lastNode and lastElseNode:
                    edges.append((lastNode.nodeID, node.nodeID))
                    edges.append((lastElseNode.nodeID, node.nodeID))
                    nodesToConnect = [n for n in nodesToConnect if n.nodeID != lastNode.nodeID and n.nodeID != lastElseNode.nodeID]
                else:
                    edges.append((nodesToConnect[-1].nodeID, node.nodeID))
                    nodesToConnect.pop()
                nodesToConnect.append(node)
                print("Nodes to connect:", [f"({n.nodeID}) {n.statement}" for n in nodesToConnect])
                print("Edges:", edges)
                nodeID += 1
        i += 1

    if nodesToConnect:
        edges.append((nodesToConnect[-1].nodeID, whileNode.nodeID))
        nodesToConnect.pop()
        print("Nodes to connect:", [f"({n.nodeID}) {n.statement}" for n in nodesToConnect])
        print("Edges:", edges)

    if i == len(lines) - 1 and nodesToConnect:
        edges.append((nodesToConnect[-1].nodeID, whileNode.nodeID))

    print("Edges", edges)
    print("Line:", i, "NodeID:", nodeID)

    return i, nodeID, nodesToConnect, whileNode
