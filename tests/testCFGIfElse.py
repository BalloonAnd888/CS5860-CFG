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

        self.ifElseForNodes = [
            "(1) int x = 5;",
            "(2) if (x > 10)",
            "(3) x = x - 10;",
            "(4) for (int i = 0; i < 2; i++)",
            "(5) x = x + i;",
            "(6) x = x * 2;"
        ]

        self.ifElseForEdges = [
            (1, 2),
            (2, 3),
            (2, 4),
            (3, 6),
            (4, 5),
            (5, 4),
            (4, 6)
        ]

        self.ifElseWhileNodes = [
            "(1) int x = 3;",
            "(2) if (x > 10)",
            "(3) x = x - 10;",
            "(4) while (x < 5)",
            "(5) x = x + 1;",
            "(6) x = x * 2;"
        ]

        self.ifElseWhileEdges = [
            (1, 2),
            (2, 3),
            (2, 4),
            (3, 6),
            (4, 5),
            (5, 4),
            (4, 6)
        ]

        self.ifElseDoWhileNodes = [
            "(1) int x = 3;",
            "(2) if (x > 10)",
            "(3) x = x - 10;",
            "(4) x = x + 1;",
            "(5) while (x < 5);",
            "(6) x = x * 2;"
        ]

        self.ifElseDoWhileEdges = [
            (1, 2),
            (2, 3),
            (2, 4),
            (3, 6),
            (4, 5),
            (5, 4),
            (5, 6)
        ]

    def testCFGIfElseStatement(self):
        self.testNodes, self.testEdges = cfg("examples/ifElse/ifElse.txt")
        self.assertEqual(self.edges, self.edges)

        for i, node in enumerate(self.testNodes):
            self.assertEqual(f"({node.nodeID}) {node.statement}", self.nodes[i])
    
    def testIfElseFor(self):
        self.testNodes, self.testEdges = cfg("examples/ifElse/ifElseFor.txt")
        self.assertEqual(sorted(self.testEdges), sorted(self.ifElseForEdges))
        for i, node in enumerate(self.testNodes):
            self.assertEqual(f"({node.nodeID}) {node.statement}", self.ifElseForNodes[i])

    def testIfElseWithWhile(self):
        self.testNodes, self.testEdges = cfg("examples/ifElse/ifElseWhile.txt")
        self.assertEqual(sorted(self.testEdges), sorted(self.ifElseWhileEdges))
        for i, node in enumerate(self.testNodes):
            self.assertEqual(f"({node.nodeID}) {node.statement}", self.ifElseWhileNodes[i])

    def testIfElseWithDoWhile(self):
        self.testNodes, self.testEdges = cfg("examples/ifElse/ifElseDoWhile.txt")
        self.assertEqual(sorted(self.testEdges), sorted(self.ifElseDoWhileEdges))
        for i, node in enumerate(self.testNodes):
            self.assertEqual(f"({node.nodeID}) {node.statement}", self.ifElseDoWhileNodes[i])

if __name__ == "__main__":
    unittest.main(verbosity=2)
