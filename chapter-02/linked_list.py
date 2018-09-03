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
        return new

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

    def get_from_end(self, k):
        if not self.head:
            return None
        gap = 0
        cur = self.head
        run = self.head
        while run.nxt:
            run = run.nxt
            if gap >= k:
                cur = cur.nxt
            else:
                gap += 1
        if gap == k:
            return cur.data
        else:
            return None

    def delete_node(self, node):
        # Note: cannot use self
        if node.nxt is None:
            assert False
        node.data = node.nxt.data
        node.nxt = node.nxt.nxt

def add_backwards(list1, list2):
    if list1 is None or list2 is None:
        assert False
    new = List()
    l1 = list1.head
    l2 = list2.head
    remainder = 0
    while l1 or l2:
        s = 0
        if l1:
            s += l1.data
            l1 = l1.nxt
        if l2:
            s += l2.data
            l2 = l2.nxt
        s += remainder
        remainder = s // 10
        new.add(s % 10)
    if remainder:
        new.add(remainder)
    return new

def add_forwards(list1, list2):
    if list1 is None or list2 is None:
        assert False
    s1 = []
    s2 = []
    s_sum = []
    cur = list1.head
    while cur:
        s1.append(cur.data)
        cur = cur.nxt
    cur = list2.head
    while cur:
        s2.append(cur.data)
        cur = cur.nxt

    remainder = 0
    while s1 or s2:
        s = 0
        if s1:
            s += s1.pop()
        if s2:
            s += s2.pop()
        s += remainder
        remainder = s // 10
        s_sum.append(s % 10)
    if remainder:
        s_sum.append(remainder)
    new = List()
    while s_sum:
        new.add(s_sum.pop())
    return new



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

    def test_list_from_end(self):
        l = List()
        l.add(1)
        l.add(2)
        l.add(3)
        l.add(1)
        l.add(2)
        l.add(5)
        assert l.get_from_end(0) == 5, l.get_from_end(0)
        assert l.get_from_end(1) == 2, l.get_from_end(1)
        assert l.get_from_end(2) == 1, l.get_from_end(2)
        assert l.get_from_end(5) == 1, l.get_from_end(5)
        assert l.get_from_end(6) == None, l.get_from_end(6)

    def test_list_from_end(self):
        l = List()
        l.add(1)
        n = l.add(2)
        l.add(3)
        l.delete_node(n)
        assert l.get(0) == 1, l.get(0)
        assert l.get(1) == 3, l.get(1)

    def test_add_backwards(self):
        list1 = List()
        list1.add(7)
        list1.add(1)
        list1.add(6)
        list2 = List()
        list2.add(5)
        list2.add(9)
        list2.add(2)
        list_sum = add_backwards(list1, list2)
        assert list_sum.get(0) == 2, list_sum.get(0)
        assert list_sum.get(1) == 1, list_sum.get(1)
        assert list_sum.get(2) == 9, list_sum.get(2)

    def test_add_forwards(self):
        list1 = List()
        list1.add(6)
        list1.add(1)
        list1.add(7)
        list2 = List()
        list2.add(2)
        list2.add(9)
        list2.add(5)
        list_sum = add_forwards(list1, list2)
        assert list_sum.get(0) == 9, list_sum.get(0)
        assert list_sum.get(1) == 1, list_sum.get(1)
        assert list_sum.get(2) == 2, list_sum.get(2)


if __name__ == '__main__':
    unittest.main()
