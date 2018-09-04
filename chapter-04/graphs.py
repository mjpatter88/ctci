class GraphNode:
    def __init__(self, data):
        self.children = []
        self.data = data
        self.visited = False

    def add_child(self, node):
        self.children.append(node)

def dfs(node):
    l = [node.data]
    node.visited = True
    for n in node.children:
        if not n.visited:
            l.extend(dfs(n))
    return l

from collections import deque
def bfs(node):
    l = []
    q = deque([node])
    while q:
        cur = q.popleft()
        cur.visited = True
        l.append(cur.data)
        for c in cur.children:
            if not c.visited:
                q.append(c)
    return l


import unittest
class TestGraph(unittest.TestCase):
    def setUp(self):
        n1 = GraphNode(1)
        n2 = GraphNode(12)
        n3 = GraphNode(13)
        n4 = GraphNode(14)
        n5 = GraphNode(35)
        n6 = GraphNode(36)
        n1.add_child(n2)
        n1.add_child(n3)
        n1.add_child(n4)
        n3.add_child(n5)
        n3.add_child(n6)
        self.n = n1

    def test_dfs(self):
        self.assertEqual([1, 12, 13, 35, 36, 14], dfs(self.n))

    def test_bfs(self):
        self.assertEqual([1, 12, 13, 14, 35, 36], bfs(self.n))


if __name__ == '__main__':
    unittest.main()
