from node import Node 
from handleElse import handleElse

def handleIf(lines, i, nodes, nodeID, edges, nodesToConnect):
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
            node = Node(nodeID, lines[i])
            nodes.append(node)
            edges.append((nodesToConnect[-1].nodeID, nodeID))
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