import unittest
from cfg import *

class TestCFGIWhileStatement(unittest.TestCase):
    def setUp(self):
        self.nodes = [
            "(1) int x = 0;",
            "(2) while (x < 5)",
            "(3) x = x + 1;",
            "(4) y = y + 3;",
            "(5) x = x * 2;"
        ]

        self.edges = [
            (1, 2),  
            (2, 3),  
            (3, 4),  
            (4, 2),
            (2, 5) 
        ]

    def testCFGWhileStatement(self):
        self.testNodes, self.testEdges = cfg("examples/while/while.txt")
        self.assertEqual(self.edges, self.testEdges)

        for i, node in enumerate(self.testNodes):
            self.assertEqual(f"({node.nodeID}) {node.statement}", self.nodes[i])

if __name__ == "__main__":
    unittest.main(verbosity=2)
