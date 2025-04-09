import unittest
from cfg import *

class TestCFGIWhileStatement(unittest.TestCase):
    def setUp(self):
        self.simpleNodes = [
            "(1) int x = 0;",
            "(2) while (x < 5)",
            "(3) x = x + 1;",
            "(4) y = y + 3;",
            "(5) x = x * 2;"
        ]

        self.simpleEdges = [
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 2),
            (2, 5)
        ]

        self.nestedNodes = [
            "(1) int x = 0;",
            "(2) while (x < 5)",
            "(3) x = x + 1;",
            "(4) while (x < 3)",
            "(5) x = x + 2;",
            "(6) cout << \"Hi\" << endl;",
            "(7) x = x * 2;"
        ]

        self.nestedEdges = [
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
            (5, 4),
            (4, 6),
            (6, 2),
            (2, 7)
        ]
    
        self.whileWithAllNestedNodes = [
            "(1) int x = 0;",
            "(2) while (x < 10)",
            "(3) x = x + 1;",
            "(4) while (x < 5)",
            "(5) x = x + 2;",
            "(6) for (int i = 0; i < 2; i++)",
            "(7) x = x * 2;",
            "(8) x = x - 1;",
            "(9) while (x > 0);",
            "(10) if (x == 0)",
            "(11) x = x + 100;",
            "(12) x++;",
            "(13) x = x - 3;"
        ]

        self.whileWithAllNestedEdges = [
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
            (5, 4),
            (4, 6),
            (6, 7),
            (7, 6),
            (6, 8),
            (8, 9),
            (9, 8),
            (9, 10),
            (10, 11),
            (10, 12),
            (11, 12),
            (12, 2),
            (2, 13)
        ]

    def testSimpleWhile(self):
        self.testNodes, self.testEdges = cfg("examples/while/while.txt")
        self.assertEqual(sorted(self.testEdges), sorted(self.simpleEdges))
        for i, node in enumerate(self.testNodes):
            self.assertEqual(f"({node.nodeID}) {node.statement}", self.simpleNodes[i])

    def testNestedWhile(self):
        self.testNodes, self.testEdges = cfg("examples/while/whileNested.txt")
        self.assertEqual(sorted(self.testEdges), sorted(self.nestedEdges))
        for i, node in enumerate(self.testNodes):
            self.assertEqual(f"({node.nodeID}) {node.statement}", self.nestedNodes[i])
    
    def testWhileWithAllNested(self):
        testNodes, testEdges = cfg("examples/while/whileWithOther.txt")
        self.assertEqual(sorted(testEdges), sorted(self.whileWithAllNestedEdges))
        for i, node in enumerate(testNodes):
            self.assertEqual(f"({node.nodeID}) {node.statement}", self.whileWithAllNestedNodes[i])

if __name__ == "__main__":
    unittest.main(verbosity=2)
