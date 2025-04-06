import unittest
from cfg import *

class TestCFGIfStatement(unittest.TestCase):
    def setUp(self):
        self.simpleNodes = [
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

        self.simpleEdges = [
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

        self.nestedNodes = [
            "(1) int x = 5;",
            "(2) if (x > 0)",
            "(3) x = x + 1;",
            "(4) if (x < 10)",
            "(5) x = x + 2;",
            "(6) if (x == 7)",
            "(7) x = x + 3;",
            "(8) x = x * 2;"
        ]

        self.nestedEdges = [
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
            (5, 6),
            (6, 7),
            (2, 8),
            (4, 8),
            (6, 8),
            (7, 8)
        ]

    def testSimpleIf(self):
        self.testNodes, self.testEdges = cfg("examples/if/if.txt")
        self.assertEqual(sorted(self.testEdges), sorted(self.simpleEdges))
        for i, node in enumerate(self.testNodes):
            self.assertEqual(f"({node.nodeID}) {node.statement}", self.simpleNodes[i])
    
    def testNestedIf(self):
        self.testNodes, self.testEdges = cfg("examples/if/ifNested.txt")
        self.assertEqual(sorted(self.testEdges), sorted(self.nestedEdges))
        for i, node in enumerate(self.testNodes):
            self.assertEqual(f"({node.nodeID}) {node.statement}", self.nestedNodes[i])

if __name__ == "__main__":
    unittest.main(verbosity=2)
