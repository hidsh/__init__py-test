import unittest
from my_package import say_hoge

class TestHoge(unittest.TestCase):
    def test_say_hoge(self):
        result = say_hoge()
        self.assertEqual(result, 'hoge!!!');


if __name__ == '__main__':
    unittest.main()
