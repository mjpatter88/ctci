import unittest

def rotate(img):
    n = len(img)
    new = []
    for i in range(n):
        new.append([''] * n)
    for row in range(n):
        for col in range(n):
            new[col][(n-1)-row] = img[row][col]
    return new

def zero(img):
    rows = len(img)
    cols = len(img[0])
    new = []
    for row in range(rows):
        new.append([''] * cols)
    for row in range(rows):
        for col in range(cols):
            if img[row][col] == 0:
                for r in range(rows):
                    new[r][col] = 0
                for c in range(cols):
                    new[row][c] = 0
            elif new[row][col] != 0:
                new[row][col] = img[row][col]
    return new

class TestUnique(unittest.TestCase):
    def test_rotate(self):
        inp = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        expected = [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]
        self.assertEqual(expected, rotate(inp))

    def test_zero(self):
        inp = [[1, 2, 0, 4], [5, 6, 7, 8], [9, 0, 11, 12], [13, 14, 15, 16]]
        expected = [[0, 0, 0, 0], [5, 0, 0, 8], [0, 0, 0, 0], [13, 0, 0, 16]]
        self.assertEqual(expected, zero(inp))


if __name__ == '__main__':
    unittest.main()
