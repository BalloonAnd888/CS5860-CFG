from node import Node

def handleElse(lines, i, nodes, nodeID, edges, ifNodeID, nodesToConnect):
    print("In Else")
    i += 1
    print(i)
    firstStatementInElse = True
    while lines[i] != "}" and i < len(lines):
        if lines[i] != "{":
            node = Node(nodeID, lines[i])
            nodes.append(node)
            if firstStatementInElse:
                edges.append((ifNodeID, node.nodeID))
                nodesToConnect.append(node)
                firstStatementInElse = False
            else:
                edges.append((nodesToConnect[-1].nodeID, node.nodeID))
                nodesToConnect.pop()
                nodesToConnect.append(node)
            print(node.nodeID, node.statement)
            print(edges)
            nodeID += 1
        i += 1

    print(edges)
    print(i, nodeID)

    return i, nodeID, nodesToConnect
