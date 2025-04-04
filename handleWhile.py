from node import Node 

def handleWhile(lines, i, nodes, nodeID, edges, nodesToConnect):
    whileNode = Node(nodeID, lines[i])
    if nodes:
        edges.append((nodesToConnect[-1].nodeID, whileNode.nodeID))
        nodes.append(whileNode)
        nodesToConnect.pop()
        nodesToConnect.append(whileNode)
        print(edges)
    else:
        nodes.append(whileNode)
        nodesToConnect.append(whileNode)
    nodeID += 1
    i += 1
    print(i, nodeID)

    while lines[i] != "}" and i < len(lines):
        if lines[i] != "{":
            node = Node(nodeID, lines[i])
            nodes.append(node)
            edges.append((nodesToConnect[-1].nodeID, node.nodeID))
            nodesToConnect.pop()
            nodesToConnect.append(node)
            print(node.nodeID, node.statement)
            print(edges)
            nodeID += 1
        i += 1

    edges.append((nodesToConnect[-1].nodeID, whileNode.nodeID))
    nodesToConnect.pop()

    if i + 1 < len(lines):
        edges.append((whileNode.nodeID, nodeID))


    print(edges)
    print(i, nodeID)

    return i, nodeID, nodesToConnect
