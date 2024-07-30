import unittest
from lib.mysample import myfunc

class TestCase1(unittest.TestCase):

    def test_case_1_1(self):
        ret = myfunc(3, 5)
        self.assertEqual(ret, 8)

if __name__ == "__main__":
    unittest.main()