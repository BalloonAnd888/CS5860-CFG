from node import Node 

def handleDoWhile(lines, i, nodes, nodeID, edges, nodesToConnect):
    i += 2

    doFirstNode = Node(nodeID, lines[i])

    if nodes:
        edges.append((nodesToConnect[-1].nodeID, doFirstNode.nodeID))
        nodes.append(doFirstNode)
        nodesToConnect.pop()
        nodesToConnect.append(doFirstNode)
        print(edges)
    else:
        nodes.append(doFirstNode)
        nodesToConnect.append(doFirstNode)
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

    i += 1

    node = Node(nodeID, lines[i])
    nodes.append(node)
    edges.append((nodesToConnect[-1].nodeID, node.nodeID))
    nodesToConnect.pop()
    nodesToConnect.append(node)

    edges.append((nodesToConnect[-1].nodeID, doFirstNode.nodeID))
    nodeID += 1

    return i, nodeID, nodesToConnect
