class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree:
    def __init__(self):
        self.head = None

    def in_order(self, node):
        l = []
        if node.left:
            l.extend(self.in_order(node.left))
        l.append(node.data)
        if node.right:
            l.extend(self.in_order(node.right))
        return l

    def pre_order(self, node):
        l = [node.data]
        if node.left:
            l.extend(self.pre_order(node.left))
        if node.right:
            l.extend(self.pre_order(node.right))
        return l

    def post_order(self, node):
        l = []
        if node.left:
            l.extend(self.post_order(node.left))
        if node.right:
            l.extend(self.post_order(node.right))
        l.append(node.data)
        return l

def balanced(node):
    # returns depth or -1 if not balanced
    l = 0
    r = 0
    if node.left:
        l = balanced(node.left)
    if node.right:
        r = balanced(node.right)
    if l == -1 or r == -1 or abs(l-r) > 1:
        return -1
    return max(l, r) + 1

def get_bst(arr):
    if not arr:
        return None
    if len(arr) == 1:
        return TreeNode(arr[0])
    mid = len(arr) // 2
    head = TreeNode(arr[mid])
    head.left = get_bst(arr[:mid])
    head.right = get_bst(arr[mid:])
    return head

from collections import deque
class LLNode:
    def __init__(self, data):
        self.nxt = None
        self.data = data

def bst_to_lls(bst):
    import math

    lls = []
    q = deque()
    cur_ll_index = -1
    last_val = math.inf
    q.append(bst)
    while q:
        n = q.popleft()
        if n.data < last_val:
            cur_ll_index +=1
            lls.append(LLNode(n.data))

        else:
            lls[cur_ll_index].nxt = LLNode(n.data)

        last_val = n.data
        if n.left:
            q.append(n.left)
        if n.right:
            q.append(n.right)

    return lls

import unittest
class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        n1 = TreeNode(1)
        n2 = TreeNode(2)
        n3 = TreeNode(3)
        n4 = TreeNode(4)
        n5 = TreeNode(5)
        n1.left = n2
        n1.right = n3
        n2.left = n4
        n2.right = n5
        self.t = BinaryTree()
        self.t.head = n1

    def test_binary_tree_in_order(self):
        self.assertEqual([4, 2, 5, 1, 3], self.t.in_order(self.t.head))

    def test_binary_tree_pre_order(self):
        self.assertEqual([1, 2, 4, 5, 3], self.t.pre_order(self.t.head))

    def test_binary_tree_post_order(self):
        self.assertEqual([4, 5, 2, 3, 1], self.t.post_order(self.t.head))

    def test_balanced(self):
        n1 = TreeNode(1)
        n2 = TreeNode(2)
        n3 = TreeNode(3)
        n4 = TreeNode(3)
        n5 = TreeNode(3)
        n1.left = n2
        n1.right = n3
        n2.left = n4
        n3.right = n5
        self.assertEqual(balanced(n1), 3)

    def test_balanced_false(self):
        n1 = TreeNode(1)
        n2 = TreeNode(2)
        n3 = TreeNode(3)
        n1.left = n2
        n2.left = n3
        self.assertEqual(balanced(n1), -1)

    def test_get_bst(self):
        arr = [1,2,3,4,5,6,7,8,9,10]
        head = get_bst(arr)

        self.assertEqual(head.data, 6, head.data)
        self.assertEqual(head.right.data, 8, head.data)
        self.assertEqual(head.left.data, 3, head.data)

    def test_bst_to_lls(self):
        n1 = TreeNode(1)
        n2 = TreeNode(2)
        n3 = TreeNode(3)
        n4 = TreeNode(4)
        n5 = TreeNode(5)
        n3.left = n2
        n2.left = n1
        n3.right = n4
        n4.right = n5
        lls = bst_to_lls(n3)
        self.assertEqual(lls[0].data, 3)
        self.assertEqual(lls[1].data, 2)
        self.assertEqual(lls[1].nxt.data, 4)
        self.assertEqual(lls[2].data, 1)
        self.assertEqual(lls[2].nxt.data, 5)

if __name__ == '__main__':
    unittest.main()
