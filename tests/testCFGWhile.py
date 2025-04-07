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

if __name__ == "__main__":
    unittest.main(verbosity=2)
