from collections import defaultdict
class Node:
    def __init__(self, data):
        self.data = data
        self.nxt = None

class List:
    def __init__(self):
        self.head = None

    def add(self, d):
        new = Node(d)

        if self.head is None:
            self.head = new
            return

        n = self.head
        while n.nxt:
            n = n.nxt
        n.nxt = new

    def get(self, i):
        if not self.head:
            assert False
        index = 0
        cur = self.head
        while index < i:
            index += 1
            cur = cur.nxt
            if cur is None:
                assert False
        return cur.data

    def remove(self, i):
        if not self.head:
            assert False
        if i == 0:
            self.head = self.head.nxt
            return

        index = 0
        cur = self.head
        while index < i-1:
            index += 1
            cur = cur.nxt
            if cur is None:
                assert False
        cur.nxt = cur.nxt.nxt

    def dedupe(self):
        if self.head is None or self.head.nxt is None:
            return

        elements = set()

        prev = self.head
        elements.add(prev.data)
        cur = self.head.nxt
        while cur.nxt:
            if cur.data in elements:
                prev.nxt = cur.nxt
            else:
                elements.add(cur.data)
                prev = cur
            cur = cur.nxt

import unittest
class TestList(unittest.TestCase):
    def test_list_add_then_get(self):
        l = List()
        l.add(1)
        l.add(2)
        l.add(3)
        assert l.get(0) == 1
        assert l.get(1) == 2
        assert l.get(2) == 3

    def test_list_delete(self):
        l = List()
        l.add(1)
        l.add(2)
        l.add(3)
        l.remove(0)
        assert l.get(0) == 2
        assert l.get(1) == 3

    def test_list_dedupe(self):
        l = List()
        l.add(1)
        l.add(2)
        l.add(3)
        l.add(1)
        l.add(2)
        l.add(5)
        l.dedupe()
        assert l.get(0) == 1, l.get(0)
        assert l.get(1) == 2, l.get(1)
        assert l.get(2) == 3, l.get(2)
        assert l.get(3) == 5, l.get(3)
if __name__ == '__main__':
    unittest.main()
