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

if __name__ == '__main__':
    unittest.main()
