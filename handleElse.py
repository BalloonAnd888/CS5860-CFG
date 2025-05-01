from node import Node

def handleElse(lines: list, i: int, nodes: list, nodeID: int, edges: list, ifNodeID: int, nodesToConnect: list) -> tuple[int, int, list]:   
    from handleIf import handleIf
    from handleWhile import handleWhile
    from handleFor import handleFor
    from handleDoWhile import handleDoWhile
    print("In Else")
    i += 1
    print(i)
    firstStatementInElse = True
    print(firstStatementInElse)
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
                if firstStatementInElse:
                    print(firstStatementInElse)
                    edges.append((ifNodeID, node.nodeID))
                    print("Edges:", edges)
                    nodesToConnect.append(node)
                    print("Nodes to connect:", [f"({n.nodeID}) {n.statement}" for n in nodesToConnect])
                    firstStatementInElse = False
                else:
                    print(firstStatementInElse)
                    edges.append((nodesToConnect[-1].nodeID, node.nodeID))
                    print("Edges:", edges)
                    nodesToConnect.pop()
                    nodesToConnect.append(node)
                    print("Nodes to connect:", [f"({n.nodeID}) {n.statement}" for n in nodesToConnect])
                print(node.nodeID, node.statement)
                print(edges)
                nodeID += 1
        i += 1

    print(edges)
    print(i, nodeID)

    return i, nodeID, nodesToConnect
