import unittest
from cfg import handleIf 

class TestHandleIf(unittest.TestCase):
    def setUp(self):
        self.lines = [
            "if (x > 5)",
            "{",
            "c = a + b;",
            "a = b + c;",
            "}",
            "a = a * 2;"
        ]

        self.nodes, self.edges = [] , []
        self.i, self.nodeID = 0, 1

    def testHandleIf(self):
        i, nodeID = handleIf(self.lines, self.i, self.nodes, self.nodeID, self.edges)

        self.assertEqual(len(self.nodes), 3)
        self.assertEqual(len(self.edges), 3)
        self.assertEqual(i, 4)
        self.assertEqual(nodeID, 4)

if __name__ == "__main__":
    unittest.main(verbosity=2)
