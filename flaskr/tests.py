import unittest

import flaskr

class FlaskrTest(unittest.TestCase):

    def test_i_will_always_pass(self):
        self.assertTrue(True)

    def test_i_will_always_fail(self):
        self.assertTrue(False, "This test will always fail, dont panic!")

    def test_i_will_always_error(self):
        raise RuntimeError('Test error!')



if __name__ == '__main__':
    
    unittest.main()
