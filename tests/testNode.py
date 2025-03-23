import unittest
from cfg import Node

class TestNode(unittest.TestCase):
    def setUp(self):
        self.node1 = Node(1, "if (a < 5)")
        self.node2 = Node(2, "x = 10")
    
    def testNodeInitialization(self):
        self.assertEqual(self.node1.nodeID, 1)
        self.assertEqual(self.node1.statement, "if (a < 5)")
        self.assertEqual(self.node1.edges, [])
        
    def testAddEdge(self):
        self.node1.edges.append(2)
        self.assertIn(2, self.node1.edges)

if __name__ == "__main__":
    unittest.main(verbosity=2)



