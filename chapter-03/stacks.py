class ArrStacks:
    def __init__(self, stack_size):
        self.l = [None] * (3 * stack_size)
        # Each pointer points to the next open spot
        self.p = [0, stack_size, 2 * stack_size]
        self.size = stack_size

    def push(self, stack_num, data):
        p = self.p[stack_num]
        if (p + 1) % self.size == 0:
            return False
        self.l[p] = data
        self.p[stack_num] += 1
        return True

    def pop(self, stack_num):
        p = self.p[stack_num]
        if (p % self.size) == 0:
            return None
        self.p[stack_num] -= 1
        return self.l[self.p[stack_num]]

    def peek(self, stack_num):
        p = self.p[stack_num]
        if (p % self.size) == 0:
            return None
        return self.l[p - 1]

import unittest

class TestArrStacks(unittest.TestCase):
    def test_arr_stack(self):
        s = ArrStacks(100)
        s.push(0, 1)
        s.push(0, 2)
        s.push(1, 3)
        s.push(2, 4)

        self.assertEqual(4, s.peek(2))
        self.assertEqual(4, s.pop(2))
        self.assertEqual(None, s.pop(2))

        self.assertEqual(3, s.peek(1))
        self.assertEqual(3, s.pop(1))

        self.assertEqual(2, s.pop(0))
        self.assertEqual(1, s.pop(0))

from collections import deque
class StackMin:
    def __init__(self):
        self.s = deque()
        self.mins = deque()

    def push(self, data):
        if not self.mins or data <= self.mins[-1]:
            self.mins.append(data)
        self.s.append(data)

    def pop(self):
        d = self.s.pop()
        if d == self.mins[-1]:
            self.mins.pop()
        return d

    def min(self):
        return self.mins[-1]


class TestStackMin(unittest.TestCase):
    def test_stack_min(self):
        s = StackMin()
        s.push(5)
        s.push(1)
        s.push(2)

        self.assertEqual(1, s.min())
        s.pop()
        s.pop()
        self.assertEqual(5, s.min())

class SetOfStacks:
    def __init__(self, limit):
        self.stacks = [deque()]
        self.limit = limit
        self.s_index = 0

    def push(self, data):
        if len(self.stacks[self.s_index]) == self.limit:
            self.stacks.append(deque())
            self.s_index += 1
        self.stacks[self.s_index].append(data)

    def pop(self):
        if len(self.stacks[self.s_index]) == 0:
            self.s_index -= 1
            self.stacks.pop()
        return self.stacks[self.s_index].pop()

    def pop_at(self, stack_index):
        return self.stacks[stack_index].pop()


class TestSetOfStacks(unittest.TestCase):
    def test_set_of_stacks(self):
        s = SetOfStacks(2)
        s.push(5)
        s.push(1)
        s.push(2)

        self.assertEqual(2, s.pop())
        self.assertEqual(1, s.pop())
        self.assertEqual(5, s.pop())

    def test_set_of_stacks_pop_at_index(self):
        s = SetOfStacks(2)
        s.push(5)
        s.push(1)
        s.push(2)

        self.assertEqual(1, s.pop_at(0))
        self.assertEqual(2, s.pop())
        self.assertEqual(5, s.pop())

class Towers:
    def __init__(self):
        self.stacks = [deque([6,5,4,3,2,1]), deque(), deque()]

    def solve(self):
        self.move(6, 0, 2)

    def move(self, amount, start, end):
        if amount == 1:
            self.stacks[end].append(self.stacks[start].pop())
        else:
            step =({0,1,2} - {start, end}).pop()
            self.move(amount-1, start, step)
            self.move(1, start, end)
            self.move(amount-1, step, end)


class TestTowers(unittest.TestCase):
    def test_towers(self):
        t = Towers()
        t.solve()

        self.assertEqual(1, t.stacks[2].pop())
        self.assertEqual(2, t.stacks[2].pop())
        self.assertEqual(3, t.stacks[2].pop())
        self.assertEqual(4, t.stacks[2].pop())
        self.assertEqual(5, t.stacks[2].pop())
        self.assertEqual(6, t.stacks[2].pop())



if __name__ == '__main__':
    unittest.main()
