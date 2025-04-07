from node import Node 

def handleFor(lines, i, nodes, nodeID, edges, nodesToConnect):
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
                i, nodeID, nodesToConnect = handleIf(lines, i, nodes, nodeID, edges, nodesToConnect)
            elif firstWord == "while":
                print(lines[i], "While")
                i, nodeID, nodesToConnect, lastNode = handleWhile(lines, i, nodes, nodeID, edges, nodesToConnect)
                nodesToConnect.append(lastNode)
                print("LastNode ID", lastNode.nodeID)
            elif firstWord == "for":
                print(lines[i], "For")
                i, nodeID, nodesToConnect, lastNode = handleFor(lines, i, nodes, nodeID, edges, nodesToConnect)
                nodesToConnect.append(lastNode)
                print("LastNode ID", lastNode.nodeID)
            elif firstWord == "do":
                i, nodeID, nodesToConnect = handleDoWhile(lines, i, nodes, nodeID, edges, nodesToConnect)
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
