from node import Node 

def handleFor(lines: list, i: int, nodes: list, nodeID: int, edges: list, nodesToConnect: list) -> tuple[int, int, list, Node]:
    from handleIf import handleIf
    from handleWhile import handleWhile
    from handleDoWhile import handleDoWhile

    forNode = Node(nodeID, lines[i])
    if nodes:
        edges.append((nodesToConnect[-1].nodeID, forNode.nodeID))
        nodes.append(forNode)
        nodesToConnect.pop()
        nodesToConnect.append(forNode)
        print(edges)
    else:
        nodes.append(forNode)
        nodesToConnect.append(forNode)
    nodeID += 1
    i += 1
    print(i, nodeID)

    while lines[i] != "}" and i < len(lines):
        if lines[i] != "{":
            firstWord = lines[i].split()[0]
            if firstWord == "if":
                print(lines[i], "If")
                i, nodeID, nodesToConnect = handleIf(lines, i, nodes, nodeID, edges, nodesToConnect)
                print("After handleIf", i, nodeID)
            elif firstWord == "while":
                print(lines[i], "While")
                i, nodeID, nodesToConnect, lastNode = handleWhile(lines, i, nodes, nodeID, edges, nodesToConnect)
                nodesToConnect.append(lastNode)
                print("Last Node", lastNode.nodeID)
                print("After handleWhile", i, nodeID)
            elif firstWord == "for":
                print(lines[i], "For")
                i, nodeID, nodesToConnect, lastNode = handleFor(lines, i, nodes, nodeID, edges, nodesToConnect)
                nodesToConnect.append(lastNode)
                print("Last Node", lastNode.nodeID)
                print("After handleFor", i, nodeID)
            elif firstWord == "do":
                print(lines[i], "Do")
                i, nodeID, nodesToConnect = handleDoWhile(lines, i, nodes, nodeID, edges, nodesToConnect)
                print("After handleDoWhile", i, nodeID)
            else:
                node = Node(nodeID, lines[i])
                nodes.append(node)
                edges.append((nodesToConnect[-1].nodeID, node.nodeID))
                nodesToConnect.pop()
                nodesToConnect.append(node)
                lastNode = node
                print(node.nodeID, node.statement)
                print(edges)
                nodeID += 1
        i += 1
    if nodesToConnect:
        edges.append((nodesToConnect[-1].nodeID, forNode.nodeID))
        nodesToConnect.pop()


    print(edges)
    print(i, nodeID)

    return i, nodeID, nodesToConnect, forNode
