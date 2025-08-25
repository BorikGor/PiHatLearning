import unittest

def add(a, b):
    return a+b

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3), 5)
        self.assertEqual(add(-1,1), 0)
        self.assertNotEqual(add(2,2), 5)
    
if name = ' main ':
    unittest.main()
