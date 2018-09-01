import unittest

def unique(s):
    return len(s) == len(set(s))

def unique2(s):
    s = sorted(s)
    for index, c in enumerate(s):
        if index < len(s) - 1 and c == s[index+1]:
            return False

    return True

def reverse(s):
    # c-style, otherwise I would use `reversed`
    result = list(s)
    for i in range(len(s)):
        j = (len(s)-1)-i
        if j <= i:
            break
        result[i], result[j] = s[j], s[i]
    return "".join(result)

def compress(s):
    new = []
    cur = 1
    cur_char = s[0]
    for i in range(1, len(s)):
        if s[i] == cur_char:
            cur += 1
        else:
            new.append(f"{cur_char}{str(cur)}")
            cur_char = s[i]
            cur = 1
    new.append(f"{cur_char}{str(cur)}")
    cur_char = s[i]
    cur = 1
    new_string = "".join(new)
    return new_string if len(new_string) < len(s) else s

def is_perm(s, s2):
    return sorted(s) == sorted(s2)

def expand(s):
    return s.replace(' ', '%20')

class TestUnique(unittest.TestCase):
    def test_unique(self):
        self.assertTrue(unique("michael"))
    def test_not_unique(self):
        self.assertFalse(unique("mmm"))
    def test_not_unique_2(self):
        self.assertFalse(unique("mlmm"))

class TestUnique2(unittest.TestCase):
    def test_unique(self):
        self.assertTrue(unique2("michael"))
    def test_not_unique(self):
        self.assertFalse(unique2("mmm"))
    def test_not_unique_2(self):
        self.assertFalse(unique2("mlmm"))

class TestRevers(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual("cba", reverse("abc"))
    def test_reverse1(self):
        self.assertEqual("a", reverse("a"))
    def test_reverse2(self):
        self.assertEqual("ab", reverse("ba"))

class TestPerm(unittest.TestCase):
    def test_is_perm(self):
        self.assertFalse(is_perm("abc", "amc"))
    def test_is_perm_single(self):
        self.assertTrue(is_perm("ab", "ba"))
    def test_is_perm_double(self):
        self.assertTrue(is_perm("a", "a"))

class TestExpand(unittest.TestCase):
    def test_expand(self):
        self.assertEqual("Mr%20John%20Smith", expand("Mr John Smith"))

class TestCompress(unittest.TestCase):
    def test_compress(self):
        self.assertEqual("michael", compress("michael"))
    def test_compress2(self):
        self.assertEqual("a2b1c5a3", compress("aabcccccaaa"))

if __name__ == '__main__':
    unittest.main()
