import unittest
from cfg import *

class TestCFGIDoWhileStatement(unittest.TestCase):
    def setUp(self):
        self.nodes = [
            "(1) int x = 0;",
            "(2) x = x + 1;",
            "(3) x = x * 2;",
            "(4) x = x + 5;",
            "(5) x = x * 3;",
            "(6) while (x < 5);",
            "(7) x = x * 2;"
        ]

        self.edges = [
            (1, 2),  
            (2, 3),  
            (3, 4),  
            (4, 5),
            (5, 6),
            (6, 2),
            (6, 7) 
        ]

        self.nestedNodes = [
            "(1) int x = 0;",
            "(2) x = x + 1;",
            "(3) x = x + 2;",
            "(4) while (x < 5);",
            "(5) x = x - 1;",
            "(6) while (x < 10);",
            "(7) x = x * 2;"
        ]

        self.nestedEdges = [
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 3),
            (4, 5),
            (5, 6),
            (6, 2),
            (6, 7)
        ]

    def testSimpleDoWhileStatement(self):
        self.testNodes, self.testEdges = cfg("examples/doWhile/doWhile.txt")
        self.assertEqual(self.edges, self.testEdges)

        for i, node in enumerate(self.testNodes):
            self.assertEqual(f"({node.nodeID}) {node.statement}", self.nodes[i])
    
    def testNestedDoWhile(self):
        self.testNodes, self.testEdges = cfg("examples/doWhile/doWhileNested.txt")
        self.assertEqual(sorted(self.testEdges), sorted(self.nestedEdges))
        for i, node in enumerate(self.testNodes):
            self.assertEqual(f"({node.nodeID}) {node.statement}", self.nestedNodes[i])


if __name__ == "__main__":
    unittest.main(verbosity=2)
