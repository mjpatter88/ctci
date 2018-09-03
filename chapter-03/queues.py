from collections import deque

class MyQueue:
    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()

    def push(self, data):
        self.s1.append(data)

    def pop(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

import unittest

class TestMyQueue(unittest.TestCase):

    def test_my_queue(self):
        mq = MyQueue()
        mq.push(1)
        mq.push(2)
        mq.push(3)

        self.assertEqual(1, mq.pop())
        mq.push(4)
        self.assertEqual(2, mq.pop())
        self.assertEqual(3, mq.pop())
        self.assertEqual(4, mq.pop())


if __name__ == '__main__':
    unittest.main()
