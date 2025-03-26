import unittest
from cfg import *

class TestCFGIfElseStatement(unittest.TestCase):
    def setUp(self):
        self.nodes = [
            "(1) int x = 10;",
            "(2) int y = 5;",
            "(3) if (x > y)",
            "(4) x = x - y;",
            "(5) x = x + 1;",
            "(6) y = y + x;",
            "(7) y = y + 5;",
            "(8) x = x + 1;",
            "(9) y = x + 5;"
        ]

        self.edges = [
            (1, 2),  
            (2, 3),  
            (3, 4),  
            (4, 5),  
            (3, 6),  
            (5, 8),  
            (6, 7),  
            (7, 8),  
            (8, 9)   
        ]

    def testCFGIfElseStatement(self):
        self.testNodes, self.testEdges = cfg("examples/ifElse/ifElse.txt")
        self.assertEqual(self.edges, self.edges)

        for i, node in enumerate(self.testNodes):
            self.assertEqual(f"({node.nodeID}) {node.statement}", self.nodes[i])

if __name__ == "__main__":
    unittest.main(verbosity=2)
