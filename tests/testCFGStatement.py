import unittest
from cfg import *

class TestCFGStatement(unittest.TestCase):
    def setUp(self):
        self.nodes= [
            "(1) int a = 5;", 
            "(2) double b = 10.5;", 
            "(3) a = a * 2;", 
            "(4) b = b - 3.5;", 
            "(5) a += 1;"
        ]
        
        self.edges = [
            (1, 2), 
            (2, 3), 
            (3, 4), 
            (4, 5)
        ]

    def testCFGStatement(self):
        self.testNodes, self.testEdges = cfg("examples/statement/statement.txt")
        self.assertEqual(self.edges, self.testEdges)

        for i, node in enumerate(self.testNodes):
            self.assertEqual(f"({node.nodeID}) {node.statement}", self.nodes[i])

if __name__ == "__main__":
    unittest.main(verbosity=2)
