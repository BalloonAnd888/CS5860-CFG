import unittest
from cfg import *

class TestCFGPrograms(unittest.TestCase):
    def setUp(self):
        self.program1Nodes = [
            "(1) while (n != m)",
            "(2) if (n<m)",
            "(3) t = m;",
            "(4) m = t-n;",
        ]

        self.program1Edges = [
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 1),
            (2, 1),
        ]

        self.program2Nodes = [
            "(1) while (n != m)",
            "(2) if (n<m)",
            "(3) t = m;",
            "(4) m = t-n;",
            "(5) x = 1;"
        ]

        self.program2Edges = [
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
            (2, 5),
            (5, 1)
        ]

        self.program3Nodes = [
            "(1) int x = 1;",
            "(2) if (x > 0)",
            "(3) x = x + 1;",
            "(4) while (x < 3);",
            "(5) for (int i = 0; i < 2; i++)",
            "(6) while (x < 5)",
            "(7) x = x + i;",
            "(8) x = x - 1;",
            "(9) x = x * 2;"
        ]

        self.program3Edges = [
            (1, 2),
            (2, 3),
            (2, 8),
            (3, 4),
            (4, 3),
            (4, 5),
            (5, 6),
            (6, 7),
            (7, 6),
            (6, 5),
            (5, 9),
            (8, 9)
        ]

        self.program4Nodes = [
            "(1) int a = 1;",
            "(2) int b = 2;",
            "(3) if (a < b)",
            "(4) a = a + 1;",
            "(5) for (int i = 0; i < 2; i++)",
            "(6) if (b % 2 == 0)",
            "(7) a = a * 2;",
            "(8) while (a < 10)",
            "(9) a = a + i;",
            "(10) a = a - 1;",
            "(11) b = a + b;"
        ]

        self.program4Edges = [
            (1, 2),
            (2, 3),
            (3, 4),
            (3, 10),
            (4, 5),
            (5, 6),
            (6, 7),
            (6, 8),
            (7, 5),
            (8, 9),
            (9, 8),
            (8, 5),
            (5, 11),
            (10, 11)
        ]

    def testProgram1(self):
        self.testNodes, self.testEdges = cfg("examples/programs/program1.txt")
        self.assertEqual(sorted(self.testEdges), sorted(self.program1Edges))
        for i, node in enumerate(self.testNodes):
            self.assertEqual(f"({node.nodeID}) {node.statement}", self.program1Nodes[i])
    
    def testProgram2(self):
        self.testNodes, self.testEdges = cfg("examples/programs/program2.txt")
        self.assertEqual(sorted(self.testEdges), sorted(self.program2Edges))
        for i, node in enumerate(self.testNodes):
            self.assertEqual(f"({node.nodeID}) {node.statement}", self.program2Nodes[i])
    
    def testProgram3(self):
        testNodes, testEdges = cfg("examples/programs/program3.txt")
        self.assertEqual(sorted(testEdges), sorted(self.program3Edges))
        for i, node in enumerate(testNodes):
            self.assertEqual(f"({node.nodeID}) {node.statement}", self.program3Nodes[i])
    
    def testProgram4(self):
        testNodes, testEdges = cfg("examples/programs/program4.txt")
        self.assertEqual(sorted(testEdges), sorted(self.program4Edges))
        for i, node in enumerate(testNodes):
            self.assertEqual(f"({node.nodeID}) {node.statement}", self.program4Nodes[i])

if __name__ == "__main__":
    unittest.main(verbosity=2)
