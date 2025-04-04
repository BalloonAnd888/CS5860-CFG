from node import Node 

# def handleWhile(lines, i , nodes, nodeID, edges):
#     whileNode = Node(nodeID, lines[i])
#     nodes.append(Node(nodeID, lines[i]))
#     nodeID += 1
#     i += 1
#     print(i, nodeID)

#     while lines[i] != "}" and i < len(lines):
#         if lines[i] != "{":
#             node = Node(nodeID, lines[i])
#             nodes.append(node)
#             edges.append((nodes[-2].nodeID, nodeID))
#             print(node.nodeID, node.statement)
#             print(edges)
#             nodeID += 1
#         i += 1
#     edges.append((nodes[-1].nodeID, whileNode.nodeID))

#     if i + 1 < len(lines):
#         node = Node(nodeID, lines[i+1])
#         edges.append((whileNode.nodeID, node.nodeID))

#     print(edges)
#     print(i, nodeID)

#     return i, nodeID