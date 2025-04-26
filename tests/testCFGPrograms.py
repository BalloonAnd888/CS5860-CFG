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

if __name__ == "__main__":
    unittest.main(verbosity=2)
