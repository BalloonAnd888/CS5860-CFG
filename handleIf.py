from node import Node 

def handleIf(lines, i, nodes, nodeID, edges, nodesToConnect):
    from handleWhile import handleWhile
    from handleFor import handleFor
    from handleDoWhile import handleDoWhile
    from handleElse import handleElse
    
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
            firstWord = lines[i].split()[0]
            if firstWord == "if":
                print(lines[i], "If")
                i, nodeID, nodesToConnect = handleIf(lines, i, nodes, nodeID, edges, nodesToConnect)
                print("After handleIf", i, nodeID)
            elif firstWord == "while":
                print(lines[i], "While")
                i, nodeID, nodesToConnect = handleWhile(lines, i, nodes, nodeID, edges, nodesToConnect)
                print("After handleWhile", i, nodeID)
            elif firstWord == "for":
                print(lines[i], "For")
                i, nodeID, nodesToConnect = handleFor(lines, i, nodes, nodeID, edges, nodesToConnect)
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
