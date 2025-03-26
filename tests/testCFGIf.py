import unittest
from cfg import *

class TestCFGIfStatement(unittest.TestCase):
    def setUp(self):
        self.nodes = [
            "(1) int a = 5;",
            "(2) double b = 10.5;",
            "(3) float c;",
            "(4) if (a > b)",
            "(5) c = a + b;",
            "(6) a = b + c;",
            "(7) if (a > b)",
            "(8) c = a + b;",
            "(9) a = b + c;",
            "(10) a = a * 2;"
        ]

        self.edges = [
            (1, 2),  
            (2, 3),  
            (3, 4),  
            (4, 5), 
            (5, 6), 
            (4, 7),  
            (6, 7),  
            (7, 8),  
            (8, 9),  
            (7, 10), 
            (9, 10)  
        ]

    def testCFGIfStatement(self):
        self.testNodes, self.testEdges = cfg("examples/if/if.txt")
        self.assertEqual(self.edges, self.testEdges)

        for i, node in enumerate(self.testNodes):
            self.assertEqual(f"({node.nodeID}) {node.statement}", self.nodes[i])

if __name__ == "__main__":
    unittest.main(verbosity=2)
