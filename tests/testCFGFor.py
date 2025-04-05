import unittest
from cfg import *

class TestCFGIForStatement(unittest.TestCase):
    def setUp(self):
        self.nodes = [
            "(1) int x = 0;",
            "(2) int y = 0;",
            "(3) for (int i = 0; i < 5; i++)",
            "(4) x = x + 1;",
            "(5) y = i * x;",
            "(6) x = x * 2;"
        ]

        self.edges = [
            (1, 2),  
            (2, 3),  
            (3, 4),  
            (4, 5),
            (5, 3),
            (3, 6) 
        ]

    def testCFGForStatement(self):
        self.testNodes, self.testEdges = cfg("examples/for/for.txt")
        self.assertEqual(self.edges, self.testEdges)

        for i, node in enumerate(self.testNodes):
            self.assertEqual(f"({node.nodeID}) {node.statement}", self.nodes[i])

if __name__ == "__main__":
    unittest.main(verbosity=2)
