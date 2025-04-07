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

        self.nestedNodes = [
            "(1) int x = 0;",
            "(2) for (int i = 0; i < 3; i++)",
            "(3) x = x + 1;",
            "(4) for (int j = 0; j < 2; j++)",
            "(5) x = x + j;",
            "(6) cout << \"End For\" << endl;",
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

    def testSimpleFor(self):
        self.testNodes, self.testEdges = cfg("examples/for/for.txt")
        self.assertEqual(self.edges, self.testEdges)

        for i, node in enumerate(self.testNodes):
            self.assertEqual(f"({node.nodeID}) {node.statement}", self.nodes[i])

    def testNestedFor(self):
        testNodes, testEdges = cfg("examples/for/forNested.txt")
        self.assertEqual(sorted(testEdges), sorted(self.nestedEdges))
        for i, node in enumerate(testNodes):
            self.assertEqual(f"({node.nodeID}) {node.statement}", self.nestedNodes[i])

if __name__ == "__main__":
    unittest.main(verbosity=2)
