import unittest
from concat_remove_library import Concat_Remove_Class


class ConcatRemoveTestCase(unittest.TestCase):

    def test0(self):
        s = "blablablabla"
        t = "blablabcde"
        k = 8

        self.concatRem = Concat_Remove_Class(s, t, k)

        self.assertEqual(self.concatRem.getData(), True)

    def test1(self):
        s = "tab"
        t = "tab"
        k = 7

        self.concatRem = Concat_Remove_Class(s, t, k)

        self.assertEqual(self.concatRem.getData(), True)

    def test2(self):
        s = "hernani"
        t = "nani"
        k = 5

        self.concatRem = Concat_Remove_Class(s, t, k)

        self.assertEqual(self.concatRem.getData(), True)


    def test3(self):
        s = "HERNANi"
        t = "nani"
        k = 2

        self.concatRem = Concat_Remove_Class(s, t, k)

        self.assertEqual(self.concatRem.getData(), False)
    def test4(self):
        s = "125"
        t = "nani"
        k = 2
        self.concatRem = Concat_Remove_Class(s, t, k)

        self.assertEqual(self.concatRem.getData(), False)


if __name__ == '__main__':
    unittest.main()