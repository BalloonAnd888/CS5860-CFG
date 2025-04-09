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

        self.ifWithAllNestedNodes = [
            "(1) int x = 0;",
            "(2) int y = 0;",
            "(3) if (x >= 0)",
            "(4) x = x + 1;",
            "(5) while (x < 5)",
            "(6) x = x + 2;",
            "(7) for (int i = 0; i < 2; i++)",
            "(8) x = x * 2;",
            "(9) x = x - 1;",
            "(10) while (x > 0);",
            "(11) if (x == 0)",
            "(12) x = x + 100;",
            "(13) y++;",
            "(14) x = x - 3;"
        ]

        self.ifWithAllNestedEdges = [
            (1, 2),
            (2, 3),
            (3, 4),
            (3, 14),
            (4, 5),
            (5, 6),
            (6, 5),
            (5, 7),
            (7, 8),
            (8, 7),
            (7, 9),
            (9, 10),
            (10, 9),
            (10, 11),
            (11, 12),
            (11, 13),
            (12, 13),
            (13, 14)
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
    
    def testIfWithAllNested(self):
        testNodes, testEdges = cfg("examples/if/ifWithOther.txt")
        self.assertEqual(sorted(testEdges), sorted(self.ifWithAllNestedEdges))
        for i, node in enumerate(testNodes):
            self.assertEqual(f"({node.nodeID}) {node.statement}", self.ifWithAllNestedNodes[i])

if __name__ == "__main__":
    unittest.main(verbosity=2)
