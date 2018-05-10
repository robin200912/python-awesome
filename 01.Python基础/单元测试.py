import unittest


def add(x, y):
    return x + y


class test_function(unittest.TestCase):
    def setUp(self):
        print 'init data...'

    def test_add(self):
        print 'go into test method...'
        result = add(1, 2)
        self.assertEqual(result, 3)

    def tearDown(self):
        print 'finished...'