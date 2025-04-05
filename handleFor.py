from node import Node 

def handleFor(lines, i, nodes, nodeID, edges, nodesToConnect):
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
            node = Node(nodeID, lines[i])
            nodes.append(node)
            edges.append((nodesToConnect[-1].nodeID, node.nodeID))
            nodesToConnect.pop()
            nodesToConnect.append(node)
            print(node.nodeID, node.statement)
            print(edges)
            nodeID += 1
        i += 1

    edges.append((nodesToConnect[-1].nodeID, forNode.nodeID))
    nodesToConnect.pop()

    if i + 1 < len(lines):
        edges.append((forNode.nodeID, nodeID))


    print(edges)
    print(i, nodeID)

    return i, nodeID, nodesToConnect
